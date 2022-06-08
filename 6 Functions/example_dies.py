# dia 21
import random


# def roll_dice(number_dice=1):
#     """
#     This function simulates rolling one or more dice.
#     :param number_dice: integer that indicates the number of dice used
#     :return: the number of pips rolled
#     """
#     total = 0
#     for counter in range(0, number_dice):
#         total += random.randint(1, 6)
#     return total


# Main program with function call
# attempts = 1
# while roll_dice(2) != 12:
#     attempts += 1
# print('After', attempts, 'attempts you rolled 12.')
# # print(throw_with_dice(2))

import random
def roll_dice(number_dice=1):
    """
    This function simulates throwing one or more dice.
    :param number of_dice: integer that indicates the number of dice used
    :return: a list with the number of pips on each stone.
    """
    if number_dice <= 0 or type(number_dice) != int:
        return None
    else:
        pips_rolled = []
        for i in range(0, number_dice):
            pips_rolled.append(random.randint(1, 6))
        return pips_rolled

assert roll_dice(2.5) == None


assert roll_dice(0) == None
assert roll_dice(-3) == None

# Main program with function call
# pips = roll_dice(3)
# total = 0
# for i in range(0, 3):
#     print('Dice', i + 1, ':', pips[i])
#     total += pips[i]
# print('Total: ', total)
