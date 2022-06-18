first_names_1ITF = set()
first_names_2ITF = set()
with open('first_names1ITF.txt', encoding="utf8") as file1:
    name = file1.readline()
    while name:
        first_names_1ITF.add(name.rstrip())
        name = file1.readline()

with open('first_names2ITF.txt') as file2:
    name = file2.readline()
    while name:
        first_names_2ITF.add(name.rstrip())
        name = file2.readline()

print('In 1ITF there are', len(first_names_1ITF), 'different first names')
print('In 2ITF there are', len(first_names_2ITF), 'different first names')
# doubles = first_names_1ITF.intersection(first_names_2ITF)

doubles = list(first_names_1ITF.intersection(first_names_2ITF)) #Add list only if you want to press alphabetically
doubles.sort()

print('These are the', len(doubles), 'first names appearing in 1ITF and 2ITF')
for name in doubles:
     print(name)