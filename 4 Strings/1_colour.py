colour = input('What is your favourite colour: ')

print(colour[0]+colour[2])
print("This colour consists of " + str(len(colour)) + " letters")
print()

for letter in colour:
    print(letter + ' = ' + str(ord(letter)))
print()

i= 0
while i < len(colour):
    if i % 2 == 0:
        print('#' + colour[i]+'#')
    else:
        print('**' + colour[i]+'**')
    i += 1