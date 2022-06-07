for counter in range(1, 5):
    print('Information for member', counter)
    name = input('Name: ')
    age = int(input('Age: '))
    years = int(input('Member for how many years: '))
    if age > 18:
        fee = 95
    elif age > 12:
        fee = 50
    else:
        fee = 20
    if years >= 5:
        fee *= 0.9
    print('Member fee for', name, '=', fee, '\n')
