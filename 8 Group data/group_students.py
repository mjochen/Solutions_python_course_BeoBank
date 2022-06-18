input_file = open('courses.csv')
output_file = open('students.csv','w')

line = input_file.readline() #read title line and do nothing with it
line = input_file.readline().rstrip() # read first real line
while line:
    record = line.split(';')
    studentind = record[3]
    student_info = studentind+';' + record[4] + ';' + record[5]
    while line and record[3] == studentind:
        student_info += ';'+record[1]+' ('+record[2] + ')'
        line = input_file.readline().rstrip()
        record = line.split(';')
    output_file.write(student_info +'\n')
    print(student_info)

input_file.close()
output_file.close()