input_file = open('hamlet.txt', 'r')
# oefening a)
output_file = open('hamlet2.txt', 'w')


# oefening b)
output_file = open('hamlet3.txt', 'w')

# oefening a)
# lines = input_file.readlines()
# for line in lines:
#     for character in ',.;:?!':
#         line = line.replace(character+'  ', character+' ')
#     output_file.write(line)

# oefening b)
def remove_vowels(line):
    new_line = ""
    for character in line:
        if character not in "aeiouAEIOU":
            new_line += character
    return new_line


counter_read = 0
counter_write = 0
line = input_file.readline()

while line:
    counter_read += len(line)
    line = remove_vowels(line)
    counter_write += len(line)
    output_file.write(line)
    line = input_file.readline()

output_file.close()
input_file.close()
print("The input file contains", counter_read, "characters")
print("The output file contains:", counter_write, "characters")

output_file.close()
input_file.close()
