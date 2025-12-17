from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

#Define a URL
url = "http://pythonscraping.com/pages/page3.html"

#Faz a abertura e leitura da URL
html = urlopen(url)
bsObj = BeautifulSoup(html, "html.parser")

#Procura no HTML os gifts presentes
def listar_presentes():
    gifts_name = bsObj.find_all(class_ = "gift")
    print("Presentes disponíveis:")
    #laço para percorrer todos os dados da classe gift
    for gifts in gifts_name:
        print(gifts.get_text().strip())
        
pergunta = input("Função desejada: 1 (Lista os presentes)")
if pergunta == "1":
    listar_presentes()
else:
    print("insira uma resposta compatível.")