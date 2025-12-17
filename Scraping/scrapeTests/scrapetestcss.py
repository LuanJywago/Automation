from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/warandpeace.html"

try:
    html = urlopen(url)

    bsObj = BeautifulSoup(html, "html.parser")
    print(bsObj)
      
except HTTPError as e:
    print(f"Ocorreu um erro {e}")
    
except Exception as e:
    print(f"Ocorreu outro erro {e}")
    
if bsObj:    
    name_list = bsObj.findAll(text = "the prince")
    print(f" Resultado da busca: {len(name_list)}") #Retorno = 7 resultados
    
    #name_list = bsObj.findAll("span", {"class": "green"})
    #print("Nome das pessoas de VERDE:")
    #for name in name_list:
        #print(name.get_text())
else:
    print("Foi foi posível realizar o scraping.")