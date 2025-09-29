print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")
print("")
print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
userChoice = input("Your choice: ")
print("")
if userChoice == "0":
    print("Exiting...")
elif userChoice == "1":
    print("Length options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    userChoice = input("Your choice: ")

    if userChoice == "0":
        print("Exiting...")
    elif userChoice == "1":
        meters = float(input("Insert meters: "))
        print(f"{round(meters, 1)} m is {round((meters / 1000), 1)} km")
    elif userChoice == "2":
        kilometers = float(input("Insert kilometers: "))
        print(f"{round(kilometers, 1)} km is {round((kilometers * 1000), 1)} m")
    else:
        print("Unknown option.")
        
elif userChoice == "2":
    print("Weight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    userChoice = input("Your choice: ")
    if userChoice == "0":
        print("Exiting...")
    elif userChoice == "1":
        grams = float(input("Insert grams: "))
        pounds = grams * 0.002205
        print(f"{round(grams, 1)} g is {round(pounds, 1)} lb")

    elif userChoice == "2":
         pounds = float(input("Insert pounds: "))
         grams = pounds * 453.6
         print(f"{round(pounds, 1)} lb is {round(grams, 1)} g")
    else:
        print("Unknown option.")

else:
    print("Unknown option.")

        
print("\nProgram ending.")