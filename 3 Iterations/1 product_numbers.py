# XKCD_start_H3_product_numbers.py
product = 1
counter = 0
number = int(input('Enter a number, stop by entering a zero: '))

while number != 0:
    product *= number
    counter += 1
    number = int(input('Enter a number, stop by entering a zero: '))

print('The product is', product)
# print('The product of the', counter, 'numbers is', product)