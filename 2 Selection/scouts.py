age = int(input("Your age = "))
if age < 6:
    print("You're too young!")
else:
    if age < 8:
        section = "Beavers"
    elif age <= 10:
        section = "Cubs"
    elif age <= 13:
        section = "Scouts"
    elif age <= 18:
        section = "Explorers"
    else:
        section = "Leaders"
    print("You'll be assigned to the", section)