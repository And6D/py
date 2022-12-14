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