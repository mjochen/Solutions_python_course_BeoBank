year = int(input("year: "))

if year % 4000 == 0 and year > 1582:
    print('no leap year')
else:
    if year % 400 == 0 and year > 1582:
        print('leap year')
    else:
        if year % 100 == 0 and year > 1582:
            print('no leap year')
        else:
            if year % 4 == 0:
                print('leap year')
            else:
                print('no leap year')


