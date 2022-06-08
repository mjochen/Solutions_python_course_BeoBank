text = input('Enter a text: ')
number_of_triples = 0
i = 0
while i < len(text) - 2:
    if text[i] == text[i+1] and text[i] == text[i+2]:
        number_of_triples += 1
    i += 1

if number_of_triples == 0:
    print ('There are no triples in this text')
else:
    if number_of_triples == 1:
        print ('There is 1 triple in this text')
    else:
        print('There are', number_of_triples, 'triples in this text')