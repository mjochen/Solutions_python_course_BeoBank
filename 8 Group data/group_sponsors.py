total_number_forms = 0
with open('sponsors.txt') as file:
    list = file.readlines()
list.sort()

print ("Overview gifts")
print ("Number\tSponsor")

i = 0
fields = list[i].rstrip().split('*')

while i < len(list):
    # start new sponsor
    sponsorind = fields[0]
    total_per_sponsor = 0
    text_form = ''
    print(str(sponsorind)+"\t"+fields[1]+' ' + fields[2], end='')

    while i < len(list) and fields[0] == sponsorind:
        total_per_sponsor += int(fields[3])
        i += 1
        if i<len(list):
            fields = list[i].rstrip().split('*')

     # end of sponsor
    if total_per_sponsor >= 40:
        total_number_forms += 1
        text_form = "**"
    print('\t' + str(total_per_sponsor)+'\t'+text_form)

print('There are',total_number_forms, 'tax certificates to be sent.')
