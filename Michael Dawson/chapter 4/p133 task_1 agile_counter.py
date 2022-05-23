
agreement_before =int(input("\n1. tape '1' to count"
                            "\n2. tape '2' for exit"))

while agreement_before == 1:

    print("Enter range, for count\n")
    start_num = int(input("start value :"))
    end_num = int(input("and end value:"))
    step = int(input("enter step:"))
    print("count range is:\t", start_num, "-", end_num, "\tstep", step)
    for i in range(start_num, end_num, step):
     print(i, end=" ")
    break

if agreement_before == 2:
    input("\n\nPress Enter to exit.")








