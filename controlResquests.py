from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
from mysql.connector import Error
from fastapi.responses import JSONResponse

# conexão com  o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='xxx',
    password='xxxx',
    database='xxxx',
)


class Dados(BaseModel):
    usuario: str
    senha: str

class CadastroUsuario(BaseModel):
    nome: str
    login: str
    senha: str
    confirmar_senha: str 

class SenhaUsuario(BaseModel):
    login: str
    antiga_senha: str
    nova_senha: str

app = FastAPI()

@app.post("/validar-login/")
def validar_login(dados: Dados):
    # O codigo retorna a 'senha' do login digitado pelo o usuario, se o login digitado for igual ao que consta no BD. E depois guarda ela na variavel "resultado". 
    try:
        cursor = conexao.cursor()
        cursor.execute('SELECT senha FROM usuarios WHERE login_usuario = %s', (dados.usuario,))
        resultado = cursor.fetchall()
    except Error as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    finally:
        cursor.close()

    # se a login/senha não constar/não foi encontrada no BD, o codigo abaixo é executado:
    if not resultado:
        return JSONResponse(content={"message": "NÃO FOI POSSÍVEL LOGAR! Usuário não encontrado."})
    
    # Caso conste e os dados sejam iguais, o codigo abaixo é executado. O codigo compara a senha digitada pelo o usuario com a senha retornada do BD. 
    elif dados.senha.strip() == resultado[0][0].strip():
        return JSONResponse(content={"message": "LOGADO!"})
    else:
        return JSONResponse(content={"message": "NÃO FOI POSSÍVEL LOGAR! Senha incorreta."})



@app.post("/cadastrar-dados/")
def cadastrar_dados(cadastrar: CadastroUsuario):

# se a senha for igual a senha repetida, o código abaixo sera executado:
    if (cadastrar.senha  == cadastrar.confirmar_senha):

        try:
            cursor = conexao.cursor()
            cursor.execute('INSERT INTO usuarios (nome_usuario, login_usuario, senha) VALUES (%s, %s, %s)', (cadastrar.nome, cadastrar.login, cadastrar.senha))
            conexao.commit()
            return JSONResponse(content={"message": "Usuário cadastrado com sucesso!"})
        except Error as e:
            return JSONResponse(content={"error": str(e)}, status_code=500)
        finally:
            cursor.close()

@app.put("/mudar-senha/")
def atualizar_senha(senhas: SenhaUsuario):
    try:
        cursor = conexao.cursor()
        # Verifica se o login existe e se a senha antiga está correta de acordo com o BD. Se sim, a senha é guardada dentro da variavael "resultado".
        cursor.execute('SELECT senha FROM usuarios WHERE login_usuario = %s', (senhas.login,))
        resultado = cursor.fetchone()

        # se o login não existir dentro do banco de dados, a senha não é retornada, e o codigo abaixo é executado. 
        if not resultado:
            return JSONResponse(content={"message": "Login de usuário incorreto!"}, status_code=404)
        
        # se login/senha constar no BD, a senha retornada do BD é guardada dentro desta variavel.
        senha_bd = resultado[0]
        
        # Verifica se os campos estão preenchidos pelo o usuario.
        if not senhas.antiga_senha or not senhas.nova_senha:
            return JSONResponse(content={"message": "Não foi possivel atualizar a senha. Preencha todos os CAMPOS!"},  status_code=400)
        
        # Verifica se a senha antiga é diferente da senha do BD. Se sim, o codigo abaixo é executado.
        elif senhas.antiga_senha != senha_bd:
            print('Senha atual incorreta!')
            return JSONResponse(content={"message": "Senha atual incorreta!"}, status_code=400)
        
        else:
            cursor.execute('UPDATE usuarios SET senha = %s WHERE login_usuario = %s', (senhas.nova_senha, senhas.login))
            conexao.commit()

        return JSONResponse(content={"message": "Senha de usuário atualizada com sucesso!"}, status_code=200)
    
    except Error as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
    finally:
        cursor.close()



