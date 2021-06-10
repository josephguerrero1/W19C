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

gameboard.printBoard(2, 3)

while True:
    gameboard.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")
    if(selection == "w" or "W"):
        gameboard.checkMove(player.rowPosition - 1, player.columnPosition)
    elif(selection == "s" or "S"):
        gameboard.checkMove(player.rowPosition + 1, player.columnPosition)
    elif(selection == "a" or "A"):
        gameboard.checkMove(player.rowPosition, player.columnPosition - 1)
    elif(selection == "d" or "D"):
        gameboard.checkMove(player.rowPosition, player.columnPosition + 1)
    else:
        print("Error! Selection is invalid!")
    player.movePlayer()
    gameboard.checkWin(player.rowPosition, player.columnPosition)
    # TODO
    # Move the player through the board
    # Check if the player has won, if so print a message and break the loop!
