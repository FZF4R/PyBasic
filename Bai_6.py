class Bai_6():
    String1 = ''
    String2 = ''
    Numberx=0
    def __init__(self,string1='',string2='',numberx=''):
        self.Numberx=numberx
        self.String1=string1
        self.String2=string2
    def getString(self):
        x=input();
        self.String2=x
    def printString(self):
        print(self.String2.upper())
Bai6=Bai_6()
Bai6.getString()
Bai6.printString()