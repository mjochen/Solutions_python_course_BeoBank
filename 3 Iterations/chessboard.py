number = 0
for i in range(1, 65):
    number += 2 ** i

weight = number * 0.065
print('On the chessboard lie ' + str(number) + ' Grains with a total weight of ' + str(weight) + 'gram.')
