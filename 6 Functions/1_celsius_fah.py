def convert(degrees_celsius):
    return degrees_celsius * 9/5 + 32

degrees_celsius = input('Degrees Celsius: ')
print(str(degrees_celsius), 'degrees Celsius =', str(convert(float(degrees_celsius))), 'degrees Fahrenheit')