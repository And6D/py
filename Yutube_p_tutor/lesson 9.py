#
l = open("numb.txt", 'r')
print(l.read())
l.close()

# использование метода close() не требует закрытия файла после сеанса доступа
with open ("numb.txt", 'r') as ly:
    print(ly.read())

try:
    a = int(input())
    b = int(input())
    print(a / b)
except ZeroDivisionError:
    print("На 0 деление запрещено ")

# посмотреть стандартные исключения
# https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
