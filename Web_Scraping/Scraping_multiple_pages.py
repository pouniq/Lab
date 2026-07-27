import requests
from bs4 import BeautifulSoup
import time

# for page_num in range(1, 6):
#     url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     books = soup.find_all("h3")
#     print(f"page {page_num}: found {len(books)} books.")
#     print(books.find('a'))
    
base_url = "https://books.toscrape.com/catalogue/"
url = "https://books.toscrape.com/catalogue/page-1.html"

all_titles = []
page_count = 0

while url:
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    # scrape the current page
    
    books = soup.find_all("h3")
    for book in books:
        title = book.find("a")['title']
        all_titles.append(title)
    page_count += 1
    time.sleep(1)
    
# check for the "next" link
    next_button = soup.find("li", class_ = "next")
    if next_button :
        next_href = next_button.find("a")["href"]
        url = base_url + next_href
    else:
        url = None
print(f"Scraped {page_count} pages, found {len(all_titles)} Total books.")       