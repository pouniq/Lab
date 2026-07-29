# when we have javascrips code 
# not static HTML files.

# playwright
# first we pip install playwright
# then we use `playwright install` to install browsers needed for
# our requests

# first playwright script

from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(channel="chrome")
#     page = browser.new_page()
#     page.goto("https://quotes.toscrape.com/")
    
#     content = page.content()
#     print(content[:500])
    
#     browser.close()
    
# playwright with beautifulsoup
# from playwright.sync_api import sync_playwright
# from bs4 import BeautifulSoup

# with sync_playwright() as p:
#     browser = p.chromium.launch(channel = "chrome")
#     page = browser.new_page()
    
#     page.goto("https://quotes.toscrape.com/")
#     html = page.content()
#     browser.close()
    
# soup = BeautifulSoup(html, "html.parser")
# qoutes = soup.find_all("span", class_ = "text")

# for qoute in qoutes:
#     print(qoute.text)


# playwright without beautifulsoup

# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(channel = 'chrome')
#     page = browser.new_page()
    
#     page.goto("https://quotes.toscrape.com/")
    
#     qoutes = page.locator(".text").all_text_contents()
#     for qoute in qoutes:
#         print(qoute)
    
#     browser.close()


# handling pages that need interaction
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    
    browser = p.chromium.launch(channel = 'chrome', headless = False)
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com/")
    
    # page.click("button.load-more")
    
    page.wait_for_selector(".text")
    
    qoutes = page.locator(".text").all_text_contents()
    print(qoutes)
    
    browser.close()