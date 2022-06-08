def code(mirror):
    list = ['yellow', 'green', 'blue', 'purple']
    new_list = []
    for color in list:
        new_color = ''
        for letter in color:
            ascii_code = ord(mirror) + (ord(mirror) - ord(letter))
            while ascii_code > ord('z'):
                ascii_code = ascii_code - 26
            while ascii_code < ord('a'):
                ascii_code = ascii_code + 26
            new_color += chr(ascii_code)
        new_list.append(new_color)
    print('original:', list)
    print('encoded:', new_list)

mirror = input('Enter a letter to mirror around: ').lower()
code(mirror)
