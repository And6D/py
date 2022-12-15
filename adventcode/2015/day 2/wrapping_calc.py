def take_source():
    """take data from source"""
    with open("input_d2.txt", "r") as file:
        data = file.read()
    return data


def spliter():
    """take data and split on pacs"""
    pac = take_source().splitlines()
    return pac

"""Calculate how many bixes of presents elves have"""
boxes = len(spliter())

"""Part 1"""
order_paper = 0

"""Part 2"""
order_ribbon = 0

for words in spliter():
    split = words.split('x')

    l = int(split[0])
    w = int(split[1])
    h = int(split[2])

    order_paper += 2 * (l * w + w * h + l * h) + min(l * w, w * h, h * l)
    order_ribbon += l * w * h + min(2 * (l + w), 2 * (w + h), 2 * (l + h))

print(f"Elves should order wrapping paper to fit {boxes} presents\n")
print(f"Elves should order {order_paper} square feet of wrapping paper")
print(f"Elves should order {order_ribbon} feet of ribbon")
