# dia 13
def triangle_type(a, b, c):
    if a == b and b == c:
        return 'equilateral triangle'
    elif c ** 2 == a ** 2 + b ** 2:
        return 'right triangle'
    else:
        return 'other triangle'


print('Give the length of the three sides, from small to large')
a = float(input('Enter the length of the first side: '))
b = float(input('Enter the length of the second side: '))
c = float(input('Enter the length of the third side: '))

print(triangle_type(a,b,c))
# circumference = a + b + c
# print('The perimeter of this', triangle_type(a, b, c), 'triangle is', perimeter)


