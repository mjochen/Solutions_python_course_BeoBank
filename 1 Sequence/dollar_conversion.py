dollar_exchange_rate = float(input('Enter the current exchange dollar rate (€-> $): '))
amount_euro = float(input('Enter your amount in euro: '))

amount_dollar = amount_euro * dollar_exchange_rate
print(amount_euro, '€ = ', amount_dollar, '$')

