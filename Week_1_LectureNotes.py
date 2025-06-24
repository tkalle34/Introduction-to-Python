"""
PYTHON PROGRAMMING 1
LECTURE NOTES
WEEK ONE

author: Beemer, Bill
"""
#
"""
Welcome to Python 1 - Week One
"""
#
"""
This is an example of a multi line docstring.
You will find these are very useful in programming... a way to cummunicate information within your code.
The multi line docstring is created by three (3) consecutive 
single or double quotes ' or ".
"""
#
# you can also leave a comment anywhere in your file using a hashtag #.
# each line that you wish to comment, must have a hashtag, unlike the multi line docstring.
#
#

line1 = "Hello Python developer..."
line2 = "Welcome to the world of Python!"
print(line1)
print(line2)

"""
Chapter 2.1
"""

### Algebraic Expressions and Functions
# slide 8

# print(2 + 3)
# print(6 - 4)
# print(8 - 17)
# print(4 * 6)

# print(7 // 8)
# print(7 % 8)
# print(41 / 10)
# print(41 % 10)

# Examples of Floor and Modulus
# convert inches to inches and feet...
# print(64)
# print(64 // 12)
# print(64 % 12)

# print(4 ** 2) 
# print(abs(-16))
# print(min(4, 7, 8, 10, 3, -2))
# print(max(4, 7, 8, 10, 3, -2))

"""

Practice Problem 2.1 p18 in textbook
slide 9

Write Python algebraic expressions corresponding with the following statements:

b) The average age of Sara(age 23), Mark (age 19), and Fatima (age 31)
d) The remainder when 403 is divided by 73
g) The lowest price among the following prices: $34.99, 29.95, 31.50

"""
# Please enter your answers here
# 



"""
SOLUTION !!!
"""

# print((23 + 19 + 31)/3)
# print(403 % 73)
# print(min(34.99, 29.95, 31.50))


"""
Chapter 2.1
"""

### Boolean Expressions and Operators
# slide 15

# print(4 > 5)
# print(7 <= 10)
# print(15 < 15)
# print(15 == 15)

# # print(15 = 15)

# print(7 < 8)
# print(3 >= 3)
# print(3 >= 2)
# print(8 != 8)
# print(10 != 5)

# print(3 < 5 and 6 < 9)
# # print(3 < 5)
# # print(6 < 9)

# print(2 + 3 == 4 or 7 >= 6)
# # print(2 + 3 == 4)
# # print(7 >= 6)

# print(not (3 + 3 == 6))
# # print(3 + 3 == 6)

# print(5 == 5 and 9 <= 3)
# # print(5 == 5)
# # print(9 <= 3)

"""

Practice Problem 2.2 p19 in textbook
slide 16

Translate the following statements into Python Boolean expressions and evaluate them:

a) The sum of 2 and 2 is less than 4
c) The sum of 3 squared and 4 squared is equal to 25
e) 1387 is divisible by 19

"""
# Please enter your answers here
#


"""
SOLUTION !!!
"""

# print(2 + 2 < 4)
# print(3 ** 2 + 4 ** 2 == 25)
# print(1387 % 19 == 0)



"""
Chapter 2.1
"""

### Variables and Assignments
# slide 22

# x = 3					
# counter = 3 * x			
# print(x)				
# print(counter)

# print(15 == 15)
# # 15 = 15

# myVar = 15
# myVar == 15

# print(myVar)
# print(myVar == 15)


# myVar = 15
# print(myVar < 10)
# print(3 < 5 and 6 < 9)

# var1 = 3 < 5
# var2 = 6 < 9
# print(var1 and var2)

# var1 = 3 < 5
# print(var1)
# # foo = not var1
# # print(foo)


"""
Chapter 2.2
"""

### String Operators
# slide 26

# print("Python Rocks!")
# "Python Rocks!"

# x = "Monty"
# print(x)
# # print(x == "Monty")

# x = "Monty"
# y = "Python"
# print(x != y)
# # print(x == y)
# # print(x < y)

# x = "Monty"
# y = "Python"
# print(x + y)
# # print(x + " " + y)  
# # print(x * y)

# print(3 * "A")
# # print(2 * "Rabbit ")  # a space is after the "t"

# x = "Monty"
# print("y" in x)
# # print("g" in x)

# x = "Monty"
# y = "Python"
# print("th" in y)
# # print(len(x))

"""

Practice Problem 2.4 p25 in textbook
slide 27

Start by executing the assignment statements:

s1 = "ant"
s2 = "bat"
s3 = "cod"

Write Python expressions using s1, s2, s3 and 
operators + and * that evaluate to:

a) "ant bat cod"
c) "ant bat bat cod cod cod"
e) "batbatcod batbatcod batbatcod batbatcod batbatcod "

"""
# Please enter your answers here
#
# s1 = "ant"
# s2 = "bat"
# s3 = "cod"



"""
SOLUTION !!!
"""

# s1 = "ant"
# s2 = "bat"
# s3 = "cod"

# print(s1 + " " + s2 + " " + s3)
# print(s1 + " " + 2 * (s2 + " ") + 2 * (s3 + " ") + s3)
# print(5 * (2 * s2 + s3 + " "))



"""
Chapter 2.2
"""

### Indexing Operator
# slide 31

# x = "monty"
# print(x[0])  ## 0 is zero
# print(x[1])
# print(x[4])

# x = "monty"
# print(x[-5])            
# print(x[-4])
# print(x[-1]) ## always last


"""
Chapter 2.3
"""

### List Operators
# slide 35

# coins = ["penny", "nickel", "dime", "quarter"]
# print(coins)

# print(coins[1])
# print(coins[3])
# # print(coins[-2])
# # print(len(coins))

# coins = ["penny", "nickel", "dime", "quarter"]

# print(coins + coins)
# print(coins * 2)

# # print("dollar" in coins)
# # print("dime" in coins)

# myGrades = [95, 100, 88, 92, 98]
# print(myGrades)

# print(min(myGrades))
# print(max(myGrades))
# # print(sum(myGrades))

# myGrades = [95, 100, 88, 92, 98]

# myGrades.sort()
# print(myGrades)

# print(min(myGrades))
# print(max(myGrades))

"""
Chapter 2.3
"""

### Lists are mutable, Strings are not
# slide 36

# pets = ["dog", "fish", "cat"]
# print(pets)

# pets[1] = "goldfish"
# print(pets)

# myPet = "bat"
# print(myPet)

# myPet[0] = "c"
# print(myPet)

"""
Chapter 2.3
"""

### Tuples or "Immutable Lists"
# slide 42

# myList = ["pickle", "lettuce", "tomato"]    ## note the square brackets [ ] 
# myList[1] = "onion"
# print(myList)

# # print(myList[1])

# myTuple = ("cheese", "bacon", "avocado")    ## note the parentheses ( ) 
# # myTuple[1] = "mayo"
# print(myTuple)

# # print(myTuple[1])

"""
Chapter 2.3
"""

### List and Tuple Methods
# slide 45

# cards = ["ace", "four", "six"]
# cards.append("jack")
# print(cards)

# cards.append("ace")
# print(cards)

# print(cards.count("ace")) 

# cards.remove("ace")
# print(cards)


# print(cards)
# cards.reverse()
# print(cards)

# cards.pop()
# print(cards)

# print(cards.pop())
# print(cards)


"""

Practice Problem 2.7 p33 in textbook
slide 46

Start by executing the assignment statement:

grades = [9, 7, 7, 10, 3, 9, 6, 6, 2]

Write the following:

a) An expression that evaluates to the number of 7 grades
c) An expression that evaluates to the maximum grade
e) An expression that evaluates to the average grade

"""
# Please enter your answers here
#
# grades = [9, 7, 7, 10, 3, 9, 6, 6, 2]


"""
SOLUTION !!!
"""


# grades = [9, 7, 7, 10, 3, 9, 6, 6, 2]

# print(grades.count(7))
# print(max(grades))
# print(sum(grades) / len(grades))


"""
Chapter 2.4
"""

### Object Type
# slide 52

# print(type(42))
# print(type(3.12))

# print(type("Python Rocks!"))
# print(type(False))
# print(type(["cat", "dog", "fish"]))

# x = 2 ** 1024
# print(x)

# y = 2.0 ** 1024
# print(y)


"""
Chapter 2.4
"""

### Valid Values for Number Types
# slide 58

# x = 3         ## implicit
# x = int(3)    ## explicit

# print(True + 2) ## implicit conversion of True to 1
# print(4 + 0.25) ## implicit conversion of 4 to 4.0

# print(int(4.7))          
# print(float(3))          
# # print(int("3.4"))

# print(float("3.4"))     
# print(str(3.12))


"""
Chapter 2.5
"""

### Module math
# slide 70

# import math

# print(math.sqrt(4))

# # print(sqrt(4))

## best in IDLE
# help(math)

# print(math.cos(0))
# print(math.log(8))

# print(math.pi)

"""

Practice Problem 2.10 p42 in textbook
slide 71

Start by executing the import module statement:

import math

a) The length of the hypotenuse in a right triangle 
whose other two sides have lengths a and b
hint: Pythagoras
c) The area of a disk of radius a
hint: Area of a circle

"""
# Please enter your answers here
#
# import math
# a = 3 # side of right triangle
# b = 4 # other side of right triangle

# radius = 5 # radius of disk




"""
SOLUTION !!!
"""


# import math

# a = 3 # side of right triangle
# b = 4 # other side of right triangle

# print((math.sqrt(a ** 2 + b ** 2)))

# radius = 5 # radius of disk

# print(math.pi * radius ** 2)


"""
Chapter 3.1
"""

### Our First Python Program
# slide 75


# line1 = "Hello Python developer..."
# line2 = "Welcome to the world of Python!"
# print(line1)
# print(line2)


"""
Chapter 3.1
"""

### Interactive Input with input()
# slide 81

# first = input("Enter your first name: ")
# print(first)

# first = input("Enter your first name: ")
# last = input("Enter your last name: ")
# line1 = "Hello " + first + " " + last + "..."
# print(line1)
# print("Welcome to the world of Python!")


"""
Chapter 3.1
"""

### Function Eval()
# slide 82

# x = eval(input('Enter x : '))
# print(type(x))

# # print("Does x == " + str(x) + " : " + str(x == x))
# # print("Does x == '" + str(x) + "' : " + str(x == str(x)))


# AVOID Using Eval()

# x = input('Enter x : ')
# print(type(x))

# # print("Does x == " + x + " : " + str(x == int(x)))
# # print("Does x == '" + x + "' : " + str(x == x))

"""

Practice Problem
slide 83

Write a program that:

Requests the user's name
Requests the user's age
Computes the user's age one year from now and prints the message shown

Enter your name: Wilson
Enter your age: 42
Wilson, you will be 43 next year!
"""
# Please enter your answers here
#


"""
SOLUTION !!!
"""



# name = input("Enter your name: ")
# age = input("Enter your age: ")
# line1 = name + ", you will be " + str(int(age) + 1) + " next year!"
# print(line1)


"""
END
"""

