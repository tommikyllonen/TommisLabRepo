def main():
    print("Program starting.\n")
    userInput = input("Insert word: ")
    frameWord(userInput)
    print("\nProgram ending.")

def frameWord(word):
    rowLength = len(word) + 4
    print("*" * rowLength)
    print(f"* {word} *")
    print("*" * rowLength)

