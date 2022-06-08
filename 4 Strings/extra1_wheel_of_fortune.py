winning = "keep looking up"
my_string = "#### ####### ##"
print("You have to guess this quote: " + my_string)

letter = input("Guess a letter or press / if you think you know the quote: ")

while letter != '/':
    help = ""
    for i in range(len(winning)):
        if winning[i] == letter:
            help += letter
        else:
            help += my_string[i]
    my_string = help
    print("You already have this result: " + my_string)
    letter = input("Guess another letter: ")

answer = input("OK. You think you know, just say it. ")
if answer == winning:
    print ("Yes, you win!")
else:
    print("Bad luck, wrong guess!")