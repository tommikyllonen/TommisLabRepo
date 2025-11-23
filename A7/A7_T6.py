import random
random.seed(1234)

def printImage(sign:str, player: str):
    print("#########################")
    if sign == '1':
        print(f"{player} chose rock.\n")
        print("    _______")
        print("---'   ____)")
        print("      (_____)")
        print("      (_____)")
        print("      (____)")
        print("---.__(___) ")
    elif sign == '2':
        print(f"{player} chose paper.\n")
        print("     _______")
        print("---'    ____)____")
        print("           ______)")
        print("          _______)")
        print("         _______)")
        print(" ---.__________)")

    elif sign == '3':
        print(f"{player} chose scissors.\n")
        print("    _______")
        print("---'   ____)____")
        print("          ______)")
        print("       __________)")
        print("      (____)")
        print("---.__(___)")
    print("")

def showRoundWinner(player1: str, player2: str, choice1: str, choice2: str):
    print("")
    print("#########################")
    print("Results:")
    if(winner):
        print(f"{player1} chose {choice1}, {player2} chose {choice2}.")

def printMenu():
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")
    selection = input("Your choice: ")
    print("Rock! Paper! Scissors! Shoot!")
    return selection
     
def gamePlay(player1: str, player2: str):
    print("Game starts...")
    while True:
        # whosTurn = player2 if whosTurn == player1 else player1

        winner = None
        P1selection = printMenu()
        P2Selection = str(random.randint(1,3))
        printImage(P1selection, player1)
        printImage(P2Selection, player2)

        #Selcect winner:
        if (P1selection == "1" and P2Selection == "3") or (P1selection == "2" and P2Selection == "1") or (P1selection == "3" and P2Selection == "2"):
            winner = player1
        elif (P2Selection == "1" and P1selection == "3") or (P2Selection == "2" and P1selection == "1") or (P2Selection == "3" and P1selection == "2"):
            winner = player2
        elif P1selection == P2Selection:
            winner = "Tie"
        if P1selection == "0":
            print("or playing!")
            break
        showRoundWinner(player1, player2, P1selection, P2Selection)
        # if selection == "1":
     


def main() -> None:
    player2 = "RPS-3PO"
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    player1 = input("Insert player name: ")
    print(f"Welcome {player1}!")
    print("Your opponent is RPS-3PO.")
    gamePlay(player1, player2)
    return None




if __name__ == "__main__":
    main()
