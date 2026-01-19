############################### Lógica a ser seguida: ###############################
# 1. Abrir a página/sistema da empresa
# 2. Fazer login
# 3. Abrir a base de dados
# 4. Cadastrar produtos
# 5. Repetir o passo 4 até finalizar o processo necessário
#####################################################################################

###################################### Código #######################################
# IMPORTS:
import pyautogui
import time
import pandas as pd

# VARIÁVEIS:
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
email = 'python@gmail.com'
senha = 'umasenhaqualquer'

# 1. Abrir a página/sistema da empresa
pyautogui.press('win')
time.sleep(2)

pyautogui.write('Chrome')
time.sleep(2)
pyautogui.press('Enter')
time.sleep(5)

pyautogui.write(link)
pyautogui.press('Enter')
time.sleep(4)

# 2. Fazer login
pyautogui.click(x=618, y=562)
time.sleep(2)
pyautogui.write(email)
time.sleep(2)
pyautogui.press('tab')
time.sleep(1)
pyautogui.write(senha)
time.sleep(2)
pyautogui.press('tab')
pyautogui.press('Enter')
time.sleep(4)

# 3. Abrir base de dados
data = pd.read_csv('produtos.csv')


# 4 e 5. Cadastrar produtos e manter até todos serem cadastrados
for linha in data.index:

    # Código do produto
    pyautogui.click(x=608, y=394)
    codigo = str(data.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press('tab')
    time.sleep(2)

    # Marca do produto
    marca = str(data.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press('tab')
    time.sleep(2)

    # Tipo do produto
    tipo = str(data.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    time.sleep(2)

    # Categoria do produto
    categoria = str(data.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    time.sleep(2)


    # Preço do produto
    preco_unitario = str(data.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')
    time.sleep(2)


    # Custo do produto
    custo = str(data.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press('tab')
    time.sleep(2)


    # Obs do produto (Se tiver!)
    obs = str(data.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press('tab')
    time.sleep(2)
    
    # Enviar o produto
    pyautogui.press('Enter')
    time.sleep(1)


    # Scroll pra subir a página
    pyautogui.scroll(5000)
    time.sleep(1)
    
print("Produtos cadastrados!")