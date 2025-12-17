from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
    global pages
    
    # URL Base corrigida (en.wikipedia.org) e sem o erro de digitação ";"
    url_completa = "https://en.wikipedia.org" + pageUrl
    
    # Adicionado Header para não tomar Block 403 da Wikipedia
    req = Request(
        url_completa, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    )

    try:
        html = urlopen(req)
        bsObj = BeautifulSoup(html, 'html.parser')
        
        # --- Bloco de Extração de Dados ---
        # 1. Título
        print("\nTítulo:", bsObj.h1.get_text())
        
        # 2. Primeiro parágrafo
        # Correção: O ID correto é 'mw-content-text' e usamos find("p") para pegar o primeiro
        content = bsObj.find(id="mw-content-text")
        # Verifica se achou o conteúdo antes de tentar pegar o parágrafo
        if content:
             # Pega todos os 'p', seleciona o primeiro [0] e pega o texto
            paragraphs = content.find_all("p")
            if len(paragraphs) > 0:
                print("Primeiro parágrafo:", paragraphs[0].get_text())
        
        # 3. Link de Editar
        edit_tag = bsObj.find(id="ca-edit")
        if edit_tag:
            link = edit_tag.find("span").find("a").attrs["href"]
            print("Link de edição:", link)
            
    except AttributeError as e:
        print(f"Algum atributo não foi encontrado na página: {e}")
    except Exception as e:
        print(f"Erro geral: {e}")
        
    # --- Bloco de Recursão (Buscar novos links) ---
    for ligacao in bsObj.find_all("a", href=re.compile("^(/wiki/)")):
        if 'href' in ligacao.attrs: # Correção: .attrs
            if ligacao.attrs['href'] not in pages:
                # Encontrou nova página
                new_page = ligacao.attrs['href']
                print("-" * 20)
                print("Indo para: " + new_page)
                
                pages.add(new_page)
                getLinks(new_page)

getLinks("")