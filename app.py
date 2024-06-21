from flask import Flask, request

app = Flask(__name__)

@app.route('/tela de compras')
def ofc():
    return 'Site em desenvolvimento: '

@app.route("/registro" , methods=['post'])
def registro1():
    nome = request.form['nome']
    cpf = request.form['cpf']
    return 'O nome enviado é: ' + nome + '<br> seu cpf: '+cpf


@app.route("/")
def hello_world():
    return '''<!DOCTYPE html>
        <html lang="pt-br">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Formulário de Cadastro</title>
        </head>
        <body>
        <h1>Formulário de Cadastro</h1>
        <p>Formulario para cadastro de compra no nosso banco de dados <br> Por Favore Prencha o formulario a Baixo</p>
        <form action="/registro" method="post">
            <label for="nome">Nome Completo:</label><br>
            <input type="text" id="nome" name="nome" required><br><br>
            
            <label for="cpf">CPF DA PESSOA:</label><br>
            <input type="text" id="cpf" name="cpf" pattern="\d{3}\.\d{3}\.\d{3}-\d{2}" placeholder="000.000.000-00" required><br><br>
            
            <input type="submit" value="Enviar">
        </form>
        </body>
        </html>'''