class IOSstring:
    def __init__(self) :
        self.string=""


    def getString(self):
        self.string = input("Enter any String : ")


    def printString(self):
        print("The result is", self.string.upper())


object = IOSstring()
object.getString()
object.printString()

       