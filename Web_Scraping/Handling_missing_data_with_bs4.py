import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

missing = soup.find('div', class_ = 'this-class-does-not-exist')
# print(missing.text)
# if missing is not None:
#     print(missing.text)
# else:
#     print("You have missed the mark")
    
# books = soup.find_all('article', class_ = "product_pod")
# for book in books:
#     title_tag = book.find('h3')
#     title = title_tag.find("a")["title"] if title_tag else "Unkown tag"
    
    
#     price_tag = book.find("p",class_ = "price_color")
#     price = price_tag.text if price_tag else "NA"
    
#     print(f"{title} - {price}")
    
# title = first_link["title"]
# title = first_link("title", "no title available")

price_tag = soup.find("article", class_ = "product_pod").find("p",class_ = "price_color") 
try :
    price_tag = price_tag.text.replace("Â£", '')
    price = float(price_tag)
    print(price)
except (AttributeError, ValueError):
    price = None
    print("could not find the price for this book")
    
    