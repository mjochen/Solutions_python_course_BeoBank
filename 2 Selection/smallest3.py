number1 = int(input('Number 1: '))
number2 = int(input('Number 2: '))
number3 = int(input('Number 3: '))
smallest = number1
if number2 < smallest:
    smallest = number2
if number3 < smallest:
    smallest = number3

print('The smallest number is', smallest)