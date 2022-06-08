def maximum(number1, number2):
    if number1 > number2:
        return number1
    return number2


assert maximum(15, 6) == 15
assert maximum(-3, 6) == 6
assert maximum(4, 4) == 4
