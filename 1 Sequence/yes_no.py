number_yes = int(input('How many people voted YES: '))
number_no = int(input('How many people voted NO: '))
number_blank = int(input('Number of blank votes: '))

total_votes = number_yes + number_no + number_blank

percentage_yes = number_yes / total_votes * 100
percentage_no = number_no / total_votes * 100
percentage_blank = number_blank / total_votes * 100

print('YES: ' + str(percentage_yes) + '%')
print('NO: ' + str(percentage_no) + '%')
print('Blank: ' + str(percentage_blank) + '%')
