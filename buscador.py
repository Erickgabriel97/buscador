from flask import Flask, request, render_template_string
from serpapi import GoogleSearch
import pandas as pd

API_KEY = "663c2ffa0c2bd96c493bdc24b9e61e6355da514dfc0e2c6cc0726b01dfb1f7a"

app = Flask(__name__)  # precisa estar fora de qualquer função ou bloco

def buscar_produto(produto):
    params = {
        "engine": "google_shopping",
        "q": produto,
        "hl": "pt",
        "gl": "br",
        "api_key": API_KEY
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    itens = []
    for item in results.get("shopping_results", []):
        itens.append({
            "loja": item.get("source"),
            "titulo": item.get("title"),
            "preco": item.get("price"),
            "link": item.get("link")
        })
    return pd.DataFrame(itens)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        produto = request.form.get("produto")
        df = buscar_produto(produto)
        if df.empty:
            tabela = "<p>Nenhum resultado encontrado.</p>"
        else:
            tabela = df.to_html(classes="table table-striped", index=False, escape=False)
        return render_template_string("""
            <h2>Resultados da busca</h2>
            {{ tabela | safe }}
            <br><a href="/">🔙 Nova busca</a>
        """, tabela=tabela)
    return """
        <h1>🔍 Buscador de Preços</h1>
        <form method="post">
            <input type="text" name="produto" placeholder="Digite o produto" required>
            <button type="submit">Buscar</button>
        </form>
    """

# Não é necessário rodar app.run() no Render
