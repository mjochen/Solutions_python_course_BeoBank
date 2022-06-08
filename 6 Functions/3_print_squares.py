def print_square(sign, number):
    line = number * sign
    for i in range(number):
        print(line)


# def print_square(character, number):
#      for i in range(0, number):
#          print(number * character)

sign = input('Which character must be used to form the lines (enter = stop): ')

while sign != '':
    number = int(input('Number of characters per line = number of lines = '))
    print_square(sign, number)
    sign = input('Which character must be used to form the lines (enter = stop): ')
