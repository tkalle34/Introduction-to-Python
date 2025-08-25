"""
PYTHON PROGRAMMING 1
HOMEWORK
WEEK NINE

author: Taran Kalle
** be sure to RENAME the file <Last><First>_Week_9_Homework.py
** example: BeemerBill_Week_9_Homework.py
"""
#
"""
Complete the following problems
"""
#
"""
Problem #1
(2 pts)

Translate these operator expressions into their matching method calls:

Be sure to double check your syntax by printing examples of each of
the examples followed by their marching method calls.

Example:
x, y = 2, 4
# x + y
print(x + y)
print(int(x).__add__(y))

a) x > y
b) x != y
c) x % y
d) x // y
e) x <= y
f) x * y
g) x == y
h) x - y
i) x >= y
j) x / y


"""
# Please enter your answer here
#

x, y = 2, 4
print(x > y)
print(x.__gt__(y))

print(x != y)
print(x.__ne__(y))

print(x % y)
print(x.__mod__(y))

print(x // y)
print(x.__floordiv__(y))

print(x <= y)
print(x.__le__(y))

print(x * y)
print(x.__mul__(y))

print(x == y)
print(x.__eq__(y))

print(x - y)
print(x.__sub__(y))

print(x >= y)
print(x.__ge__(y))

print(x / y)
print(x.__truediv__(y))



"""
Problem #2
(2 pts)

Overload appropriate operators for class Card so that you can compare
cards based on rank.  (Note: the comparison should ONLY be rank, not suit)

Be sure to check your work by printing out all four (4) comparisons 

firstCard = Card("3", "\u2660")
secondCard = Card("8", "\u2662")

print(firstCard < secondCard)
print(firstCard > secondCard)
print(firstCard <= secondCard)
print(firstCard >= secondCard)

Results:
True 
False
True
False

"""
# Please enter your answer here
# 

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit
    
    def __str__(self):
        return 'Card({}, {})'.format(self.rank, self.suit)

    def __lt__(self, card2):
        return self.rank < card2.rank

    def __le__(self, card2):
        return self.rank <= card2.rank

firstCard = Card("3", "\u2660")
secondCard = Card("8", "\u2662")

print(firstCard < secondCard)
print(firstCard > secondCard)
print(firstCard <= secondCard)
print(firstCard >= secondCard)

"""
Problem #3
(2 pts)

Implement a new class myInteger that behaves the same as the class int.
Except, when you are trying to ADD an object of type myInteger you
get this strange behavior:

x = myInteger(6)
print(x * 4)
print(x * (3 + 2))
print(x + 6)

Results:
24
30
Whatever ...

"""
# Please enter your solution here
# 


class myInteger:

    def __init__(self, input):
        self.input = input

    def __add__(self, other):
        return "Whatever ..."

    def __mul__(self, other):
        return myInteger(self.input * other)

    def __str__(self):
        return str(self.input)



x = myInteger(6)
print(x * 4)
print(x * (3 + 2))
print(x + 6)




"""
Problem #4 
(2 pts)

Implement a subclass of Polygon called Square which will overload
the constructor method __init__ so it takes only one argument 
(the side length). It will ALSO override method area() that computes 
the area using simpler notation.

NOTE: The method __init__ should make use of the superclass's __init__ 
so that NO variables need to be defined in the subclass.

HINT: area of a square is length squared

Be sure to demonstrate functionality by printing out both the 
perimter and area of your Square object.

mySquare = Square(2)
print(mySquare.perimeter())
print(mySquare.area())

Results:
8
4

"""
# Please enter your solution here
#

import math
class Polygon(object):
    def __init__(self, sides, length):
        "constructs a polygon with number of sides and length"
        self.sides = sides
        self.length = length

    def perimeter(self):
        "returns polygon perimeter"
        return self.sides * self.length

    def area(self):
        # create polygon area formula
        numerator = self.sides * self.length ** 2
        denominator = (4 * math.tan(math.pi/self.sides))
        return (numerator/denominator)

class Square(Polygon):
    def __init__(self, length):
        super().__init__(4, length)

    def area(self):
        return self.length ** 2


myPoly = Polygon(6, 1)
print(myPoly.perimeter())
print(myPoly.area())

mySquare = Square(2)
print(mySquare.perimeter())
print(mySquare.area())

"""
Problem #5 
(2 pts)

Implement a subclass of Polygon called Triangle which will overload
the constructor method __init__ so it takes only one argument 
(the side length). It will ALSO override method area() that computes 
the area using simpler notation.

NOTE: The method __init__ should make use of the superclass's __init__ 
so that NO variables need to be defined in the subclass.

HINT: area of a equilateral (perfect) triangle is the 
square root of 3 divided by 4, multiplied by the length squared

sqrt(3) / 4 * (length ** 2)

Be sure to demonstrate functionality by printing out both the 
perimter and area of your Triangle object.

myTriangle = Triangle(3)
print(myTriangle.perimeter())
print(myTriangle.area())

Results:
9
3.8971143170299736

"""
# Please enter your solution here
#

import math
class Polygon(object):
    def __init__(self, sides, length):
        "constructs a polygon with number of sides and length"
        self.sides = sides
        self.length = length

    def perimeter(self):
        "returns polygon perimeter"
        return self.sides * self.length

    def area(self):
        # create polygon area formula
        numerator = self.sides * self.length ** 2
        denominator = (4 * math.tan(math.pi/self.sides))
        return (numerator/denominator)

class Triangle(Polygon):
    def __init__(self, length):
        super().__init__(3, length)

    def area(self):
        return math.sqrt(3) / 4 * (self.length ** 2)

    
myPoly = Polygon(6, 1)
print(myPoly.perimeter())
print(myPoly.area())

myTriangle = Triangle(3)
print(myTriangle.perimeter())
print(myTriangle.area())



"""
BONUS PROBLEM
EXTRA CREDIT
(Bonus 1 pts)


The following code does not work - it does not function as expected...
Try to resolve any issues/bugs/problems you can...

hint: 
there are five known issues

Expected Output:

Name: Alice Smith, Salary: 2300
Annual Salary: 27600

Name: Bob Johnson, Salary: 4000
Department: Marketing
Annual Salary: 48000
Alice Smith received a 10 percent raise.
New salary: 2530.0

Name: Charlie Brown, Salary: 3000
Sales Target: 10000
Commision: 1200.0
Commision: 0

To get credit please comment (using # tags) EVERY issue/bug/problem you 
find as well as make the appropriate correction!

"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def displayInfo(self):
        print("Name: {0}, Salary: {1}".format(self.name, self.salary))

    def calculateSalary(self):
      return self.salary * 12

class Manager(Employee): # Added inheritance
    def __init__(self, name, salary, department):
        super().__init__(name, salary) # Removed self
        self.department = department

    def displayInfo(self):
        super().displayInfo() # Removed self
        print("Department: {0}".format(self.department))

    def giveRaise(self, employee, percentage):
        employee.salary *= (1 + percentage/100)
        message = "{0} received a {1} percent raise.\nNew salary: {2}"
        print(message.format(employee.name, percentage, employee.salary))
        #Changed to modify employee salary instead of manager

class SalesPerson(Employee):
    def __init__(self, name, salary, salesTarget):
        super().__init__(name, salary) # Added super
        self.salesTarget = salesTarget

    def displayInfo(self):
        Employee.displayInfo(self)
        print("Sales Target: {0}".format(self.salesTarget))

    def calculateCommission(self, salesMade):
      if salesMade >= self.salesTarget:
        return 0.1 * salesMade
      else:
        return 0


employee1 = Employee("Alice Smith", 2300)
manager1 = Manager("Bob Johnson", 4000, "Marketing")
salesperson1 = SalesPerson("Charlie Brown", 3000, 10000)

employee1.displayInfo()
print("Annual Salary: {0}".format(employee1.calculateSalary()))
print()
manager1.displayInfo()
print("Annual Salary: {0}".format(manager1.calculateSalary()))
manager1.giveRaise(employee1, 10)
print()
salesperson1.displayInfo()
print("Commision: {0}".format(salesperson1.calculateCommission(12000)))
print("Commision: {0}".format(salesperson1.calculateCommission(5000)))

"""
END
"""
