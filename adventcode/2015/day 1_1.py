print("Agenda:\n\t\t\t\t--- Day 1: Not Quite Lisp ---"
      "\nSanta is trying to deliver presents in a large apartment building,"
      "\nbut he can't find the right floor - the directions he got are a little"
      "\nconfusing. He starts on the ground floor (floor 0) and then follows the"
      "\ninstructions one character at a time."
      "\n\nAn opening parenthesis, (, means he should go up one floor, and a closing"
      "\nparenthesis, ), means he should go down one floor."
      "\n\nThe apartment building is very tall, and the basement is very deep; he "
      "\nwill never find the top or bottom floors."
      "\n\nTo what floor do the instructions take Santa?")

def take_source():
    """adding source"""
    with open("input source/input_d1.txt", "r") as file:
        data = file.read()
    return data

def data_slicer():
    """slice data from source to "70" simbols on each line"""
    element = len(take_source())
    return element

print(f"\nData loaded: {data_slicer()} simbols")
# to do test
# (()) and ()() both result in floor 0.
# ((( and (()(()( both result in floor 3.
# ))((((( also results in floor 3.
# ()) and ))( both result in floor -1 (the first basement level).
# ))) and )())()) both result in floor -3.

def lift_floor():
    floor = 0
    for element in take_source():
        if element == "(":
            floor += 1
        elif element == ")":
            floor -= 1
    return floor


print(f"\nCurrent floor number of the house is: {lift_floor()}")

# to do
# test in py
