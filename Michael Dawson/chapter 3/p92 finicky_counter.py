# Привередливая считалка
#Демонстрирует работу команд break и continue
count = 0
while True:
 count += 1
#завершить цикл . если count принимает значение больше 10
 if count > 10:
  break
# пропустить 5
 if count == 5:
  continue
 print(count)
input("\n\nHaжмитe Enter. чтобы выйти.")