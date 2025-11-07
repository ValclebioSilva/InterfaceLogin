Projeto Interface de Login
Este é um projeto de uma interface de login de usuário (frontend) desenvolvida em Python. A interface gráfica foi construída utilizando a biblioteca customtkinter para um visual mais moderno, e a validação do login é feita através de requisições HTTP a um servidor backend, utilizando a biblioteca requests.


Funcionalidades
Interface gráfica moderna e limpa para login.

Campos para inserção de nome de usuário e senha.

Comunicação com um servidor (backend) para autenticação.

Exibição de mensagens de feedback (sucesso ou erro) para o usuário.

Tecnologias Utilizadas
Python 3

CustomTkinter: Para a criação da interface gráfica de usuário (GUI).

Requests: Para realizar as chamadas HTTP (POST) para o servidor de autenticação.

Como Executar o Projeto
Para executar este projeto, você precisará ter o Python 3 instalado, bem como as bibliotecas listadas no arquivo requirements.txt.

1. Clonar o Repositório:

Bash

git clone https://github.com/ValclebioSilva/InterfaceLogin.git
cd InterfaceLogin
2. Criar um Ambiente Virtual (Recomendado):

Bash

# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
3. Instalar as Dependências: O projeto depende de requests e customtkinter. Você pode instalá-las usando o requirements.txt:

Bash

pip install -r requirements.txt
4. Executar a Aplicação: O arquivo principal que inicia a interface é o telaLogin.py.

Bash

python telaLogin.py
:warning: Pré-requisito Importante: O Backend
Este projeto é apenas o cliente (frontend).

O arquivo controlResquests.py é responsável por enviar os dados de login para um servidor (backend) que deve estar rodando e ouvindo por requisições. Para que o login funcione corretamente, você deve ter um servidor backend executando e respondendo na URL para a qual o controlResquests.py está apontando.

Estrutura do Projeto
telaLogin.py: O arquivo principal da aplicação. É responsável por criar a janela, os widgets (campos de usuário, senha, botão) e por instanciar o ControlRequest.

controlResquests.py: Contém a classe ControlRequest. Esta classe gerencia a lógica de fazer a requisição HTTP (POST) para o servidor backend, enviando o usuário e a senha para validação.

requirements.txt: Lista as bibliotecas Python necessárias para rodar o projeto.

Autor
Valclebio Silva - GitHub

