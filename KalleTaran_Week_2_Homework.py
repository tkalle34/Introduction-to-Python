"""
PYTHON PROGRAMMING 1
HOMEWORK
WEEK TWO

author: <YOUR NAME HERE>
** be sure to RENAME the file <Last><First>_Week_2_Homework.py
** example: BeemerBill_Week_2_Homework.py
"""
#
"""
Complete the following problems
"""
#
"""
Problem #1
(2 pts)

Implement a program that accepts a list of names (provided)
and prints only those names that start with only certain 
letters (provided).

(a)
letters A - L
nameList1 = ["Ellie", "Steve", "Sam", "Owen", "Gavin"]
result:
Ellie
Gavin

(b)
letters M - Z
nameList2 = ["Chris", "Zed", "Mary", "Laura", "Oscar"]

(c)
letters K - P
nameList3 = ["Luis", "Zoe", "Nancy", "Sonita", "Adrien"]

HINT: remember that letters have values similar to integers 
e.g. 3 < 7, "A" < "B"
"""
# Please enter your answers here
# 
nameList1 = ["Ellie", "Steve", "Sam", "Owen", "Gavin"]
nameList2 = ["Chris", "Zed", "Mary", "Laura", "Oscar"]
nameList3 = ["Luis", "Zoe", "Nancy", "Sonita", "Adrien"]

# Problem 1.a
for i in nameList1:
    if i[0] <= "L":
        print(i)

# Problem 1.b
for i in nameList2:
    if i[0] >= "M":
        print(i)

# Problem 1.c
for i in nameList3:
    if "K" <= i[0] <= "P":
        print(i)


"""
Problem #2
(2 pts)

Implement a program that accepts a four digit integer
and prints its digits in order. 

(Assume it is ALWAYS a FOUR digit POSITIVE integer)

The program can NOT treat the integer as a string!!

It must process the integer as an integer using standard 
arithmetic operations (+, *, -, //, %, etc)

(a)
num1 = 6541
result:
6
5
4
1

(b)
num2 = 3289

HINT:
remember modulus and remainder operations from week 1!
"""
# Please enter your answers here
# 
num1 = 6541
num2 = 3289

# Problem 2.a
print(num1//1000)
print((num1//100)%10)
print((num1//10)%10)
print(num1%10)

# Problem 2.b
print(num2//1000)
print((num2//100)%10)
print((num2//10)%10)
print(num2%10)


"""
Problem #3
(2 pts)

Implement a function called pay() that accepts two arguments:
an hourly wage and the number of hours
The function should return (or print) the total pay.
Any hours worked beyond 40 hours is considered overtime
and each hour past 40 should be paid at 1.5 times the regular pay

HINT:
use a conditional execution for multiple conditions

(a)
pay(10, 35)
result: 
350

(b)
pay(10, 45)
result: 
475.0

(c)
pay(12, 50)

(d)
pay(16, 25)


"""
# Please enter your answers here
# 
def pay(wage, hours):
    payAmount = wage*hours
    if hours > 40:
        payAmount = payAmount + ((hours-40)*(wage/2))
    print(payAmount)

# Problem 3.a
pay(10,35)

# Problem 3.b
pay(10, 45)

# Problem 3.c
pay(12, 50)

# Problem 3.d
pay(16, 25)

"""
Problem #4
(2 pts)

Write the for loops that use the function range() 
and print the following sequences...

hint:
for i in range(4):
    print(i, end = " ")
print()

0 1 2 3


(a) 0 1
(b) 0
(c) 3 4 5 6
(d) 1
(e) 0 3
(f) 5 9 13 17 21

"""
# Please enter your answers here
#

# Problem 4.a
for i in range(2):
    print(i, end = " ")
print()

# Problem 4.b
for i in range(1):
    print(i, end = " ")
print()

# Problem 4.c
for i in range(4):
    print(i+3, end = " ")
print()

# Problem 4.d
for i in range(1):
    print(i+1, end = " ")
print()

# Problem 4.e
for i in range(2):
    print(i*3, end = " ")
print()

# Problem 4.f
for i in range(5, 25, 4):
    print(i, end = " ")
print()

"""
Problem #5
(2 pts)

Implement a function called getAverage() that accepts a list of 
a list of grades.  Yes, a list of lists!
Each list of grades represents the grades of an individual student.
The list contains multiple students grade lists.
You can assume that a list of grades is NOT empty,
but you can NOT assume that each student has the same number of grades.

HINT:
remember list functions from week 1!

studentGrades = [[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]]
result:
90.0
60.0
87.0
11.0

"""
# Please enter your answers here
# 
studentGrades = [[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]]

def getAverage(grades):
    for i in grades:
        total = 0
        for j in i:
            total = total + j
        print(total/len(i))

getAverage(studentGrades)


"""
BONUS PROBLEM
EXTRA CREDIT
(Bonus 1 pts)

The following code does not work - it does not function as expected...
Try to resolve any issues/bugs/problems you can...

hint: 
there are four known issues

correct result:
['Stanley', 10, 'fight']
Stanley hit points are currently 8
['Stanley', 8, 'fight']

To get credit please comment (using # tags) EVERY issue/bug/problem 
you find AND make the appropriate correction!

"""

## character (name, hitpoints, current status)
charList = ["Stanley", 10, "fight"] # Should be list, not tuple
print(charList)
def reduceHitPoints(char):
    """
    reduces the hit points of a character
    if character is engaged in a fight

    @param char: list[] list of a character stats
    """
    damage = 2 # Should be assignment variable not equivalence
    if char[2] == "fight": # Should check third element, not second
        char[1] = char[1] - damage
    print(char[0] + "'s hit points are currently " + str(char[1])) # Double quotes instead of single

## reduce hit points of character
reduceHitPoints(charList)
## print character with reduced hit points
print(charList)

"""
END
"""
