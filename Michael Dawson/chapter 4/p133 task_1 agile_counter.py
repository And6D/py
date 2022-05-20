# by user request count numbers
# input set start and finish numbers by user
# set step of count by user
#  в цикл?
print ("Для начала рассчёта введите диапазон" )
start_num =int(input("Введите первое число диапазона: "))
end_num =int(input("Для задания диапазона ввведите конечное число: "))
step =int(input("Задайте значение шага подсчёта: "))
print("для подсчета доступен диапазон: ", start_num, "до", end_num, "с шагом ", step )
# диалог для запуска цикал или возрата к вводу знасений и шага
agreement = 1
disagreement = 2
restart = 3






for i in range(start_num, end_num, step):
 print(i, end=" ")