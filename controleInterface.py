from PyQt5 import uic, QtWidgets
from mysql.connector import Error
import requests


def logar():
    primeiraTela.label_5.setText("")
    usuario = primeiraTela.lineEdit.text()
    senha = primeiraTela.lineEdit_2.text()
    try:
        response = requests.post(
            "http://127.0.0.1:8000/validar-login/",
            json={"usuario": usuario, "senha": senha}
        )
        if response.status_code == 200:
            data = response.json()
            if data.get("message") == 'LOGADO!':
                print('Você esta LOGADO!')
                segunndaTela.show()
                primeiraTela.close()
            
            elif not usuario or not senha:
                primeiraTela.label_5.setText("Preencha todos os CAMPOS!")

            else:
                print('Dados de login incorretos!')
                primeiraTela.label_5.setText("Dados de login incorretos!")
                primeiraTela.lineEdit.setText("")
                primeiraTela.lineEdit_2.setText("")
        else:
            print('Erro ao verificar login:', response.json())
            primeiraTela.label_5.setText("Erro ao verificar login.")
            primeiraTela.lineEdit.setText("")
            primeiraTela.lineEdit_2.setText("")

    except requests.exceptions.RequestException as e:
        print(f'Erro ao conectar com a API: {e}')


def logout():
    primeiraTela.show()
    segunndaTela.close()
    primeiraTela.lineEdit.setText("")
    primeiraTela.lineEdit_2.setText("")


def open_cadastro():
    tela_cadastro.show()

def cadastrar():
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_2.text()
    senha = tela_cadastro.lineEdit_3.text()
    confirmar_senha = tela_cadastro.lineEdit_4.text()

    if senha != confirmar_senha:
        tela_cadastro.label_2.setText("As senhas digitadas estão diferentes!")
        tela_cadastro.lineEdit_3.setText("")
        tela_cadastro.lineEdit_4.setText("")

    elif not senha or not confirmar_senha:
        print('Preecha todos os campos p/ finalizar o seu cadastro!')
        tela_cadastro.label_2.setText("Preecha todos os campos p/ finalizar!")
        return

    try:
        response = requests.post(
            "http://127.0.0.1:8000/cadastrar-dados/",
            json={"nome": nome, "login": login, "senha": senha, "confirmar_senha": confirmar_senha}
        )
        if response.status_code == 200:
            print('Usuário cadastrado com SUCESSO!')
            tela_cadastro.label_2.setText("Usuário cadastrado com sucesso!")
            tela_cadastro.lineEdit.setText("")
            tela_cadastro.lineEdit_2.setText("")
            tela_cadastro.lineEdit_3.setText("")
            tela_cadastro.lineEdit_4.setText("")
        else:
            print('Não foi possível cadastrar o usuário', response.json())

    except requests.exceptions.RequestException as erro:
        print('Erro ao conectar com a API:', erro)
        

def back_logar():
    tela_cadastro.close()
    primeiraTela.show()

def openMudarSenha():
    telaMudarSenha.show()

def mudaSenha():
    login = telaMudarSenha.lineEdit.text()
    senhaAnt = telaMudarSenha.lineEdit_2.text()
    senhaNova = telaMudarSenha.lineEdit_3.text()

    try:
        response = requests.put(
            "http://127.0.0.1:8000/mudar-senha/",
            json={"login": login, "antiga_senha": senhaAnt, "nova_senha": senhaNova}
        )

        # Verifica se os campos estão preenchidos pelo o usuario no FRONT.
        if not senhaAnt or not senhaNova:
            telaMudarSenha.label_2.setText('Preencha todos os CAMPOS!')

        elif response.status_code == 200: 
            print('Senha atualizada com sucesso!')
            telaMudarSenha.label_2.setText('Senha atualizada com SUCESSO!')
            telaMudarSenha.lineEdit.setText("")
            telaMudarSenha.lineEdit_2.setText("")
            telaMudarSenha.lineEdit_3.setText("")
        
        else: 
            print('Não foi possível atualizar os dados!')
            telaMudarSenha.label_2.setText('Não foi possível atualizar nova senha!')
            telaMudarSenha.lineEdit_2.setText("")
            telaMudarSenha.lineEdit_3.setText("")
    
    except requests.exceptions.RequestException as erro:
        print('Erro ao conectar com a API:', erro)
    
def close_mudar_senha():
    telaMudarSenha.close()
    primeiraTela.show()




app=QtWidgets.QApplication([])
primeiraTela=uic.loadUi("Tela_login.ui")
segunndaTela=uic.loadUi("Tela_logout.ui")
tela_cadastro=uic.loadUi("Tela_Cadastro.ui")
telaMudarSenha=uic.loadUi("Tela_MudarSenha.ui")
primeiraTela.pushButton.clicked.connect(logar)
segunndaTela.pushButton.clicked.connect(logout)
primeiraTela.pushButton_2.clicked.connect(open_cadastro)
tela_cadastro.pushButton.clicked.connect(cadastrar)
tela_cadastro.pushButton_2.clicked.connect(back_logar)
primeiraTela.pushButton_3.clicked.connect(openMudarSenha)
telaMudarSenha.pushButton.clicked.connect(mudaSenha)
telaMudarSenha.pushButton_2.clicked.connect(close_mudar_senha)
primeiraTela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

primeiraTela.show()
app.exec()