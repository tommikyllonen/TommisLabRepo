import random
random.seed(1234)

def printImage(sign:str, player: str):
    print("#########################")
    if sign == 'rock':
        print(f"{player} chose rock.\n")
        print("    _______")
        print("---'   ____)")
        print("      (_____)")
        print("      (_____)")
        print("      (____)")
        print("---.__(___) ")
    elif sign == 'paper':
        print(f"{player} chose paper.\n")
        print("     _______")
        print("---'    ____)____")
        print("           ______)")
        print("          _______)")
        print("         _______)")
        print(" ---.__________)")

    elif sign == 'scissors':
        print(f"{player} chose scissors.\n")
        print("    _______")
        print("---'   ____)____")
        print("          ______)")
        print("       __________)")
        print("      (____)")
        print("---.__(___)")
    print("")

def showRoundWinner(player1: str, player2: str, choice1: str, choice2: str, winner: str):
    print("")
    print("#########################")
    print("Results:")
    if(winner == "Tie"):
        print(f"Draw! Both players chose {choice1}")
    if(winner == player1):
        print(f"{player1} {choice1} beats {player2} {choice2}.")
    if(winner == player2):
        print(f"{player2} {choice2} beats {player1} {choice1}.")

def printMenu():
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")
    selection = input("Your choice: ")
    if(selection != "0"):
        print("Rock! Paper! Scissors! Shoot!")
    return selection


def changeToText(num:str):
    result = "" 
    if (num == "1"):result = "rock"
    if (num == "2"):result = "paper"
    if (num == "3"):result = "scissors"
    if (num == "0"): return num

    return result


def gamePlay(player1: str, player2: str):
    print("Game starts...")
    player1Score = 0
    player2Score = 0
    ties = 0
    while True:
        winner = None

        P1selection = changeToText(printMenu())
        if P1selection == "0":
            break
        P2Selection = changeToText(str(random.randint(1,3)))

        printImage(P1selection, player1)
        printImage(P2Selection, player2)
        #Selcect winner:
        if (P1selection == "rock" and P2Selection == "scissors") or (P1selection == "paper" and P2Selection == "rock") or (P1selection == "scissors" and P2Selection == "paper"):
            winner = player1
            player1Score += 1
        elif (P2Selection == "rock" and P1selection == "scissors") or (P2Selection == "paper" and P1selection == "rock") or (P2Selection == "scissors" and P1selection == "paper"):
            winner = player2
            player2Score += 1
        elif P1selection == P2Selection:
            winner = "Tie"
            ties += 1
        showRoundWinner(player1, player2, P1selection, P2Selection, winner)
    #print results
    print(f"{player1} - wins ({player1Score}), losses ({player2Score}), draws ({ties})")
    print(f"{player2} - wins ({player2Score}), losses ({player1Score}), draws ({ties})")



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
