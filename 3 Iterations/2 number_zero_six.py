number = int(input('Enter a number: '))
number_zero = number_six = 0

while number > 0:
    rest = number % 10
    if rest == 0:
        number_zero += 1
    elif rest == 6:
        number_six += 1
    number = number // 10

print ('The number consists of', number_zero, 'zeros and', number_six, 'sixes')
