digits = set()
letters = set()
text = input('Enter a text consisting only of letters and numbers: ')
for character in text:
    if character.isdigit():
        digits.add(character)
    else:
        letters.add(character)

print('The numbers:')
for digit in digits:
    print(digit)
print('The letters:')
for letter in letters:
    print(letter)
