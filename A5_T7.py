
def main():
    print("Program starting.")
    wordsString = collectWords()
    analyseWords(wordsString)
    print("Program ending.")

def analyseWords(wordsString: str):
    wordsList = wordsString.split(",")
    stringLength = len(wordsString.replace(",", "")) 
    listLength = len(wordsList)
    avgWordLength = round((stringLength / listLength), 2)
    print(f"- {listLength} Words")
    print(f"- {stringLength} Characters")
    #.2f always prints 2 decimals, even if its .00 at the end. Normally python prints
    # number that has only zeros after the dot like this .0
    print(f"- {avgWordLength:.2f} Average word length")

def collectWords() -> str:
    wordsString = ""
    while True:
        nextWord =  input("Insert word(empty stops): ")
        if nextWord == "":
            return wordsString[1:]
        wordsString = f"{wordsString},{nextWord}"

main()