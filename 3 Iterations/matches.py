import random
winner_known = False
number_pile1 = random.randint(20, 40)
number_pile2 = random.randint(20, 40)

while not winner_known:
    player_pile = int(input('From which tile do you take? '))
    player_number = int(input('How many matches (between 3 and 8) do you take? '))

    if player_pile == 1:
        number_pile1 -= player_number
    else:
        number_pile2 -= player_number

    # see if the player might have taken the last matches from a pile
    if number_pile1 <= 0 or number_pile2 <= 0:
        winner_known = True
        print('Congratulations, you win')  # Player wins
    else:
        computer_pile = random.randint(1, 2)
        computer_number = random.randint(3, 9)
        if computer_pile == 1:
            number_pile1 -= computer_number
        else:
            number_pile2 -= computer_number

        if number_pile1 <= 0 or number_pile2 <= 0:
            winner_known = True
            print('I win')  # computer wins
