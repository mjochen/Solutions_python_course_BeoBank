# dia 5
# numbers = {10, 90, 70, 56}
# french_letters = set()
# for sign in "éçàèéàèçé":
#      french_letters.add(sign)
# vowels = set('aeiou')
# squares = set(x**2 for x in range(10))
#
# print(numbers)
# print(french_letters)
# print(vowels)
# print(squares)


# dia 6
# vegetables = {"leek", "tomato", "celery", "endive", "fennel"}
# print('The set contains', len(vegetables), 'elements')
# for element in vegetables:
#     print(element)
# print()

# dia 7
# vegetables = {"leek", "tomato", "celery", "endive", "fennel"}
# vegetable_list = list(vegetables)
# vegetable_list.sort()
# for element in vegetable_list:
#      print(element)


# dia 8
# vegetables = {'tomato', 'celery', 'endive', 'fennel' }
# print(vegetables)
#
# vegetables.remove('celery')
# print(vegetables)
#
# vegetables.add('lettuce')
# vegetables.add('leeks')
# print(vegetables)
#
# vegetables.clear()
# print(vegetables)
#
# dia 9-10
# vegetables1 = {'tomato', 'celery', 'endive', 'fennel' }
# vegetables2 = {'cucumber', 'tomato', 'celery'}
#
# # vegetable_union = vegetables1.union(vegetables2)
# vegetable_union = vegetables1 | vegetables2
# # vegetable_difference = vegetables1.difference(vegetables2)
# vegetable_difference = vegetables1 - vegetables2
# # vegetable_intersection = vegetables1.intersection(vegetables2)
# vegetable_intersection = vegetables1 & vegetables2
# #
# print('union:', vegetable_union)
# print('difference:', vegetable_difference)
# print('intersection:', vegetable_intersection)

#dia 11-
# vegetables1 = {'tomato', 'celery', 'endive', 'fennel' }
# vegetables2 = {'cucumber', 'tomato', 'celery'}
# vegetables3 = {'endive', 'fennel'}
#
# print(vegetables2.issubset(vegetables1))         #False
# print(vegetables3.issubset(vegetables1))         #True
# print(vegetables1.issubset(vegetables1))         #True
#
# print(vegetables2.issuperset(vegetables3))       #False
# print(vegetables1.issuperset(vegetables3))       #True
#
# print(vegetables1.isdisjoint(vegetables2))       #False
# print(vegetables2.isdisjoint(vegetables3))       #True

# dia 12-13
# word = 'hottentot'
# characters = ['e', 'h', 'n', 'o', 't']
# occurrence = [1, 1, 1, 2, 4]
# print('Occurrences of letter t:', occurrence[characters.index('t')])

# dia 14-15-16
# letters = {'e': 1, 'h': 1, 'n': 1, 'o': 2, 't': 4}
# print('Occurrences of letter t:', letters['t'])
#
# my_choice = input('Letter? ')
# print(letters.get(my_choice, 'This character does not occur'))

word = input('Enter a word: ')
characters = {}
# go through letters in word
for letter in word:
    # check if letter is present in dictionary
    if letter in characters:
        characters[letter] += 1    # increase value via key
    else:
        characters[letter] = 1     # create new key/value pair
# print key/value pairs
for character in characters:
    print(character, characters[character])

print('Total:', sum(characters.values()), 'chars')
for character in sorted(characters):
    print(character, characters[character])

for character in sorted(characters, reverse=True):
    print(character, characters[character])


