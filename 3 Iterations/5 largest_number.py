number = int(input('Enter a number: '))
if number == 0:
    print('No numbers entered')
else:
    largest = number
    smallest = number
    number = int(input('Enter a number: '))
    while number != 0:
        if number > largest:
            largest = number
        else:
            if number < smallest:
                smallest = number
        number = int(input('Enter a number: '))

    print('The difference between the largest number', largest, 'and the smallest', smallest,'=',largest-smallest)
