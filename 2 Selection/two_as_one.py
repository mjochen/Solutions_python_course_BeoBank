a = int(input('Number 1: '))
b = int(input('Number 2: '))
c = int(input('Number 3: '))

if a+b == c or a+c == b or b+c == a:
    print('This works')
else:
    print("This won't work")