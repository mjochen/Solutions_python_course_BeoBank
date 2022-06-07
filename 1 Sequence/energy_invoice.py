consumption_day = int(input('Power consumption during the day (kilowatt per hour): '))
consumption_night = int(input ("Power consumption at night (kilowatt per hour): "))
fixed_amount = 83.6
price_day = 0.068
price_night = 0.035
total_day = consumption_day * price_day
total_night = consumption_night * price_night
total_excl = total_day + total_night + fixed_amount
total_incl = total_excl * 1.21

print('Invoice')
print('*******')
print('Fixed costs: €', fixed_amount)
print('Daily consumption: €', total_day)
print('Night consumption: €', total_night)
print('Total excluding VAT: €', total_excl)
print('Total including VAT: €', total_incl)
