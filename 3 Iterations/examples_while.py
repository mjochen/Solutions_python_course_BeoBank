# number = 5
# while number > 0:
#     number -= 1
#     print('We still have', number, 'pieces left')
# print('Too bad, no pieces left!')


# number = total = 0  #initialization is necessary!
#
# while total < 100:
#     number += 1
#     total += number
# print('Sum of 1 to', number, '=', total)

# total = count = 0
# #read the first number before the while
# number = int(input('Enter a number, stop by entering -1: '))
#
# while number != -1:
#     count += 1
#     total += number
#     #read the following numbers
#     number = int(input('Enter a number, stop by entering -1: '))
#
# print('Sum of the', count, 'numbers =', total)
#
#
#
counter = 1
number = int(input('Enter number ' + str(counter) + ': '))

while number > 0:
    print("x² = " + str(number ** 2), "x³ = " + str(number ** 3), sep='\t')
    counter += 1
    number = int(input('Enter number ' + str(counter) + ': '))
