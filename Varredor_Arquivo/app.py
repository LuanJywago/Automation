from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
from time import sleep

# Entrar no site ()
driver = webdriver.Chrome()
driver.get('https://devaprender-play.netlify.app/')
sleep(8)

# Ver qual o nome do produto () - XPATH: //tag[@atributo= 'valor]
#//h3[@class='text-lg font-semibold text-gray-900 group-hover:text-indigo-600']
produtos = driver.find_elements(By.XPATH,"//h3[@class='text-lg font-semibold text-gray-900 group-hover:text-indigo-600']")

# Anotar o preço do produto ()
# XPATH DO PREÇO DO PRODUTO = //p[@class="text-2xl font-bold text-indigo-600"]
preco = driver.find_elements(By.XPATH,"//p[@class='text-2xl font-bold text-indigo-600']")

# Repetir isso para todos os produtos da página
# Guardar em arquivo de texto .csv
for produto, preco in zip(produtos,preco):
    with open('preços.csv','a',encoding='utf-8') as arquivo:
        arquivo.write(f'{produto.text}, {preco.text}{os.linesep}')