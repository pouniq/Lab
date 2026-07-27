import requests
from bs4 import BeautifulSoup
# import csv
import json

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

books_data = []
books = soup.find_all("article", class_ = "product_pod")

for book in books:
    title = book.find('h3').find('a')['title']
    price = book.find("p", class_ = "price_color").text.replace('Â£','')
    
    books_data.append({
        "title": title,
        "price": price
    })
print(books_data[:2])


# Exporting to CSV
# with open("books_scraped.csv", 'w', newline="", encoding="utf-8") as file:
#     writer = csv.DictWriter(file, fieldnames=["title", "price"])
#     writer.writeheader()
#     writer.writerows(books_data)
# print("Save to books_scraped.csv")

# Exporting to JSON

with open("books.json", 'w', newline="", encoding="utf-8") as file:
    json.dump(books_data, file, indent=4, ensure_ascii=False)
print("saved a JSON file")

    
