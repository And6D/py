
print("\nEnter range, for count\n")
start_num = int(input("start value :"))
end_num = int(input("and end value:"))
step = int(input("enter step:"))
print("count range is:\t", start_num, "-", end_num, "\tstep", step)

choise = int(input("\n1.count\n2.set again\n3.exit"))
calcualte=1
restart=2
exit =3
while choise == restart:
    start_num = int(input("\nstart value :"))
    end_num = int(input("and end value:"))
    step = int(input("enter step:"))
    print("count range is:\t", start_num, "-", end_num, "\tstep", step)
    choise = int(input("\n1.count\n2.set again\n3.exit"))
else:
    if choise ==calcualte:
        for i in range(start_num, end_num, step):
            i <= end_num
            print(i, end=" ")
            print()
    if choise==exit:
     print("enter to exit")



