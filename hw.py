import requests

r = requests.get('https://www.bookvoed.ru/author?id=153717')
print(r, "статус сервера")
print(r.headers, "заголовок")
print(r.text, "текст")
