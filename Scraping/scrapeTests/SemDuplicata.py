from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

pages = set()

def salvar_no_arquivo(url):
    """
    Função auxiliar para salvar o URL no arquivo txt.
    O uso do 'with' garante que o arquivo é salvo e fechado 
    imediatamente após a escrita.
    """
    try:
        # Modo 'a' significa APPEND (adicionar ao final)
        with open('urls_salvas.txt', 'a', encoding='utf-8') as f:
            f.write(url + '\n')
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")

def getLinks(pageUrl):
    global pages
    
    url_completa = "http://en.wikipedia.org" + pageUrl
    
    # Headers para evitar Erro 403
    req = Request(
        url_completa, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
    )
    
    try:
        html = urlopen(req)
        bsObj = BeautifulSoup(html, 'html.parser')
        
        for ligacao in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
            if 'href' in ligacao.attrs:
                if ligacao.attrs["href"] not in pages:
                    # Novo link encontrado
                    new_page = ligacao.attrs["href"]
                    
                    # 1. Mostra na tela
                    print(f"Encontrado e salvando: {new_page}")
                    
                    # 2. Adiciona ao set (para não repetir)
                    pages.add(new_page)
                    
                    # 3. SALVA NO ARQUIVO IMEDIATAMENTE
                    salvar_no_arquivo(new_page)
                    
                    # 4. Continua a busca (Recursão)
                    getLinks(new_page)
                    
    except Exception as e:
        print(f"Erro ao acessar {pageUrl}: {e}")

# Bloco para capturar o Ctrl+C (KeyboardInterrupt) de forma limpa
try:
    print("Iniciando o Crawler... Pressione Ctrl+C para parar.")
    # Limpa o arquivo antigo ou cria um novo cabeçalho (opcional)
    with open('urls_salvas.txt', 'w', encoding='utf-8') as f:
        f.write("--- Lista de URLs Coletados ---\n")
        
    getLinks("") # Começa pela Home da Wikipedia
except KeyboardInterrupt:
    print("\n\nPrograma interrompido pelo usuário (Ctrl+C).")
    print(f"Total de URLs salvos: {len(pages)}")
    print("Os dados estão seguros em 'urls_salvas.txt'.")