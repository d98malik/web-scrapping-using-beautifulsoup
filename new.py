import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone"

content = requests.get(url)

soup = BeautifulSoup(content.text, 'lxml')