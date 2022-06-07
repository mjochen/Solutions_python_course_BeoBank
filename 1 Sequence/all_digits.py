number = int(input('Enter a three-digit number: '))

print('Half =', number/2)
print('Double =', number*2)
print('Third power =', number**3)
print('Tenfold =', number*10)
print('The digits are:')
first = number//100
second = (number % 100)//10
third = (number % 100) % 10
print(first)
print(second)
print(third )
