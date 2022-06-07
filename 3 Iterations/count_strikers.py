number_strikers = 0
counting = True

print('Press Enter for each new striker you see.')
print('If you want to pass a group, enter the number of strikers')
print('If you want to stop, typ S and press Enter')

while counting:
    count = input('>> ')
    while count != 'S':
        if count == '':
            number_strikers += 1
        else:
            number = int(count)
            number_strikers += number
        count = input('>> ')

    answer = input('Do you really want to stop Y/N? ')
    if answer in ('N', 'n'):
        counting = True
    else:
        counting = False

print('Total number of strikers =', number_strikers)
