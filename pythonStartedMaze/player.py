class Player:
    def __init__(self, intitalRow, initialColumn):
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn

    def moveUp(self):
        if(userMove == "w"):
            self.rowPosition - 1

    def moveDown(self):
        userMove = input("")
        if(userMove == "s"):
            self.rowPosition + 1

    def moveLeft(self):
        userMove = input("")
        if(userMove == "a"):
            self.rowPosition - 1

    def moveRight(self):
        userMove = input("")
        if(userMove == "d"):
            self.rowPosition + 1
