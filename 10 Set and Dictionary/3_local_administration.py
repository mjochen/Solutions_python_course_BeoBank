classrooms = set()
with open('local_booking.txt') as file:
    lesson = file.readline()
    while lesson:
        fields = lesson.split(';')
        classrooms.add(fields[3])
        lesson = file.readline()

print('Classrooms:')
for room in classrooms:
     print(room)