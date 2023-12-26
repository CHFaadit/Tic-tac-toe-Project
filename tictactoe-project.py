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
    inp = int(input("Enter a number from 1 to 9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("You cannot take what is already taken!")


# Checking for win by achieving three in a row horizontally, vertically, or diagonally
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkCross(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

# Checking for tie by seeing if nobody won but the board is full, and ending the game if it is a tie
def checkTie(board):
    global gameRunning
    if "-" not in board:
        print("It is a tie!")
        printBoard(board)
        gameRunning = False

# Printing winner if there is one and ending game once winner is found
def checkWin():
    global gameRunning
    if checkHorizontal(board) or checkVertical(board) or checkCross(board):
        print(f"The winner is {winner}! They are better.")
        gameRunning = False



# Switching player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"

# Creating computer to play against (plays randomly)
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()



# Running the game
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    if gameRunning:
        switchPlayer()
        computer(board)
        checkWin()
        checkTie(board)