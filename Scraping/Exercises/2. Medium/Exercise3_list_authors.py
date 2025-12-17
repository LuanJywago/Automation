# Acesse http://quotes.toscrape.com. 
# Faça um loop para listar todos os autores presentes na primeira página. 
# Dica: Lembre-se que existem vários elementos repetidos. 
# O find_all cria uma lista, e você itera sobre ela.

from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

authors = soup.find_all(class_="author")
print("\nAll the authors: \n")

for author in authors:
    print(author.get_text())

