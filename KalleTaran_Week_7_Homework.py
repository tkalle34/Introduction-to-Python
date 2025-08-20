"""
PYTHON PROGRAMMING 1
HOMEWORK
WEEK SEVEN

author: Taran Kalle
** be sure to RENAME the file <Last><First>_Week_7_Homework.py
** example: BeemerBill_Week_7_Homework.py
"""
#
"""
Complete the following problems
"""
#
"""
Problem #1 part a
(1 pts)

Describe in words what is the problem with this chunk of code?

print(calc(3))

def calc(x):
    return 2 * x + 1

"""
# print(calc(3))
#
# def calc(x):
#     return 2 * x + 1

# Please enter your answer here
# (be sure to comment your answer out)

# Calc is defined after use

"""
Problem #1 part b
(1 pts)

Describe in words what is the problem with this chunk of code?

def myFunction(x):
    y = 6 
    return y * x + 2

print("x : {0}".format(x))
print("y : {0}".format(y))

print(myFunction(2))

"""
# def myFunction(x):
#     y = 6 
#     return y * x + 2

# print("x : {0}".format(x))
# print("y : {0}".format(y))

# print(myFunction(2))

# Please enter your answer here
# (be sure to comment your answer out)

# x and y don't have global scope so cant be used in the print statements

"""
Problem #2
(2 pts)

Run the following code using the function call subTwo(5)

Describe in words (and use line numbers for clarity) what
happens at EVERY step of the program in SEQUENCE.

def frac(n):
    print("frac")
    print(1/n)
    print(n)

def subOne(n):
    print("subOne")
    frac(n - 1)
    print(n)

def subTwo(n):
    print("subTwo")
    subOne(n - 2) 
    print(n)


subTwo(5)

"""
def frac(n):
    print("frac")
    print(1/n)
    print(n)

def subOne(n):
    print("subOne")
    frac(n - 1)
    print(n)

def subTwo(n):
    print("subTwo")
    subOne(n - 2)
    print(n)

subTwo(5)

# Please enter your answer here
# (be sure to comment your answer out)

# def frac is defined
# def subOne is defined
# def subTwo is defined
# subTwo is called and begins executing
# subOne is called within SubTwo and begins executing
# frac is called within SubOne and executes
# subOne finishes executing
# subTwo finishes executing

"""
Problem #3
(2 pts)

Create a global variable balance and set its value to 100.
Create three functions atmWithdraw, checkWithdraw, and deposit.
Each function accepts only ONE input, a dollar amount.
The atmWithdrawal has a local variable atmFee set to 3 and
this function reduces the balance by input as well as the fee.
The checkWithdraw function reduces the balance by the input.
The depost function increases the balance by the input.
Use the provided function calls and print statements
to verify your solution.

If the following code is run:

print("Current Balance : {0}".format(balance))
checkWithdraw(25)
print("Current Balance : {0}".format(balance))
atmWithdraw(40)
print("Current Balance : {0}".format(balance))
deposit(100)
print("Current Balance : {0}".format(balance))

The result printed in the terminal should be:

Current Balance : 100
Current Balance : 75
Current Balance : 32
Current Balance : 132

"""
# Please enter your solution here
# 

BALANCE = 100
def atmWithdraw(amount):
    atmFee = 3
    global BALANCE
    BALANCE -= (amount+atmFee)

def checkWithdraw(amount):
    global BALANCE
    BALANCE -= amount

def deposit(amount):
    global BALANCE
    BALANCE += amount

# # use the following to verify your answer
print("Current Balance : {0}".format(BALANCE))
checkWithdraw(25)
print("Current Balance : {0}".format(BALANCE))
atmWithdraw(40)
print("Current Balance : {0}".format(BALANCE))
deposit(100)
print("Current Balance : {0}".format(BALANCE))


"""
Problem #4 
(2 pts)

Create a function called inValues() that asks the user to input 
a set of floating point numbers one at a time.  When the user
enters a value that is NOT a number, give them a second chance to enter
a valid value.
If a user makes two mistakes in a row (e.g. enters a value that is NOT a 
number) quit the function.
If a user enters three valid values, print the sum of the correctly
entered values.
Use exception handling to detect improper user inputs.

The following are two examples of running the program:

The first shows an example of a user entering one mistake, but completing 
the valid entry of three values followed by the function printing the 
sum of all the values.

The second shows a user entering non-valid values TWICE as mistakes 
and therefore triggering the quit statment, and quiting the function.

Please enter a number: 4.75
Please enter a number: 2,2,5
Error. Please re-enter the value...
Please enter a number: 2.25
Please enter a number: 1.00
8.0

Please enter a number: 3.4
Please enter a number: 2,,5
Error. Please re-enter the value...
Please enter a number: 2,5
Two errors in a row. Quitting...

"""
# Please enter your solution here
#

def inValues():
    values = []
    consecutive_errors = 0

    while len(values) < 3:
        try:
            user_input = input("Please enter a number: ")
            num = float(user_input)
            values.append(num)
            consecutive_errors = 0
        except ValueError:
            consecutive_errors += 1
            if consecutive_errors == 1:
                print("Error. Please re-enter the value...")
            elif consecutive_errors == 2:
                print("Two errors in a row. Quitting...")
                return

    print(sum(values))

# inValues()

"""
Problem #5 

Take the following commands and re-write them using the 
following notation learned in Chapter 7.5:

class.method(instance, arg1, arg2, . . . )

example:

myList.sort()

solution:

list.sort(myList)

"""
# # Please enter your solution here
# #
myString = "hello"
myList = [9, 1, 8, 2, 7, 3]
myDict = {"Apollo": 40, "Athena": 35, "Hera": 71}

# 1
str.upper(myString)

# 2
str.find(myString,"e")

# 3
str.replace(myString,"h", "j")

# 4
str.split(myString,"e")

# 5
list.insert(myList,8, 2)

# 6
list.count(myList,8)

# 7
list.append(myList,5)

# 8
dict.get(myDict,"Apollo")

# 9
dict.keys(myDict)

# 10
dict.pop(myDict,"Hera")


"""
BONUS PROBLEM
EXTRA CREDIT
(Bonus 1 pts)

TWO PART PROBLEM!!

== Part One == 
THe following code works as expected.

BUT...

It needs to be rewritten to be more user friendly, cleaner
and allow for possible future features to be implemented.

Re-write the following code so that instead of checking
if the file name exists in the text file and THEN generating
a print statement if it does NOT, collect ALL missing file names into two 
lists (missingPost and missingDelivery) first!
THEN loop through the lists to generate the print statements.

== Part Two == 

AFTER you complete the re-write in Part One, please describe WHY this change might be
considered more user friendly, cleaner and allow for future features.
(Be sure to comment out all your text)

NOTE: this bonus question requires the BonusCapture.txt, BonusPost.txt,
and BonusDelivery.txt files to be downloaded from Canvas and 
placed in the same working directory as this homework assignment

The OUTPUT should be as follows AFTER you re-write the code:

Needs Post : lastofus/post/2022_04_02/Hero_MoveTree_Run_180_tk001.post
Needs Post : lastofus/post/2022_04_02/Hero_MoveTree_Walk_Pistol_000_tk001.post
Needs Post : lastofus/post/2022_04_02/Enemy_MoveTree_Walk_Pistol_000_tk001.post
Needs Delivery : lastofus/delivery/2022_04_02/Hero_MoveTree_Walk_045_tk001.delivery
Needs Delivery : lastofus/delivery/2022_04_02/Enemy_MoveTree_Run_135_tk001.delivery
Needs Delivery : lastofus/delivery/2022_04_02/Enemy_MoveTree_Walk_180_tk001.delivery
Needs Delivery : lastofus/delivery/2022_04_02/Hero_MoveTree_Walk_Pistol_045_tk001.delivery
"""
# # Please enter your Part One solution below
# #
# # functions to notify user of missing files
# def needsPost(filePath):
#     print("Needs Post : {0}".format(filePath))

# def needsDelivery(filePath):
#     print("Needs Delivery : {0}".format(filePath))

# # gather all captured shots
# shotsList = []
# with open("BonusCapture.txt", "r") as shotlist:
#     lines = shotlist.readlines()
#     for line in lines:
#         shotsList.append(line.strip())

# # gather all post shots
# postShots = []
# with open("BonusPost.txt", "r") as postlist:
#     lines = postlist.readlines()
#     for line in lines:
#         postShots.append(line.strip())

# # gather all delivered shots
# deliveryShots = []
# with open("BonusDelivery.txt", "r") as deliverylist:
#     lines = deliverylist.readlines()
#     for line in lines:
#         deliveryShots.append(line.strip())

# # compare all captured shots with post and delivered
# for shot in shotsList:
#     filePathList = shot.split("/")
#     # generate post file name and path
#     postFileName = "{0}.{1}".format(filePathList[-1].strip(), "post")
#     postFilePath = "{0}/post/{1}/{2}".format(filePathList[0], 
#                                             filePathList[2], 
#                                             postFileName)
#     # if post does not exist, notify user
#     if postFilePath not in postShots:
#         needsPost(postFilePath)

#     # generate delivery file name and path
#     deliveryFileName = "{0}.{1}".format(filePathList[-1], "delivery")
#     deliveryFilePath = "{0}/delivery/{1}/{2}".format(filePathList[0], 
#                                             filePathList[2], 
#                                             deliveryFileName)
#     # if delivery does not exist, notify user
#     if deliveryFilePath not in deliveryShots:
#         needsDelivery(deliveryFilePath)


# Please enter your Part Two written answer here
#

def needsPost(filePath: str) -> None:
    print(f"Needs Post : {filePath}")

def needsDelivery(filePath: str) -> None:
    print(f"Needs Delivery : {filePath}")


def load_file_to_list(filename: str) -> list[str]:
    with open(filename, "r") as file:
        return [line.strip() for line in file]


shotsList = load_file_to_list("BonusCapture.txt")
postShots = load_file_to_list("BonusPost.txt")
deliveryShots = load_file_to_list("BonusDelivery.txt")


missingPost = []
missingDelivery = []

for shot in shotsList:
    filePathList = shot.split("/")

    postFileName = f"{filePathList[-1]}.post"
    postFilePath = f"{filePathList[0]}/post/{filePathList[2]}/{postFileName}"
    if postFilePath not in postShots:
        missingPost.append(postFilePath)

    deliveryFileName = f"{filePathList[-1]}.delivery"
    deliveryFilePath = (f"{filePathList[0]}/delivery/{filePathList[2]}/"
                        f"{deliveryFileName}")
    if deliveryFilePath not in deliveryShots:
        missingDelivery.append(deliveryFilePath)

for postFile in missingPost:
    needsPost(postFile)

for deliveryFile in missingDelivery:
    needsDelivery(deliveryFile)

'''
By grouping all missing “post” files together before listing the missing “delivery”
 files, this version makes the output easier to follow and more logically ordered, 
 avoiding the confusion of intermingled results. The code is made cleaner through the 
 removal of repetitive file-reading logic, achieved by introducing a single helper 
 function, as well as through the use of distinct sections for functions, 
 data loading, processing, and output. The modular layout also means that additional 
 categories of missing files can be incorporated with minimal disruption to the 
 existing structure.
'''

"""
END
"""
