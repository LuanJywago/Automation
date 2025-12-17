from urllib.request import urlopen
from urllib.error import HTTPError 
from bs4 import BeautifulSoup 

# URL alvo para o scraping
url = "http://pythonscraping.com/pages/page1.html"

try:
    # 1. Tenta abrir a URL
    html = urlopen(url)
    
    # 2. Faz a leitura do HTML e cria o objeto BeautifulSoup
    bsObj = BeautifulSoup(html, "html.parser")
    
    # 3. Tenta encontrar a primeira tag <div> e imprimir seu conteúdo
    # Acessar diretamente .div é um atalho para find('div')
    print("Conteúdo da primeira tag <div>:")
    print(bsObj.div)
    
except HTTPError as e: # Correção 3: Captura o erro 'HTTPError'
    print(f"Ocorreu um Erro HTTP ao tentar acessar a URL: {e}")
except Exception as e:
    # Captura outros erros de rede/conexão
    print(f"Ocorreu um erro geral ao abrir a URL: {e}")

# --- Tratamento de Tags Não Existentes ---

if 'bsObj' in locals():
    # Verifica se o objeto bsObj foi criado com sucesso
    try:
        # Tenta acessar tags que provavelmente não existem
        # Correção 4: 'AttributeError' é a exceção correta para tags não encontradas
        # Correção 5: Remove a sintaxe 'like e', usando apenas 'as e'
        badContent = bsObj.nonExistingTag.otherTag
    except AttributeError as e: 
        print("\n--- Resultado do Teste de Erro ---")
        print("Tag Não Encontrada (AttributeError capturado).")
    else:
        # Este bloco só é executado se NÃO houver exceção (ou seja, se a tag for encontrada)
        # Correção 6: O valor para 'nada' em Python é 'None', não 'Null'
        print("\n--- Resultado do Teste de Erro ---")
        if badContent is None: 
            # Embora seja improvável chegar aqui, é um bom fallback
            print("Tag não encontrada, mas o código não lançou AttributeError.")
        else:
            print("Conteúdo inesperado encontrado:")
            print(badContent)