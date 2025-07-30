class IOString:
    def __init__(self):
        self.str1=""
    def input(self):
        self.str1=(input("enter a string"))
    def upper(self):
        print("upper case of your string is",self.str1.upper())
str1=IOString()
str1.input()
str1.upper()