

numbers = (4, 2, 3, 7, 5, 1, 3, 8)
print(numbers)

if 4 not in numbers:
    print('The number 4 does not appear in the Tuple')
else:
    # oplossing klopt niet: toont alles vanaf de eerste vier, niet vanaf de laatste
    # location = numbers.index(4)
    # new = numbers[location+1:]
    # print(new)
    while 4 in numbers:
        location = numbers.index(4)
        numbers = numbers[location+1:]
    print(numbers)

    
# andere oplossingen
# numbers = (4, 2, 3, 9, 1, 4)
# print(numbers)
# found = False
# index = len(numbers)
# while not found and index > 0:
#     index -= 1
#     if numbers[index] == 4:
#         found = True
#
# if not found:
#     print ('The number 4 does not appear in the Tuple')
# else:
#     partNumbers = numbers[index+1:len(numbers)]
#     print(partNumbers)


# numbers = (2, 3, 7, 5, 4, 1, 9, 8)
# print(numbers)
#
# if 4 not in numbers:
#      print('The number 4 does not appear in the Tuple')
# else:
#      found = False
#      index = len(numbers)
#      while not found and index > 0:
#          index -= 1
#          if numbers[index] == 4:
#              found = True
#      partNumbers = numbers[index + 1:len(numbers)]
#      print(partNumbers)
