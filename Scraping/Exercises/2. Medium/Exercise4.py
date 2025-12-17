#### Missão:

# Acesse http://books.toscrape.com.

# Extraia o título completo de todos os 20 livros da primeira página.

# Dica de Ouro: Inspecione o HTML do título de um livro longo (como o "Sharp Objects"). Você verá que o texto visível está cortado, mas o título completo está escondido dentro de um atributo da tag <a>.

# Lembra do exemplo lá do início? Para pegar texto usamos .get_text(). Para pegar um atributo (como href, src, title), usamos colchetes, igual a um dicionário: tag['nome_do_atributo'].

from bs4 import BeautifulSoup
import requests

url = "http://books.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

titles_h3 = soup.find_all("h3")
for item in titles_h3:
    book_title = item.find("a")["title"]
    print(book_title)
