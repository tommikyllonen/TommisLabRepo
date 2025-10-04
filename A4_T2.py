
print("Program starting.")
print("")
startValue = int(input("Insert starting value: "))
endValue = int(input("Insert stopping value: "))
print("")
print("Starting for-loop:")
finalString = ""
for i in range(startValue, endValue + 1):
    if (len(finalString) != 0):
        finalString +=  " " + str(i)
    else:
        finalString += str(i)
print(finalString)
print("")
print("Program ending.")



