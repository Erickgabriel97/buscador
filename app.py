from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pergunta', methods=['POST'])
def pergunta():
    nome = request.form['nome']
    if nome == 'Larissa Yumi Ferreira Ogata':
        return render_template('pergunta.html')  # Renderiza a pergunta
    else:
        return "Nome incorreto. Tente novamente."

@app.route('/resposta', methods=['POST'])
def resposta():
    resposta = request.form['resposta']
    if resposta == 'sim':
        return "Eu te amo! 💖"
    else:
        return "Você não pode clicar nesse botão! Tente novamente."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
