# Кости
# Демонстрирует генерацию случайных чисел
import random
# создаем случайные числа из диапазона 1 - 6
diel = random.randint(1, 6)
die2 = random.randrange(6) + 1
total = diel + die2
print("Пpи вашем броске выпало", diel, "и", die2, "очков. в сумме", total)
input("\n\nHaжмитe 'Enter ', чтобы выйти ")
