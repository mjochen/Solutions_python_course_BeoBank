number1 = 0
number2 = 1
limit = int(input('Up to which limit would you like to print the sequence of Fibonacci? '))
if limit == 0:
     series = "0"
else:
     series = "0, 1"
     number3 = number1 + number2
     while number3 <= limit:
         series = series + ", " + str(number3)
         number1 = number2
         number2 = number3
         number3 = number1 + number2
print(series)
