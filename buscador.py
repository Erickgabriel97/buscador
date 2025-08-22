from serpapi import GoogleSearch
import pandas as pd

# Sua chave da SerpApi
API_KEY = "f663c2ffa0c2bd96c493bdc24b9e61e6355da514dfc0e2c6cc0726b01dfb1f7a"

def buscar_produto(produto):
    params = {
        "engine": "google_shopping",
        "q": produto,   # termo de busca
        "hl": "pt",     # idioma
        "gl": "br",     # país (Brasil)
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

if __name__ == "__main__":
    produto = input("Digite o nome do produto que deseja pesquisar: ")
    df = buscar_produto(produto)

    if df.empty:
        print("Nenhum resultado encontrado.")
    else:
        print("\nResultados encontrados:\n")
        print(df)

        # salva em CSV
        nome_arquivo = f"{produto.replace(' ', '_')}_resultados.csv"
        df.to_csv(nome_arquivo, index=False, encoding="utf-8-sig")
        print(f"\nResultados salvos em: {nome_arquivo}")
