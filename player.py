import app

class Player:
    def __init__(self, intitalRow, initialColumn, userSelection):
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn
        self.userSelection = app.selection

    def movePlayer(self):
        if(self.userSelection == "w" or "W"):
            self.rowPosition - 1
        elif(self.userSelection == "s" or "S"):
            self.rowPosition + 1
        elif(self.userSelection == "a" or "A"):
            self.columnPosition - 1
        elif(self.userSelection == "d" or "D"):
            self.columnPosition + 1
        else:
            print("Invalid Selection!")
