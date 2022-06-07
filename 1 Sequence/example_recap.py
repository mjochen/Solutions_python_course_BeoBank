# read data
person = input("Who are we celebrating today: ")
number_of_guests = int(input("How many guests are invited: "))
price_present = float(input("How much did the gift cost: "))
# process data
price_per_guest = price_present/number_of_guests
# print information
print("\nYour contribution to the gift for "+person+" = "+str(price_per_guest))

