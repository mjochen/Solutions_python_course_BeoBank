tasks = {}
with open('tasks.csv') as file:
    title = file.readline()  # title line read and do nothing with it
    line = file.readline().rstrip()

    while line:
        names = line.split(';')
        for i in range(1, len(names)):
            if names[i] in tasks:
                tasks[names[i]] += 1
            else:
                tasks[names[i]] = 1
        line = file.readline().rstrip()

print('Task distribution:')
for person in tasks:
    print(person, tasks[person])