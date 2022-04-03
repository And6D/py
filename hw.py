import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://www.bookvoed.ru/author?id=153717'
response = requests.get(url) # url можно напрямую записать значение, без присвоения
soup = BeautifulSoup(response.text, 'lxml')
print(soup.h2.text)

items = soup.find_all('div', class_='GT')
print(items)
