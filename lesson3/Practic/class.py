from User import User
from Card import Card

User1=User("Вася")

User1.sayName()
User1.sayage()
User1.setAge(33)
User1.sayage()

Card = Card("2451 6655 7788 9900","User1 F","11/28")

User1.addCard(Card)
User1.getCard().pay(1000)









