from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

# Correção 1: Seed vazia usa o relógio do sistema (datetime.now geraria erro)
random.seed()

def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    
    # Cria o padrão Regex: Começa com "/" OU contém a URL do site
    pattern = re.compile("^(/|.*" + includeUrl + ")")
    
    for link in bsObj.findAll("a", href=pattern):
        if 'href' in link.attrs:
            url = link.attrs['href']
            
            # Verificamos apenas se já não salvamos esse link na lista atual
            if url not in internalLinks:
                internalLinks.append(url)
                
    return internalLinks

def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    
    # Cria o padrão Regex: Começa com "http" OU "www" E NÃO contém a URL do site
    pattern = re.compile("^(http|www)((?!" + excludeUrl + ").)*$")
    
    for link in bsObj.findAll("a", href=pattern):
        if 'href' in link.attrs:
            url = link.attrs['href']
            
            # Verificamos apenas se já não salvamos esse link na lista atual
            if url not in externalLinks:
                externalLinks.append(url)
                
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    
    # Extrai o domínio base da URL
    domain = splitAddress(startingPage)[0]
    
    externalLinks = getExternalLinks(bsObj, domain)
    
    if len(externalLinks) == 0:
        print("Nenhum link externo encontrado, procurando em links internos...")
        internalLinks = getInternalLinks(bsObj, domain)
        if len(internalLinks) == 0:
            print("Nenhum link interno encontrado. Fim da busca.")
            return None
        else:
            return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]
    
def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    if externalLink:
        print("Indo para o link externo: " + externalLink)
        followExternalOnly(externalLink)
followExternalOnly("http://oreilly.com")

#Coleta uma lista de todos os URLS externos encontrados no site
allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    
    domain = splitAddress(siteUrl)[0]
    
    internalLinks = getInternalLinks(bsObj, domain)
    externalLinks = getExternalLinks(bsObj, domain)
    
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
            
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            print("Coletando links internos: " + link)
            getAllExternalLinks(link)
            
getAllExternalLinks("http://oreilly.com")
#Fim