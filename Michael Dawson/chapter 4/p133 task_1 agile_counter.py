# by user request count numbers
# input set start and finish numbers by user
# set step of count by user
#  в цикл?
print ("Enter range, for count " )
start_num =int(input("It starts at : "))
end_num =int(input("and end at: "))
step =int(input("Enter step: "))
print("для подсчета доступен диапазон: ", start_num, "до", end_num, "с шагом ", step )

range_num=(start_num, end_num)
print(len(range_num), "count range")
# диалог для запуска цикл или возрата к вводу значений и шага
# расчет идет когда start_num >= end_num

agreement =input ("\n1. tape '1' to count:"
                  "\n2. tape '2' for re-enter value:"
                  "\n3. tape '3' for exit :")

for i in range(start_num, end_num, step):
 print(i, end=" ")



#agree =1
#disagree = 2
#exit= 3







