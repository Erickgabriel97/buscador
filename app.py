from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verificar_nome', methods=['POST'])
def verificar_nome():
    data = request.get_json()
    nome = data.get('nome')
    if nome == "Larissa Yumi Ferreira Ogata":
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

if __name__ == "__main__":
    app.run(debug=True)
