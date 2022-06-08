from os.path import exists


def read_month():
    month_number = int(input('Choose a month: '))
    while month_number not in range(1, 13):
        month_number = int(input('Choose a month: '))

    if month_number < 10:
        return '0' + str(month_number)
    else:
        return str(month_number)


filename = 'weather_2018 ' + read_month() + '.csv'
if not exists(filename):
    print('No data available for this month!')
else:
    with open(filename) as file:
        # Read first line with field names
        line = file.readline()

        # read second line to initialize highest_temp
        line = file.readline()
        date_info = line.split(';')
        start_date = date_info[0]
        info_date_highest = date_info
        highest_temp = float(date_info[1])

        # read second line
        line = file.readline()
        while line:
            date_info = line.split(';')
            if float(date_info[1]) > highest_temp:
                highest_temp = float(date_info[1])
                info_date_highest = date_info
            end_date = date_info[0]  # at the end we need to know the last date
            line = file.readline()

    print('\nPeriod: ', start_date, '-', end_date)
    print('-' * len('Period'))
    print('The highest temperature in this period =', highest_temp, '°C')
    date_part = info_date_highest[0].split(' ')
    print('This temperature was measured at ' + date_part[1] + 'h on ' + date_part[0])
