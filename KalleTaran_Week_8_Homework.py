"""
PYTHON PROGRAMMING 1
HOMEWORK
WEEK EIGHT

author: TARAN KALLE
** be sure to RENAME the file <Last><First>_Week_8_Homework.py
** example: BeemerBill_Week_8_Homework.py
"""
#
"""
Complete the following problems
"""
#
"""
Problem #1
(2 pts)

Add four NEW methods to the Point class:

up()
down()
left()
right()

NOTE: The implentation of each of the above should NOT modify the 
instance variables x or y directly, but rather indirectly by calling
the existing method move().

Demonstrate examples of ALL FOUR methods being implemented 
with correct results - see below for an example of ONE method.

Example:

myPoint = Point()
myPoint.setx(3)
myPoint.sety(1)
print(myPoint.get()) # should print (3, 1)

myPoint.left()
print(myPoint.get()) # should print (2, 1)

Expected Results:
(3, 1)
(2, 1)

"""
# Please enter your answer here
# 

class Point:
    def setx(self, xcoord):
        self.x = xcoord

    def sety(self, ycoord):
        self.y = ycoord

    def get(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def up(self):
        self.move(0,1)

    def down(self):
        self.move(0,-1)

    def left(self):
        self.move(-1,0)

    def right(self):
        self.move(1,0)

myPoint = Point()
myPoint.setx(3)
myPoint.sety(1)
print(myPoint.get()) # should print (3, 1)

myPoint.left()
print(myPoint.get()) # should print (2, 1)

myPoint.down()
print(myPoint.get()) # should print (2, 0)

myPoint.right()
print(myPoint.get()) # should print (3, 0)

myPoint.up()
print(myPoint.get()) # should print (3, 1)

"""
Problem #2
(2 pts)

Add a constructor to class Rectangle so that the length 
and width of the rectangle can be set at the time 
the Rectangle object is created.
Use the default values of 1 for both length 
and width if not specified.

Demonstrate three (3) examples of using the defaults 
values AND using user provided inputs AND using a mix 
of a default value and a user provided input.

class Rectangle:
   
    def setSize(self, width, length):
        self.width = width
        self.length = length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area(self):
        return self.width * self.length

Examples:
myRectangle = Rectangle(2, 4)
myRectangle.perimeter()      # should print 12

otherRect = Rectangle()
otherRect.area()             # should print 1


Expected Results:
12
1

"""
# Please enter your answer here
# 
class Rectangle:
    def __init__(self, length = 1, width = 1):
        self.length = length
        self.width = width


    def setSize(self, width, length):
        self.width = width
        self.length = length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area(self):
        return self.width * self.length

myRectangle = Rectangle(2, 4)
print(myRectangle.perimeter())

otherRect = Rectangle()
print(otherRect.area())

newRect = Rectangle(5)
print(newRect.area())


"""
Problem #3
(2 pts)

Develop a class BankAccount that supports the following methods:

__init__() : initializes the balance with value of input argument
or 0 if no input is provided

withdraw() : takes amount as input and subtracts from the balance

deposit() : takes amount as input and adds to the balance

balance() : prints the current balance 

Demonstrate the functionality of the class object by showing
the following:
a) create a new BankAccount object using an input argument
b) demonstrate both withdraw and deposit followed by showing
the balance afterward
c) create another new BankAccount object using the default 
constructor
d) demonstrate both withdraw and deposit followed by showing
the balance afterward


"""
# Please enter your solution here
# 

class BankAccount:
    def __init__(self,balance):
        self.balanceAmount = balance

    def withdraw(self,amount):
        self.balanceAmount -= amount

    def deposit(self,amount):
        self.balanceAmount += amount

    def balance(self):
        print(self.balanceAmount)


newAccount = BankAccount(5000)

newAccount.withdraw(50)
newAccount.balance()

newAccount.deposit(100)
newAccount.balance()

twoAccount = BankAccount(6000)

twoAccount.withdraw(500)
twoAccount.balance()

twoAccount.deposit(50)
twoAccount.balance()


"""
Problem #4 and #5
(4 pts)

Create the class Hand that represents a players hand 
of playing cards.  The class should have a constructor
that takes as input a string that represents the players
name. (e.g. myHand = Hand("Beemer")) 
It should support two (2) methods:

addCard - takes a card object as input, and adds it to hand
(e.g. hand.addCard(myDeck.dealCard()))

showHand - that displays the players name and all cards in hand
(e.g. hand.showHand())

Use the existing Card and Deck code built during the class
lecture (provided below including the import statement)

Be sure to demonstrate the creation of two (2) hands
with five (5) cards EACH created from the SAME deck 
and display the contents of both hands.

See Problem 8.29 on p.283 for example of output

"""
# Please enter your solution here
#

from random import shuffle

class Hand:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def addCard(self,card: object):
        self.hand.append(card)

    def showHand(self):
        for cardObj in self.hand:
            print("{0} of {1}".format(cardObj.getRank(),cardObj.getSuit()))


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit


class Deck:
    ranks = {"2","3","4","5","6","7","8","9","10","J","Q","K","A"}
    suits = {"\u2660", "\u2661", "\u2662", "\u2663"}

    def __init__(self):
        self.deck = []
        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.deck.append(Card(rank, suit))

    def shuffleDeck(self):
        shuffle(self.deck)

    def dealCard(self):
        return self.deck.pop()

myDeck = Deck()
myDeck.shuffleDeck()
handOne = Hand("Person 1")
for i in range(1,6):
    handOne.addCard(myDeck.dealCard())
print(handOne.name)
handOne.showHand()

print("\n")

handTwo = Hand("Person 2")
for i in range(1,6):
    handTwo.addCard(myDeck.dealCard())
print(handTwo.name)
handTwo.showHand()

"""
BONUS PROBLEM
EXTRA CREDIT
(Bonus 1 pts)


The following code does not work - it does not function as expected...
Try to resolve any issues/bugs/problems you can...

hint: 
there are five known issues

Expected Output:

Canis Familiaris
Buddy says woof!
Buddy
Golden Retriever
4
Bradley
Golden Retriever
7

To get credit please comment (using # tags) EVERY issue/bug/problem you 
find as well as make the appropriate correction!

"""

class Dog:


    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.species = "Canis Familiaris" #moved to contractor

    def bark(self):
        print("{0} says woof!".format(self.name))

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def getBreed(self):
        return self.breed

    def setBreed(self, breed):
        self.breed = breed

myDog = Dog("Buddy", "Golden Retriever", 4) # Missing breed
print(myDog.species) # Not a function
myDog.bark() # print is included in the function
print(myDog.name) # Not a function
print(myDog.getBreed())
print(myDog.getAge())
myDog.name = "Bradley" # Not a function
myDog.setAge(7)
print(myDog.name) # Not a function
print(myDog.getBreed())
print(myDog.getAge())


"""
END
"""
