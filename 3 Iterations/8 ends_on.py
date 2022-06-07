digit = int(input('What final digit do you want to check the numbers on: '))
number = 0
for i in range(1, 11):
    my_number = int(input('Enter a number: '))
    if my_number % 10 == digit:
        number += 1

if number == 1:
    print ('1 out of 10 numbers ends on', digit)
else:
    print(number, 'out of 10 numbers end on', digit)
