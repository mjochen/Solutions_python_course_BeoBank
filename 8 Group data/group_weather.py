print('Average temperatures:')
with open('weather_2018 10.csv') as file:
    # read first line with field names
    line = file.readline()

    # read second line to initialize highest_temp
    line = file.readline()
    date_info = line.split(';')
    while line:
        dateind = date_info[0].split(' ')[0]
        date_number = 0
        date_total = 0
        while line and date_info[0].split(' ')[0] == dateind:
            date_number += 1
            date_total += float(date_info[1])
            line = file.readline().rstrip()
            date_info = line.split(';')

        average = date_total / date_number
        print(dateind + '\tnumber of measurements = ' + str(date_number) + '\taverage =', '{:.4}'.format(average))

print('>' * 60)
