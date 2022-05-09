import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://www.bookvoed.ru/author?id=153717'
response = requests.get(url) # url можно напрямую записать значение, без присвоения
soup = BeautifulSoup(response.text, 'lxml')

items = soup.find('div', class_='GT')

spisok = []
for eachPart in items:
    spisok.append(eachPart.get_text(strip=True))
spisok = list(filter(None, spisok))

print(spisok)