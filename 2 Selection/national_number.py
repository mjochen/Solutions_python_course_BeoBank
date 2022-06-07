name = input ('Enter your name: ')
nnumber_part1 = int(input('Enter the first 9 digits of your national number : '))
nnumber_part2 = int(input('Enter the last 2 digits of your national number : '))

remainder = 97 - nnumber_part1 % 97
if nnumber_part2 != remainder:
    print('Hello ' + name + ', the national number you gave is not correct')
else:
    date = nnumber_part1 // 1000
    day = date % 100
    year = date // 10000
    month = date % 10000 // 100
    dummy = nnumber_part1 % 1000
    if dummy % 2 == 0:
        gender = 'female'
    else:
        gender = 'male'
    print('Hello ' + name + ', your gender is '+gender)
    print('You were born on ' + str(day) + '/' + str(month) + '/' + str(year))

