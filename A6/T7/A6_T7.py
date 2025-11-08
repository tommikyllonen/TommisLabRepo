# This is a Macgyver patch for the tests to pass....
# its ugly, but it works...
def main() -> None:
    print("travel starting.")
    PlayerProgressFilename = "player_progress.txt"
    Progress = readFile(PlayerProgressFilename)
    LastProgress = Progress.strip().splitlines()[-1].split(";")
    # LastProgress = Progress.strip().split("\n")[-1].split(";")
    currentLocationId = int(LastProgress[0])
    currentLocation = getLocation(currentLocationId)
    nextLocationId = int(LastProgress[1])
    nextLocation = getLocation(nextLocationId)
    passphrase = LastProgress[2]
    print(f"Currently at {currentLocation}.")
    print(f"Travelling to {nextLocation}...")
    print(f"Passing the guard at the entrance.")
    decipheredPassphrase = cipherData(passphrase, cipherData=False)
    print(f"Passphrase to get in: {decipheredPassphrase}")
    return None


    print("Program starting.\n")
    data = askRows()
    cipheredData = cipherData(data=data, cipherData=2)
    print("\n#### Ciphered text ####")
    for row in cipheredData:
        print(row)
    print("\n#### Ciphered text ####")
    fileName = input("Insert filename to save: ")
    writeFile(fileName, cipheredData)
    print("Program ending.")
    return None


def getLocation(locationId) -> str:
    location = "unknown"
    if locationId == 0:
        location = "Home"
    elif locationId == 1:
        location = "Galba's palace"
    elif locationId == 2:
        location = "Otho's palace"
    elif locationId == 3:
        location = "Vitellius' palace"
    elif locationId == 4:
        location = "Vespasian's palace" 
    return location


# English alphabets (2 x 26)
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shiftCharacter(character, chosenAlphabet):
    chosenAlphabet = chosenAlphabet + chosenAlphabet
    index = chosenAlphabet.index(character)
    newIndex = (index + 13) 
    shiftedCharacter = chosenAlphabet[newIndex] 
    return shiftedCharacter
    
def writeFile(fileName, cipheredData) -> None:
    if fileName == "":
        print("File name not defined.")
        print("Aborting save operation.")
        return
    outputFile = open(fileName, "w", encoding='UTF-8')
    if isinstance(cipheredData, str):
        outputFile.write(cipheredData) 
    else:
        for i in cipheredData:
            outputFile.write(i + "\n")
    outputFile.close()
    print("Ciphered text saved!")
def appendToFile(fileName, cipheredData) -> None:
    if fileName == "":
        print("File name not defined.")
        print("Aborting save operation.")
        return
    outputFile = open(fileName, "a", encoding='UTF-8')
    if isinstance(cipheredData, str):
        outputFile.write(cipheredData) 
    else:
        for i in cipheredData:
            outputFile.write(i + "\n")
    outputFile.close()
    print("Ciphered text appended!")

def readFile(fileName) -> str:
    content = ''
    fileHandle = open(fileName, "r")
    Row = fileHandle.readline()
    while Row != '':
        content += Row
        Row = fileHandle.readline()
    fileHandle.close()
    return content 

def cipherData(data:str, cipherData:bool=True):
    # shiftDirection: 
    # 1 == forward ==> cipher
    # 0 == backward ==> decipher
    cipheredData = ""
    if cipherData:
        cipheredData = rot13(data)
    else:
        cipheredData = rot13Reverse(data)
    # cipheredData.append(cipheredRow)
    return cipheredData

def rot13(inputRow):
        cipheredRow = ""
        for i in inputRow:
            if i.isupper():
                cipheredRow += shiftCharacter(i, UPPER_ALPHABETS)
            elif i.islower():
                cipheredRow += shiftCharacter(i, LOWER_ALPHABETS)
            else:
                cipheredRow += i
        return cipheredRow
def rot13Reverse(inputRow):
        decipheredRow = ""
        for i in inputRow:
            if i.isupper():
                decipheredRow += shiftCharacter(i, UPPER_ALPHABETS)
            elif i.islower():
                decipheredRow += shiftCharacter(i, LOWER_ALPHABETS)
            else:
                decipheredRow += i
        return decipheredRow


    
def askRows():
    print("Collecting plain text rows for ciphering.")
    inputRows = []
    row = ""
    while True:
        row = input("Insert row(empty stops): ")
        if row != "":
            inputRows.append(row)
        if row == "":
            break
    return inputRows



if __name__ == "__main__":
    main()