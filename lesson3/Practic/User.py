class User:
    age= 0

    def __init__(self, name):
        print("Я создался")
        self.username = name

    def sayName(self):
        print("Меня зовут", self.username)

    def sayage(self):
        print(self.age)

    def setAge(self, newAge):
        self.age = newAge

    def addCard(self, Card):
        self.Card = Card

    def getCard(self):
        return self.Card