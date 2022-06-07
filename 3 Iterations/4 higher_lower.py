# XKCD_start_H3_higher_ bearing.py
computer_number = 15
number_of_attempts = 0
number = int(input('Enter a positive number: '))

while number != computer_number:
    number_of_attempts += 1
    if number < computer_number:
        print('Higher!')
    else:
        print('Lower!')
    number = int(input('Enter a positive number: '))

print('You have guessed the number', computer_number, 'in', number_of_attempts + 1, 'turns.')
