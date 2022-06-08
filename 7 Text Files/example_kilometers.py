with open('kilometers.txt') as file:
    # read first line to initialize smallest and largest
    line = file.readline().rstrip()
    smallest = largest = int(line)

    # read second line
    line = file.readline().rstrip()
    while line:
        number = int(line)
        if number > largest:
            largest = number
        else:
            if number < smallest:
                smallest = number
        line = file.readline().rstrip()

difference = largest - smallest
print('The difference between the largest and the smallest number =', largest, '-', smallest, '=', difference)
