class Strings:
    def __init__(self,word=""):
            self.word=word
    def getString(self):
        self.word=input("Enter string: ")
        
    def printString(self):
         print(self.word)

x=Strings()
x.getString()
x.printString()