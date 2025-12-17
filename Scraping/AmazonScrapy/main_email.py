from bs4 import BeautifulSoup
import requests
import smtplib
import os

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(practice_url)

soup = BeautifulSoup(response.content, "html.parser")
#print(soup.prettify()) #Here will show all site content in a structured way

price = soup.find(class_="a-offscreen").get_text()
#print(price) # Here will show the price of the product ($99.99) 

price_without_dollarsing = price.split("$")[1]
#print(price_without_dollarsing) # Here will show the price without the dollar sign (99.99)

price_as_float = float(price_without_dollarsing) #this line is not totally necessary, but it converts the string (text) to a float (number)
print(price_as_float) # Here will show the price as a float (99.99)


#########################This part is for sending email alerts#########################

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 100.00
EMAIL = "YOUR_EMAIL"
PASSWORD = "YOUR_PASSWORD"

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}\n{live_url}"
    
    print(f"Tentando login com:{EMAIL}")
    
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{live_url}".encode('utf-8')
        )
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")