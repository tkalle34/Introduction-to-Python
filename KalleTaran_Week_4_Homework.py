"""
PYTHON PROGRAMMING 1
HOMEWORK
WEEK FOUR

author: <YOUR NAME HERE>
** be sure to RENAME the file <Last><First>_Week_4_Homework.py
** example: BeemerBill_Week_4_Homework.py
"""
#
"""
Complete the following problems
"""
#
"""
Problem #1
(2 pts)

Write function pay() that takes as input an hourly wage and the number
of hours an employee worked in the last week. The function should
computer and return the employee's pay.

Overtime work should be paid in this way:
Any hours beyond 40 but less than or equal to 60 should be paid 
at 1.5 times the regular hourly wage. 
Any hours beyond 60 should be paid at 2 times the regular hourly wage.

pay(10, 35) # results should be 350
pay(10, 45) # results should be 475.0
pay(10, 61) # results should be 720.0

"""
# Please enter your answers here
# 
def pay(hourlyWage, hoursWorked):
    if hoursWorked <= 40:
        total_pay = hourlyWage * hoursWorked
    elif hoursWorked <= 60:
        regular_pay = hourlyWage * 40
        overtime_pay = (hoursWorked - 40) * (hourlyWage * 1.5)
        total_pay = regular_pay + overtime_pay
    else:
        regular_pay = hourlyWage * 40
        overtime_pay = 20 * (hourlyWage * 1.5)
        double_overtime_pay = (hoursWorked - 60) * (hourlyWage * 2)
        total_pay = regular_pay + overtime_pay + double_overtime_pay

    return total_pay

print(pay(10,35))
print(pay(10,45))
print(pay(10,61))

"""
Problem #2
(2 pts)

Write function doubles() that takes as input a list of integers
and prints the integers in the list that are exactly twice 
the previous integer in the list, one per line.

hint: item[index] : if this is the current index 
than item[index - 1] is the previous index

myList = [3, 0, 1, 2, 3, 6, 2, 4, 5, 6, 5]

doubles(myList)
# results should be...
2
6
4

"""
# Please enter your answers here
# 
myList = [3, 0, 1, 2, 3, 6, 2, 4, 5, 6, 5]

def doubles(intList):
    for i in range(1,len(intList)-1):
        if intList[i] == 2 * intList[i-1]:
            print (intList[i])

doubles(myList)



"""
Problem #3
(2 pts)

Implement the function pair() that takes as input two lists 
of integers and one integer n and prints the pairs of integers,
one from the first input list and the other from the second
input list, that add up to n.  

The pair and the result should be printed in this format: 
<int> + <int> = <int>

firstDice = [1, 5, 2, 4, 4]
secondDice = [4, 6, 3, 2, 1]
winner = 7
pair(firstDice, secondDice, winner)

# results should be...
1 + 6 = 7
5 + 2 = 7
4 + 3 = 7
4 + 3 = 7

"""
# Please enter your answers here
# 
firstDice = [1, 5, 2, 4, 4]
secondDice = [4, 6, 3, 2, 1]
winner = 7

import random # I'm not sure why you are importing random here

def pair(list1:list, list2:list, n:int):
    for i in list1:
        for j in list2:
            if i+j == n:
                print("{0} + {1} = {2}".format(i,j,n))

pair(firstDice,secondDice,winner)

"""
Problem #4 
(2 pts)

Implement the function noEmpty() that takes as input a 
two-dimensional list (a list of lists) that represent all
the pixels in a small image and check for the pixel value
of 0 (an "empty" pixel), change the 0 value to 2 and then
print the entire "table".

pixels = [[2, 5, 4, 0, 1], [0, 3, 2, 0, 3], [3, 0, 3, 7, 0], [0, 0, 9, 7, 1]]
noEmpty(pixels)

# results should be ...
2 5 4 2 1
2 3 2 2 3 
3 2 3 7 2
2 2 9 7 1

"""
# Please enter your answers here
# 
pixels = [[2, 5, 4, 0, 1], [0, 3, 2, 0, 3], [3, 0, 3, 7, 0], [0, 0, 9, 7, 1]]

def noEmpty(image):
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] == 0:
                image[i][j] = 2
            print(image[i][j], end = " ")
        print("")

noEmpty(pixels)
"""
Problem #5
(2 pts)

Implement a function called advantageRoll() that takes an integer
input that represents the number of faces on a single die (common 
dice are 4, 6, 8, 10, 12, 20).  The function should generate two
random integers based on the die size and display the highest.
If the highest integer matches the number of faces input, print
the following line: "Critical hit!"

Because random is being used, the examples below are just that, 
examples of possible outcomes - In order to TEST your code, I would
suggest running the code over and over

advantageRoll(20)
# could possibly result in
18

advantageRoll(20)
# or possibly result in
20
Critical hit!

advantageRoll(6)
# could possibly result in
4

advantageRoll(6)
# or possibly result in
6
Critical hit!

"""
# Please enter your answers here
# 
import random

def advantageRoll(diceSize):
    roll1 = random.randint(1, diceSize)
    roll2 = random.randint(1, diceSize)
    if roll1 >= roll2:
        print(roll1)
        if roll1 == diceSize:
            print("Critical hit!")
    else:
        print(roll2)
        if roll2 == diceSize:
            print("Critical hit!")

advantageRoll(20)


"""
BONUS PROBLEM
EXTRA CREDIT
(Bonus 1 pts)

The following code does not work - it does not function as expected...
Try to resolve any issues/bugs/problems you can...

hint: 
there are five known issues
look at the 'correct result' section carefully

correct result:

(for a list of commands type 'help')
What is your command? asdf
I don't understand that command!
What is your command? help
['jump', 'walk', 'run', 'rest', 'stay', 'help']
What is your command? walk
You entered the following command: walk
What is your command? run
You entered the following command: run
What is your command? 

To get credit please comment (using # tags) EVERY issue/bug/problem you 
find as well as make the appropriate correction!

"""

commands = ["jump", "walk", "run", "rest", "stay", "help"] # "stay" not "kick"

commandEntered = True # Assignment not equivalence
print("(for a list of commands type 'help')") # Moved outside while statement
while commandEntered:
    command = input("What is your command? ")
    if command == "":
        commandEntered = False
    elif command == "help": # Equivalence not assignment
        print(commands)
    elif command in commands: # No brackets
        print("You entered the following command: {0}".format(command))
    else:
        print("I don't understand that command!")
        # Should not set commandEntered to False

"""
END
"""
