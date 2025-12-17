# 🕸️ Automação e Web Scraping com Python

Este repositório serve como um guia de estudos e prática de **Web Scraping** (raspagem de dados) utilizando a linguagem **Python** e a biblioteca **BeautifulSoup 4**. 

O objetivo é documentar a evolução do aprendizado, desde a extração simples de textos até a limpeza de dados e lógica de programação aplicada à coleta de informações.

## 📖 O que é o BeautifulSoup?

O **BeautifulSoup** (frequentemente abreviado como `bs4`) é uma biblioteca Python poderosa usada para extrair dados de arquivos HTML e XML. Ele funciona como um "parser" (analisador), transformando o código bagunçado de uma página web em uma árvore de objetos Python estruturada, permitindo que você navegue e busque informações facilmente.

Geralmente, ele é utilizado em conjunto com a biblioteca `requests`, que é responsável por fazer a conexão e baixar o conteúdo da página para que o BeautifulSoup possa ler.

---

## 🛠️ Cheat Sheet: Métodos Mais Usados

Abaixo está um resumo dos comandos essenciais para quem está começando:

| Método | O que ele faz? | Exemplo de uso |
| :--- | :--- | :--- |
| **`soup.find()`** | Encontra o **primeiro** elemento que corresponde ao critério. | `soup.find('div', class_='quote')` |
| **`soup.find_all()`** | Retorna uma **lista** com **todos** os elementos encontrados. | `soup.find_all('a')` |
| **`.get_text()`** | Extrai apenas o texto visível de uma tag (remove o HTML). | `elemento.get_text(strip=True)` |
| **`['atributo']`** | Acessa atributos da tag (como links, imagens, IDs). | `tag_link['href']` ou `imagem['src']` |
| **`.select()`** | Busca elementos usando seletores CSS (igual ao front-end). | `soup.select('div.container > p')` |

---

## 🚀 Como Usar

### 1. Instalação das Dependências
Para rodar os scripts deste repositório, você precisará instalar as bibliotecas principais:

#bash
pip install beautifulsoup4 requests


2. Exemplo "Hello World"
Um script básico para testar se tudo está funcionando:

Python

import requests
from bs4 import BeautifulSoup

# 1. Faz a requisição ao site
response = requests.get('[http://quotes.toscrape.com](http://quotes.toscrape.com)')

# 2. Cria o objeto Soup (o analisador)
soup = BeautifulSoup(response.content, 'html.parser')

# 3. Extrai o título da página
print(soup.title.string)

📂 Estrutura de Exercícios
Os códigos práticos estão organizados dentro da pasta exercises/ e foram divididos por níveis de complexidade para facilitar o aprendizado gradual:

🟢 Nível Fácil: Focado em entender a estrutura HTML e usar o .find() para extrair textos simples e títulos.

🟡 Nível Médio: Introdução ao .find_all() e loops (for) para extrair listas de dados (ex: listas de autores, categorias).

🔴 Nível Difícil: Cenários reais que exigem tratamento de dados. Inclui lógica de programação (Python if/else) para filtrar resultados e limpeza de strings (ex: converter preços com símbolos de moeda em números float).

<p align="center"> <sub>Desenvolvido para fins educacionais em Ciência da Computação.</sub> </p>
