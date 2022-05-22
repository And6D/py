# by user request count numbers
# input set start and finish numbers by user
# set step of count by user
#  в цикл?
print ("Enter range, for count " )
start_num =int(input("It starts at : "))
end_num =int(input("and end at: "))
step =int(input("Enter step: "))
print("для подсчета доступен диапазон: ", start_num, "до", end_num, "с шагом ", step )
# диалог для запуска циклf или возрата к вводу знасений и шага

agreement =input ("\nFor start tape '1',\n for restart tape '2,\n or '3' for exit: ")

for i in range(start_num, end_num, step):
 print(i, end=" ")



#agree =1
#disagree = 2
#exit= 3







