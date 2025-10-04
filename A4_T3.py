

print("Program starting.")
print("")
startValue = int(input("Insert starting value: "))
endValue = int(input("Insert stopping value: "))
print("")
print("Starting while-loop:")
finalString = ""


while (startValue < endValue + 1):
    if (len(finalString) == 0):
        finalString += str(startValue)
    else:
        finalString +=  " " + str(startValue)
    startValue += 1

print(finalString)
print("")
print("Program ending.")