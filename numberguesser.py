from random import randrange

class MyClass:
    def  __init__(self):
        self.randomNumber = randrange(0, 10)

    def validateAnswer(self, value):
        print(self.randomNumber)
        return int(value) == self.randomNumber

x = MyClass()
value = input("Please enter a number \n")

print(x.validateAnswer(value))
