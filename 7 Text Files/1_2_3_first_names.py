# Oefening 1
# with open('first_names.txt') as file:
#     name = file.readline()
#     # number = 0
#     total_number = 0
#     while name:
#         total_number += 1
#         print(name.rstrip())
#         name = file.readline()
#     # while name:
#     #     total_number += 1
#     #     if 'z' in name or 'Z' in name:
#     #         number += 1
#     #         print(name.rstrip())
#     #     name = file.readline()
#
# print('There are', total_number, 'first names in the file.')
# # print(number, 'of which contain a letter z.')

# Oefening 2
# with open('first_names.txt') as file:
#     first_names = file.readlines()
#
#     for name in first_names[::-1]:
#         print(name, end='')
#
# with open('first_names.txt') as file:
#     first_names = file.readlines()
#     first_names.reverse()
#     for name in first_names:
#         print(name, end='')

# Oefening 3
with open('first_names.txt') as file:
    first_names = file.readlines()
    counter = 0
    while counter < len(first_names):
        print(first_names[counter].rstrip().ljust(13), end='')
        counter += 1
        if counter % 10 == 0:
            print()
