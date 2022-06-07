# number = int(input('Enter a number: '))
#
# for counter in range(1, 11):
#     print(counter, 'x', number, '=', counter * number)
#
# for counter in range(1, 11):
#     print(counter, counter ** 2, counter ** 3, sep='\t')
# #
# count_numbers = int(input('How many numbers do you want to enter: '))
#
# smallest = int(input('First number: '))
# for i in range(count_numbers - 1):
#     number = int(input('Next number: '))
#     if number < smallest:
#         smallest = number
#
# print('The smallest number =', smallest)
#
# for x in range(3, 5):
#     for y in range(10, 50, 15):
#         print(x, y)
# for x in range(3, 5):
#     print(x)
#     for y in range(10, 50, 15):
#         print(y)
# for x in range(3, 5):
#     for y in range(10, 50, 15):
#         print(x, y)
# for x in range(3, 5):
#     for y in range(x, 50, 15):
#         print(x, y)
# for x in range(3, 5):
#     for y in range(10, 50, x):
#         print(x, y)

for i in range(1, 8):
    print(i, '\t', end='')  # print i and don't go to a new line!
    for j in range(1, i + 1):
        print(str(j), end='')
    print()
