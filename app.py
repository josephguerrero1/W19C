import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
# Create a new Player called played starting at position 3,2

board = gameboard.GameBoard()
played = player.Player(3, 2)


while True:
    board.printBoard(played.rowPosition, played.columnPosition)
    selection = input("Make a move: ")

    if(selection == "w"):
        board.checkMove(played.rowPosition - 1, played.columnPosition)
    elif(selection == "s"):
        board.checkMove(played.rowPosition + 1, played.columnPosition)
    elif(selection == "a"):
        board.checkMove(played.rowPosition, played.columnPosition - 1)
    elif(selection == "d"):
        board.checkMove(played.rowPosition, played.columnPosition + 1)
    else:
        print("Error! Selection is invalid!")

    if(selection == "w" and board[played.rowPosition][played.columnPosition].find("*") == -1):
        played.moveUp()
    elif(selection == "s" and board[played.rowPosition][played.columnPosition].find("*") == -1):
        played.moveDown()
    elif(selection == "a" and board[played.rowPosition][played.columnPosition].find("*") == -1):
        played.moveLeft()
    elif(selection == "d" and board[played.rowPosition][played.columnPosition].find("*") == -1):
        played.moveRight()
    else:
        print("Error! Invalid Selection!")

    board.checkWin(played.rowPosition, played.columnPosition)

    # TODO
    # Move the player through the board
    # Check if the player has won, if so print a message and break the loop!
