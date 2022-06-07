a = int(input('First number: '))
b = int(input('Second number: '))

if a in range(30, 41) and b in range(30, 41) or a in (65, 72, 83, 90) and b in (65, 72, 83, 90):
    print('Both numbers are ok')
else:
    print('They are NOT ok')