text = input('What do you eat for lunch: ')
first = text.find("sandwich")

if first != -1:
    part_text = text[first + 8:]
    second = part_text.find("sandwich")
    if second != -1:
        print('You have', part_text [0: second],'between your sandwich.')