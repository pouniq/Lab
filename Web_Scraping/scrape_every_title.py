import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"

response = requests.get(URL)
# print(response.status_code)
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")


# with find_all method

# books = soup.find_all("article", class_ = "product_pod")
# print(f"Found {len(books)} books, ")
# print(books)
# for book in books:
#     title = book.find("h3").find("a")["title"]
#     price = book.find("p", class_ = "price_color").text
#     print(title, "," , price)


# CSS selectors
# it is most used
# titles = soup.select("article.product_pod h3 a")
# for title in titles:
#     print(title["title"])
    
# ratings = soup.select("article.product_pod p.star-rating")
# for rate in ratings:
#     star = rate["class"][1]
#     print(star)

books = soup.select("article.product_pod")
for book in books:
    title = book.h3.a["title"]
    rate = book.select_one("p.star-rating")["class"][1]
    print(title, "-", "have", rate, "stars")
