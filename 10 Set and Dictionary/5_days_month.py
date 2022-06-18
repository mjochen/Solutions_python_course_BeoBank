months = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30,
          "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}

choice = input('Month (press Enter if you want to see an overview of all months): ')

if choice == '':
    for month in months:
        print(month, '\t', months[month])
else:
    print(months.get(choice, 'This month does not exist.'))


