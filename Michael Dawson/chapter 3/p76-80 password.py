# Пароль
#Демонстрирует использование конструкции if print('Дoбpo пожаловать к нам в ООО "Системы безопасности ". ')
print('-- Безопасность - наше второе имя\n')
password = input("Введите пароль : ")
if password == "secret":
    print( "Дocтyп открыт")
else: print("Не угадал, access denied ")
input("\nHaжмитe Enter . чтобы выйти ")
