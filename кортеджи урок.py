tuple = ("First",)
print(type(tuple))

dict = {"яблоко": "красное", "груша": "зеленая", "лимон": ":желтый"}
for k in dict.keys():
    print(k)
for l in dict.values():
    print(l)
for z in dict.items():
    print(z)

#  print key for  value "груша"
print(dict["груша"])

# change key
dict["яблоко"] = "желтый"

print(dict["яблоко"])

# del in dictionary
del(dict["лимон"])
print(dict)


