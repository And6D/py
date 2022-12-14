def take_source():
    """taking data from source"""
    with open("input_d1.txt", "r") as file:
        data = file.read()
    return data


def lift_floor():
    floor = 0
    for element in take_source():
        if element == "(":
            floor += 1
        elif element == ")":
            floor -= 1
    return floor


print(f"\nCurrent floor number of the house is: {lift_floor()}")

"""-part 2-"""


def position(input_string, floor_query):
    if floor_query == 0:
        return 0

    floor = 0

    for idx, char in enumerate(input_string, start=1):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == floor_query:
            return idx


print(position(take_source(), -1))
