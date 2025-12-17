from bs4 import BeautifulSoup
import requests

url ="https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

cards = soup.find_all("div", class_="quote")
for card in cards:
    text = card.find("span", class_="text").get_text()
    tags_elements = card.find_all("a", class_="tag")
    
    tags_text = [tag.get_text() for tag in tags_elements]
        
    have_life = "life" in tags_text
    print(f"Quote: {text}")
    print(f"tem a tag life?{have_life}\n")