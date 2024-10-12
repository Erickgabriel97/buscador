from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1 style='color: black;'>Olá, bem-vinda ao meu aplicativo!</h1>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Usa a porta do ambiente ou 5000 como padrão
    app.run(host='0.0.0.0', port=port, debug=True)
