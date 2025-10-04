print("Program starting.")
print("")
startPoint = int(input("Insert starting point: "))
stoppingPoint = int(input("Insert stopping point: "))
inspectionPoint = int(input("Insert inspection point: "))
print("")
if(inspectionPoint >= startPoint and inspectionPoint <= stoppingPoint):
    print("First loop - inspection with break:")
    for i in range(startPoint - 1, stoppingPoint - 1):
        if(i == inspectionPoint - 1):
            break

        if(i == inspectionPoint - 2):
            print(i + 1, end ="") 
        else:
            print(i + 1, end =" ")

    print("\nSecond loop - inspection with continue:")
    for i in range(startPoint - 1, stoppingPoint -1):
        if(i == inspectionPoint - 1):
            continue

        if(i == stoppingPoint - 1):
            print(i + 1, end ="") 
        else:
            print(i + 1, end =" ")
    # print("\n")

else:
    if(startPoint == stoppingPoint):
        print("Starting point value must be less than the stopping point value.")
    print("Inspection value must be within the range of start and stop.")
print("\n\nProgram ending.")
print("")