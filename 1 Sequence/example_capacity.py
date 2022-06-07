trains_per_hour = int(input("Enter the number of trains per hour: "))
places_per_train = int(input("Enter the number of places per hour: "))
# trains_per_hour = 2
# places_per_train = 28
minutes_per_ride = 2
minutes_boarding_time = 0.5
capacity_per_hour = trains_per_hour * places_per_train * 60 / (minutes_boarding_time + minutes_per_ride)
print('The maximum capacity of the Python per hour is', int(capacity_per_hour), 'persons')
