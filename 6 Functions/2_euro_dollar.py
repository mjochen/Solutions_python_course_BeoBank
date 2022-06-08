def convert(amount_in_euro, dollar_rate):
     return amount_in_euro * dollar_rate

rate = float(input('Current dollar rate (€ -> $): '))
amount = float(input('Your amount in Euro: '))
print('€',amount, '= $', convert(amount, rate))
