'''
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

'''

class String():
    def __init__(self):
        self.s =""

    def get_string(self):
        self.s = input('Enter a name:')

    def print_string(self):
        print(self.s.upper())

    # same as    
    def string_lower(self):
        print(self.s.lower())
        


obj = String()
obj.get_string()
obj.print_string()
obj.string_lower()

