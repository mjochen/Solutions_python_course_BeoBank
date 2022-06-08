#dia 20
#1 Open file
file = open('agenda.txt', 'w')
# #2 Write data to file
# file.write('25/11;Bob Potters; 08:30')
# file.write('30/11;René François; 12:30')
# file.write('02/12;Chris Benz; 10:15')
# #3 Close file
# file.close()
#

#dia 22
#1 Open file
# file = open('agenda.txt','w')
# #2 Write data to file
# file.write('25/11;Bob Potters; 08:30\n')
# file.write('30/11;René François; 12:30\n')
# file.write('02/12;Chris Benz; 10:15\n')
# #3 Close file
# file.close()
#
# dia 24
#1 Open file
# file = open('agenda.txt','w', encoding='UTF-8')
# #2 Write data to file
# file.write('25/11;Bob Potters; 08:30\n')
# file.write('30/11;René François; 12:30\n')
# file.write('02/12;Chris Benz; 10:15\n')
# #3 Close file
# file.close()
#
# dia 25

# with open('agenda.txt','w', encoding='UTF-8') as file:
# # Write data to file
#     file.write('25/11;Bob Potters; 08:30\n')
#     file.write('30/11;René François; 12:30\n')
#     file.write('02/12;Chris Benz; 10:15\n')

#
#dia 26
# appointments=[]
# appointments.append('25/11;Bob Potters; 08:30\n')
# appointments.append('30/11;René François; 12:30\n')
# appointments.append('02/12;Chris Benz; 10:15\n')
#
# with open('agenda.txt','w', encoding='UTF-8') as file:
#     # Write data to file with writelines()
#     file.writelines(appointments)

#
# dia 27
# with open('agenda.txt','a', encoding='UTF-8') as file:
#  #2 add data from list to file with writelines()
#      appointments=[]
#      appointments.append('13/12;Anne Davis,08:30\n')
#      appointments.append('13/12;Connor Leeds;10:00\n')
#      file.writelines(appointments)
#
# dia 29
from os.path import exists
# check if file exists and if not create the file
# if exists('agenda.txt'):
#     print('The file already exists and cannot be overwritten')
# else:
#     with open('agenda.txt', 'w', encoding='UTF-8') as file:
#         file.write('14/12;Mia Thans,12:30\n')
#         file.write('15/12;Lian Sanchez;10:00\n')

# dia 30
from os.path import exists
# check if file exists and if not create the file
if exists('agenda.txt'):
    file = open('agenda.txt', 'a', encoding='UTF-8')
else:
    file = open('agenda.txt', 'w', encoding='UTF-8')

file.write('14/12;Mia Thans;12:30\n')
file.write('15/12;Lian Sanchez;10:00\n')
file.close()
