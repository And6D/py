#text analazer
# len() и оператора in
message = input("Введите текст: ")
print ( "\nДлина введенного вами текста составляет:", len(message))
print( "\nСамая частая согласная , 'т', ")
if 'т' in message:
    print("встречается в вашем тексте.")
else:
    print("нe встречается в вашем тексте.")
input("\n\nHaжмитe Enter. чтобы выйти.")