#
with open("input_d1.txt","r" ) as file:
    data =file.read()

print(data)
level =0
for element in data:
    if element == "(":
        level += 1
    elif element == ")":
        level -= 1


print(level)

# to do
# 1 def
# test in py
