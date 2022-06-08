text = input ('Enter the text to be encrypted: ')

rotation = ''
while not rotation.isdigit():
    rotation = input('Enter the number of characters you want to rotate with: ')

rotation = int(rotation) % 26
encrypted_text = ''
for i in range(0, len(text)):
    if text[i].isupper():
        border = ord('Z')
    else:
        border = ord('z')
    if ord(text[i])+rotation <= border:
        encrypted_text += chr(ord(text[i])+rotation)
    else:
        encrypted_text += chr(ord(text[i]) - 26 + rotation)
print(encrypted_text)