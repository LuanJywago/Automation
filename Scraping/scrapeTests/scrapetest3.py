from urllib.request import urlopen, Request # Importe Request também
from bs4 import BeautifulSoup
import random
import re

random.seed()

def getLinks(articleUrl):
    url = "http://en.wikipedia.org" + articleUrl
    
    # Cria uma requisição com um cabeçalho de "User-Agent" falso
    # Isso faz a Wikipedia achar que você é um navegador Chrome no Windows
    req = Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    )
    
    html = urlopen(req)
    bsObj = BeautifulSoup(html, 'html.parser')
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")

while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)