# Acesse o URL http://books.toscrape.com. 
# Extraia e imprima o nome da categoria de livros que está na barra lateral esquerda 
# (apenas a primeira que aparecer, geralmente é "Travel"). 
# Dica: Inspecione o elemento no navegador para ver a hierarquia.

from bs4 import BeautifulSoup
import requests

url = "http://books.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

##########################################################
################### USAR UM OU OUTRO #####################
##########################################################

# Encontra e improme o nome da primeira categoria na posição [1]
category = soup.find(class_="nav-list").find_all("a")[1].get_text().strip()
print(category)

# Encontra e imprime o nome de todas as categorias
# Ele navega pela classe "nav-list", encontra os elementos
# Procura apenas o tag <a> dentro dela e imprime o conteúdo
for cat in soup.find(class_="nav-list").find_all("a"):
    print(cat.get_text().strip())
