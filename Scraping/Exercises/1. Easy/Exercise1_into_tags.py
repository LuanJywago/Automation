# Acesse o URL http://quotes.toscrape.com. 
# Utilize o bs4 para encontrar e imprimir o texto da primeira citação (quote) que aparece na página (apenas o texto da frase). 
# Dica: Use .find() com a classe específica.

from bs4 import BeautifulSoup
import requests

#informa o URL
url = "http://quotes.toscrape.com"
response = requests.get(url)

#Define o objeto soup 
soup = BeautifulSoup(response.content,"html.parser")

#Encontra e imprime o text da primeira citação
coment = soup.find(class_="text").get_text()
print(coment)
