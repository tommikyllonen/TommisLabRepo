print("Program starting.")
print("")
print("Check multiplicative persistence.")
steps = 0
userString = input("Insert an integer: ")
# userStringLength = len(userString)
result = 1
resultList = []
while True:
    tempString = ""
    for i in userString:
        steps += 1
        result = result * int(i)
        if(len(userString) == steps):
            tempString += f"{i} = "
        else:
            tempString += f"{i} * "
    steps = 0
    tempString += str(result)
    resultList.append(tempString)
    # print(result)
    if len(str(result)) == 1:
        break
    userString = str(result)
    tempString = ""
    result = 1
for i in resultList:
    print(i)
print("No more steps.")
print("")
print(f"This program took {len(resultList)} step(s)")
print("")
print("Program ending.")