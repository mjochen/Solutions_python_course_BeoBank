# animals = {'horse': 'whinnying', 'cat': 'meows', 'dog': 'barks', 'cow': 'mooing'}
animals = {}
with open('animal_sounds.txt','r') as file:
    line = file.readline()
    while line:
        fields = line.strip().split(";")
        animals[fields[0]]=fields[1]
        line = file.readline()

correct = 0
print('Do you know the animal sounds?')
# print(animals)
for animal in animals:
    sound = input('What is the sound of a ' + animal + ': ')
    if sound == animals[animal]:
        correct += 1

print('You have', correct, 'correct answers.')