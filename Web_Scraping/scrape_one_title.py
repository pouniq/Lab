# check /robots.txt in every website
import requests
from bs4 import BeautifulSoup
import time


# urls = [
#     "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
#     "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html",
#     "https://books.toscrape.com/catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html"
# ]


# for url in urls:
#     response = requests.get(url)
#     print(url, response.status_code)
#     time.sleep(2)
    
# for small practice sites --> 2-3 seconds
# for real-world and/or commercial sites --> 3-5+ second

# code  meaning
# 200   success
# 404   Page Not found
# 403   Forbidden (You are Blocked)
# 500   Server Error (It is not your fault)

# every time check the status code before going further
url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(response.status_code)

if response.status_code == 200:
    print("SUCCESS, you can continue scraping")
else:
    print(f'Failed with code of {response.status_code}')
    
#  print(soup.title)
# print(soup.title.text)
# print(soup.h1)
# print(soup.find("a"))

# <h3></h3> -> <a></a> -> attribute: <title>

first_book = soup.find('h3')
first_link = first_book.find("a") 
title = first_link["title"]
print(title)



