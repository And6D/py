def _main(number, operator=None):
    if operator is None:
        return number
    return operator(number)

def zero(operator=None): return _main(0, operator)
def one(operator=None): return _main(1, operator)
def two(operator=None): return _main(2, operator)
def three(operator=None): return _main(3, operator)
def four(operator=None): return _main(4, operator)
def five(operator=None): return _main(5, operator)
def six(operator=None): return _main(6, operator)
def seven(operator=None): return _main(7, operator)
def eight(operator=None): return _main(8, operator)
def nine(operator=None): return _main(9, operator)

def plus(second_operand):
    return lambda first_operand: first_operand + second_operand
def minus(second_operand):
    return lambda first_operand: first_operand - second_operand
def times(second_operand):
    return lambda first_operand: first_operand * second_operand
def divided_by(second_operand):
    return lambda first_operand: int(first_operand / second_operand)

print(seven(times(five()))) # must return 35

print(four(plus(nine()))) # must return 13

print(eight(minus(three()))) # must return 5

print(six(divided_by(two()))) # must return 3




