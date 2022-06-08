# dia 7
# file = open('schedule.txt')
# print(file.read())
# file.close()
#
# # other method
# with open('schedule.txt') as file:
#      print(file.read())
#
# Read line by line dia 12
# 1: open file
# with open('schedule.txt') as file:
#     # 2: read line by line
#     line = file.readline()
#     while line:
#         if line != '\n':
#             print(line.rstrip())
#         line = file.readline()
#
# dia 13
# 1: open file
# with open('schedule.txt') as file:
#     # 2: read line by line
#     line = file.readline()
#     while line:
#         if line != '\n':
#             record = line.split(';')
#             print(record[1])
#         line = file.readline()










# dia 16
# Read all the rules at once in a list
# with open('schedule.txt') as file:
#     # read all lines and place them in a list of strings
#     lines = file.readlines()
#     for line in lines:
#         if line != '\n':
#             print(line, end='')

# Reading fields from records
# with open('schedule.txt') as file:
#     all_lines = file.readlines()
#     for line in all_lines:
#         if line != '\n':
#             # line is split into record of fields
#             record = line.split(';')
#             print(record[0], record[2].rstrip(), record[1], sep='\t')
