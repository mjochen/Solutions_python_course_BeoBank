bottles_wine = int(input('How many bottles of wine are there: '))
pizzas = int(input ("How many pizzas are there: "))

if pizzas < 5 or bottles_wine < 5:
    answer = "This is just a stupid party"
else:
    if bottles_wine >= 5 and pizzas >= 5 \
             and pizzas >= 2 * bottles_wine or bottles_wine >= 2 * pizzas:
        answer = "This is a fantastic party"
    else:
        answer = "This is a good party"

print(answer)
