
agreement_before =int(input("\n1. tape '1' to count"
                            "\n2. tape '2' for exit\n"))

# включить проверку на пустой ввод
# обработка ошибок
while agreement_before == 1:

    print("Enter range, for count\n")
    start_num = int(input("start value :"))
    end_num = int(input("and end value:"))
    step = int(input("enter step:"))
    print("count range is:\t", start_num, "-", end_num, "\tstep", step)

    agreement_in = input("\nto continue and count type 'Y' or 'N' to re-enter Values: \n")


    for i in range(start_num, end_num, step):
       print(i, end=" ")
    break

    # Включить обработку на пустой ввод
    count = "Y"
    restart ="N"
# любой ввод возвращает в начала цикла
# нужен  вложеный цикл при Y
    while agreement_in == count:
      for i in range(start_num, end_num, step):
       print(i, end=" ")
    break
#  при N в начало цикла

if agreement_before == 2:
    input("\n\nPress Enter to exit.")








