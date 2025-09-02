"""
PYTHON PROGRAMMING 1
HOMEWORK
WEEK TEN

author: Taran Kalle
** be sure to RENAME the file <Last><First>_Week_10_Homework.py
** example: BeemerBill_Week_10_Homework.py

IGNORE THE SYNTAX WARNING
Its from commented out example code for some reason
"""
#
"""
Complete the following problems
"""
#
"""
Problem #1
(2 pts)

Use recursive thinking to implement recursive function sumDigits()
that takes in a positive integer as input and prints the total
of all the individual digits. 
e.g. 431 would result in 8 (4 + 3 + 1 = 8)

sumDigits(431)
8

Please include three (3) demonstrations of the function working
as expected.

"""
# Please enter your answer here
#

def sumDigits(n: int):

    if n < 10:
        return n
    else:
        return (n % 10) + sumDigits(n // 10)

print("sumDigits(431):", sumDigits(431))
print("sumDigits(2057):", sumDigits(2057))
print("sumDigits(9999):", sumDigits(9999))
"""
Problem #2
(2 pts)

Write a recursive method timer() that takes one nonnegative 
integer as input and then using the module time and 
its method sleep() to pause for one second ( time.sleep(1) )
between printing the consecutive integers down to 1, 
at which time, when the value reaches 0 print "Time's Up!!!"

timer(5)
5 4 3 2 1 Time's Up!!!

Hint: to match the print out above, be sure to remove 
the default end of line /n from the print statement and use this 
code snippet:

    print(n, end=" ", flush=True)

Please indlude one (1) demonstration of the function working
as expected when 5 is entered as the input variable.


"""
# Please enter your answer here
# 

import time

def timer(n:int):
    if n == 0:
        print("Time's Up!!!")
    else:
        print(n, end=" ", flush=True)
        timer(n-1)

timer(5)
"""
Problem #3
(2 pts)

Write a function called search() that locates the index of a target
word (type string) from a list of words.  

You must use the binary 
search technique learned in class and recursion (see lecture notes)
to get full credit for the problem.

list of words to use:
myList = ["apple", "book", "desk", "pen", "cat", "dog", "tree", 
"house", "car", "phone", "computer", "laptop", "keyboard", "mouse", 
"chair", "table", "door", "window", "wall", "floor"]

target = "door"

HINT: you will need to sort the list prior to calling search()

"""
# Please enter your solutions here
# 

myList = ["apple", "book", "desk", "pen", "cat", "dog", "tree",
"house", "car", "phone", "computer", "laptop", "keyboard", "mouse",
"chair", "table", "door", "window", "wall", "floor"]

def search(srcList, target, i, j):

    middle = (i + j) // 2
    if srcList[middle] == target:
        return print(middle)
    elif target < srcList[middle]:
        return search(srcList, target, i, middle-1)
    else:
        return search(srcList, target, middle+1, j)

myList.sort()
target = "door"
search(myList, target, 0, len(myList)-1)

"""
Problem #4
(2 pts) 

Using regular expression operators to come up with expressions 
that produce the provided results.

To receive full credit you should ONLY use regular expression
operators. (NOT regular expression special sequences.)

myString = "net next nest neck neet w00t newt neeet"

a) ['next', 'nest', 'neet', 'newt']
b) ['nest', 'newt']
c) ['w00t', 'neeet']
d) ['net', 'neet', 'neeet']
e) ['net', 'neet']

example:

myString = "net next nest neck neet w00t newt neeet"
match = re.findall("w00t", myString)
print(match)

results:

['w00t']

"""
# Please enter your solutions here
#

import re

myString = "net next nest neck neet w00t newt neeet"

match = re.findall(r"ne[xsew]t", myString)
print(match)
match = re.findall(r"ne[sw]t", myString)
print(match)
match = re.findall(r"(w00t|neeet)", myString)
print(match)
match = re.findall(r"nee*t", myString)
print(match)
match = re.findall(r"nee?t", myString)
print(match)


"""
Problem #5
(2 pts) 

Using regular expression to come up with expressions 
that produce the provided results.

myOrder = "Order number: 12345"

a) ['Order', 'number', '12345']
b) [' ', ':', ' ']

myUser = "User: bill@2025!"

c) ['U', 's', 'e', 'r', ':', 'b', 'i', 'l', 'l', '@', '2', '0', '2', '5', '!']
d) [':', ' ', '@', '!']
e) ['2025']


example:

myOrder = "Order number: 12345"
match = re.findall("\d+", myOrder)
print(match)

results:

['12345']

"""
# Please enter your solution here
#

import re

myOrder = "Order number: 12345"
myUser = "User: bill@2025!"

match = re.findall(r"\w+", myOrder)
print(match)
match = re.findall(r"[\s:]", myOrder)
print(match)
match = re.findall(r".", myUser)
print(match)
match = re.findall(r"[:\s@!]", myUser)
print(match)
match = re.findall(r"\d+", myUser)
print(match)


"""
BONUS PROBLEM
EXTRA CREDIT
(Bonus 1 pts)

The following code does not work - it does not function as expected...
Try to resolve any issues/bugs/problems you can...

Please insert comments for every issue/bug/problem you uncover
and solve!!

hint: 
there are five known issues


Expected Output:

Julian
Sociable
Smiling
The employees feel all warm and fuzzy.
Bob
Negative
The employees feel cheated and start plotting.
The team is shocked by the yelling.

To get credit please comment (using # tags) EVERY issue/bug/problem you 
find as well as make the appropriate correction!

"""

class Boss(object):
    def __init__(self, name, attitude, behavior, face):
        self.name = name
        self.attitude = attitude
        self.behavior = behavior
        self.face = face

    def getAttitude(self):
        return self.attitude

    def getBehavior(self):
        return self.behavior

    def getFace(self): #Missing Self
        return self.face

class GoodBoss(Boss):
    def __init__(self, name, attitude, behavior, face): #Missing face
        super().__init__(name, attitude, behavior, face)
        
    def nurtureTalent(self):
        print("The employees feel all warm and fuzzy.")
    
    def encourage(self):
        print("The team cheers then gets back to work.")

class BadBoss(Boss):
    def __init__(self, name, attitude, behavior, face):
        super().__init__(name, attitude, behavior, face) #Missing name
        
    def hoardPraise(self):
        print("The employees feel cheated and start plotting.")
    
    def yell(self):
        print("The team is shocked by the yelling.")

julian = GoodBoss("Julian", "Positive", "Sociable", "Smiling")
bob = BadBoss("Bob", "Negative", "Angry", "Scowling")# Extra argument

print(julian.name)
print(julian.getBehavior())
print(julian.getFace())
julian.nurtureTalent()
print(bob.name)
print(bob.getAttitude())
bob.hoardPraise()
bob.yell() # Print is in the method


"""
END
"""
