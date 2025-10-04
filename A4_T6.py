print("Program starting.")
steps = 0
userInt = int(input("Insert a positive integer: "))
print(int(userInt), end=" -> ")
while userInt != 1:
    isOdd = (userInt % 2) == 1
    if(isOdd):
        userInt = userInt * 3 + 1
    else:
        userInt = userInt / 2 
    steps += 1
    if int(userInt) != 1:
        print(int(userInt), end=" -> ")
    else:
        print(int(userInt))


print(f"Sequence had {steps} total steps.")
print("")
print("Program ending.")