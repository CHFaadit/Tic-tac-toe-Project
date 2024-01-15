import random

print("This project is a simple, single-player implementation of the popular Tic-tac-toe/Xs and Os game in Python.")

print(" ")

print("The rules are straightforward and as follows:")

print("You will be playing against the computer, which randomly plays its moves. You and your opponent will take turns \n"
      "placing down your assigned symbol, either X or O, on a three-by-three grid. If either team achieves placing three \n"
      "of their symbols in a row either horizontally, vertically, or diagnally, then they will be crowned the winner and \n"
      "the game will end. If the board becomes full but no team has won, then a tie will be called and the game will end. \n"
      "If either team places down their symbol where a symbol already exists, they will lose their turn, and the game will \n"
      "proceed as expected. You will be given the first move.")

print(" ")

print("You can play by entering a number from 1 to 9. The number you choose corresponds to where your symbol will be put down. \n"
      "The following image represents which position on the grid each number corresponds to:")

print(" ")

example_chart = ["1", "2", "3",
                        "4", "5", "6",
                        "7", "8", "9"]

def printBoard(example_chart):
    print(example_chart[0] + " | " + example_chart[1] + " | " + example_chart[2])
    print("---------")
    print(example_chart[3] + " | " + example_chart[4] + " | " + example_chart[5])
    print("---------")
    print(example_chart[6] + " | " + example_chart[7] + " | " + example_chart[8])

printBoard(example_chart)


print("")

print(" ")

print("You are assigned the symbol X and your opponent is assigned the symbol O.")
print("Let the games begin!")

print("")


# Creating global variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True

# Printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Consuming player input
def playerInput(board):
    if currentPlayer == "X":
        inp = int(input("Enter a number from 1 to 9: "))
        if inp >= 1 and inp <= 9 and board[inp-1] == "-":
            board[inp-1] = currentPlayer
        else:
            print("You cannot take what is already taken!")

# Checking for win by achieving three in a row horizontally, vertically, or diagonally
def checkWin(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Checking for tie by seeing if nobody won but the board is full, and ending the game if it is a tie
def checkTie(board):
    global gameRunning
    if "-" not in board:
        print("It is a tie!")
        printBoard(board)
        gameRunning = False

# Switching player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"

# Creating computer to play against (plays smarter)
def computer(board):
    while currentPlayer == "O":
        # Check if computer can win in the next move
        for i in range(9):
            if board[i] == "-":
                board[i] = "O"
                if checkWin(board, "O"):
                    return
                board[i] = "-"

        # Check if player can win in the next move and block them
        for i in range(9):
            if board[i] == "-":
                board[i] = "X"
                if checkWin(board, "X"):
                    board[i] = "O"
                    return
                board[i] = "-"

        # If no immediate win or block, then take a random available move
        while True:
            position = random.randint(0, 8)
            if board[position] == "-":
                board[position] = "O"
                return

# Running the game
while gameRunning:
    printBoard(board)
    if currentPlayer == "X":
        playerInput(board)
        if checkWin(board, "X"):
            print("The winner is X! They are better.")
            break
        checkTie(board)
    if gameRunning:
        switchPlayer()
        computer(board)
        if checkWin(board, "O"):
            print("The winner is O! They are better.")
            break
        checkTie(board)
