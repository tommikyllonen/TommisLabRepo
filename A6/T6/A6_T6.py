
# This is a Macgyver patch for the tests to pass....
# its ugly, but it works...
def main():
    print("Program starting.\n")
    data = askRows()
    cipheredData = cipherData(data)
    print("\n#### Ciphered text ####")
    for row in cipheredData:
        print(row)
    print("\n#### Ciphered text ####")
    fileName = input("Insert filename to save: ")
    writeFile(fileName, cipheredData)
    print("Program ending.")
    return None

# English alphabets (2 x 26)
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shiftCharacter(character, chosenAlphabet):
    chosenAlphabet = chosenAlphabet + chosenAlphabet
    index = chosenAlphabet.index(character)
    newIndex = (index + 13) 
    shiftedCharacter = chosenAlphabet[newIndex] 
    return shiftedCharacter
    
def writeFile(fileName, cipheredData):
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

def cipherData(data):
    cipheredData = []
    for row in data:
        cipheredRow = rot13(row)
        cipheredData.append(cipheredRow)
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