from bs4 import BeautifulSoup
import requests

keyword = "Integrity"

def url_scrapper(keyword):
    url = f"https://en.wikipedia.org/wiki/{keyword}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def article_scrapper(soup):
    p_tags = soup.find_all('p')
    article_text = ""
    for p in p_tags:
        article_text+=p.text
    return article_text



