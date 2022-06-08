file1 = open("stock1.txt")
file2 = open("stock2.txt")
outputfile = open("stock3.txt", "w")
# Read title lines
record1 = file1.readline()
record2 = file2.readline()
outputfile.write(record1)

# Read real content
record1 = file1.readline()
record2 = file2.readline()
while record1 and record2:
    fields1 = record1.rstrip().split(';')
    fields2 = record2.rstrip().split(';')

    if fields1[0] < fields2[0]:
        outputfile.write(record1)
        record1 = file1.readline()
    elif fields1[0] == fields2[0]:
        total = int(fields1[1]) + int(fields2[1])
        record = fields1[0] + ";" + str(total) + "\n"
        outputfile.write(record)
        record1 = file1.readline()
        record2 = file2.readline()
    else:
        outputfile.write(record2)
        record2 = file2.readline()

# in either file there might be a "leftover" you need to read
while record1:
    outputfile.write(record1)
    record1 = file1.readline()
while record2:
    outputfile.write(record2)
    record2 = file2.readline()

file1.close()
file2.close()
outputfile.close()
