output_file = open('books2.txt', 'a', encoding='UTF-8')
with open('books.txt', encoding='UTF-8') as file:
    book = file.readline()
    while book:
        author = file.readline()
        output_file.write(author.rstrip()+";"+ book)
        book = file.readline()



