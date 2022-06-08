# start = ord('a')
# for i in range(26):
#     print(chr(start + i) + ' ', end='')

# start = ord('a')
# for i in range(26):
#     print(chr(start + i) + ' ', end='')
#     if i % 6 == 5:
#         print()

# sport = "baseball"
# i = 0
# while i < len(sport):
#     print(sport[i])
#     i += 1
#
# sport = "baseball"
# for i in range(len(sport)):
#     print(i, sport[i])
#
# sport = "baseball"
# for letter in sport:
#     print(letter)

# word = 'mystery'
# print(word[2])
# print(word[2:])
# print(word[:2])
# print(word[2:2])
# print(word[::2])
# print(word[-2])
# print(word[-2:])
# print(word[:-2])
# print(word[::-2])
# print(word[-2::-2])
# print(word[::-1])
#
# punctuation_marks = ',.:;?!'
# sentence = input('Enter a sentence with punctuation marks: ')
# sentence_without = ''
#
# for letter in sentence:
#     if letter not in punctuation_marks:
#         sentence_without += letter
#
# print('The sentence without punctuation marks:', sentence_without)
#
# season = "summer"
# season.capitalize()
# print(season)
# print(season.upper())
# new_season = season.replace('m','n')
# print(season, new_season)
# print(season.count('m'))

# number = int(input('Enter a number: '))
# print('Double of {} is {}'.format(number, number * 2))
#
# for number in range(1,11):
#     print('{} {} {}'.format(number, number / 2, number * 2))

number = 1 / 7
score = 17

print('The number: {:.5}'.format(number))
print('Your percentage: {:.2%}'.format(score / 30))
