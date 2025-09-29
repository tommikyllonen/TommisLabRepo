
print("Program starting.")
print("Testing decision structures.")
userInt = int(input("Insert an integer: "))
print("Options:")
print("1 - In one multi-branched decision")
print("2 - In multiple independent if-statements")
print("0 - Exit")
userSelection = input("Your choice: ")
# if int(userSelection) not in range(3):
if userSelection not in ["0", "1", "2"]:
    print ("Unknown option.")
if userSelection == "0":
    print("Exiting...")

if userSelection == "1":
    print("Using one multi-branched decision structure.")
    if userInt >= 400:
        userInt += 44
    elif userInt >= 200:
        userInt += 22
    elif userInt >= 100:
        userInt += 11

if userSelection == "2":
    print("Using one multi-branched decision structure.")
    if userInt >= 400:
        userInt += 44
    if userInt >= 200:
        userInt += 22
    if userInt >= 100:
        userInt += 11
    
if userSelection in ["1", "2"]:
    print(f"Result is {userInt}")

print("")

print("Program ending.")

