from symtable import Class

class Card:
    number = "0000 0000 0000 0000"
    validDate = "11/24"
    holder = "unknown"

    def __init__(self, number, holder, date):
        self.number = number
        self.holder = holder
        self.validDate = date

    def pay(self, amount):
        print("с карты",self.number,"списали",amount)

