number = int(input('Enter a number: '))
if number <= 0:
    print('Negative numbers will not be tested')
else:
    digit = int(input('What final digit do you want to test with: '))
    if number % 10 == digit:
        print(number, 'ends with', digit)
    else:
        print(number, 'does not end with', digit)