# by user request count numbers
# input set start and finish numbers by user
# set step of count by user
#  в цикл?
print ("Enter range, for count\n" )

start_num =int(input("start value :"))
end_num =int(input("and end value:"))
step =int(input("enter step:"))

print("count range is:\t", start_num, "-", end_num, "\tstep", step)
print("\nReady or not?")

agreement_before =int(input("\n1. tape '1' to count"
                            "\n2. tape '2' for re-enter value"
                            "\n3. tape '3' for exit"
                            "\n"))
print("\nresult: \n")
for i in range(start_num, end_num, step):
  print( i, end=" ")

agreement_after =input("\nCount again  Y/N  ?\n\n")







