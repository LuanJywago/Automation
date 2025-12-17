from bs4 import BeautifulSoup
import requests

url = "http://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# 1. Encontramos o "container" de cada livro
livros = soup.find_all("article", class_="product_pod")

for livro in livros:
# O título completo está no atributo 'title' dentro do link <a> que está dentro do <h3>
    titulo = livro.find("h3").find("a")["title"]
    
    # --- EXTRAÇÃO DO PREÇO ---
    # O preço está numa classe 'price_color'. Ex: "£51.77"
    preco_texto = livro.find("p", class_="price_color").get_text()
    

    # Passo 1: Remover o símbolo '£'.
    # Como o símbolo é o primeiro caractere (índice 0), pegamos do índice 1 até o fim.
    preco_limpo = preco_texto[1:] # Isso transforma "£51.77" em "51.77"
    
    # Passo 2: Converter de string para float (número real)
    preco_final = float(preco_limpo)
    
    # --- RESULTADO ---
    print(f"Título: {titulo}")
    print(f"Preço original: {preco_texto} | Preço numérico: {preco_final}")
    
    # Prova real que virou número (pode fazer conta):
    # print(f"Preço com 10% de desconto: {preco_final * 0.9:.2f}") 
    print("-" * 40)