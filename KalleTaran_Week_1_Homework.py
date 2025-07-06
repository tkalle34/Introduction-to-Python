"""
PYTHON PROGRAMMING 1
HOMEWORK
WEEK ONE

author: <Taran Kalle>
** be sure to RENAME the file <Last><First>_Week_1_Homework.py
** example: BeemerBill_Week_1_Homework.py
"""
#
"""
Complete the following problems
"""
#
"""
Problem #1
(1 pts)

Write Python expressions corresponding to the statements, and print the results:
1) The sum of negative integers -7 through -1
2) The average age of a kid at a summer camp given that there are
    17 kids that are 9 years old
    24 kids that are 10 years old
    21 kids that are 11 years old
    and 27 kids are 12 years old.
3) 2 to the power of -20
4) The number of times 61 goes into 4356
5) The remainder when 4365 is divided by 61

Example:

Q: The absolute value of -16
A: print(abs(-16))

"""
# Please enter your answers here
# 
# The absolute value of -16
# print(abs(-16))
import math

# Problem 1.1
x = 0
for y in range(-7,-1):
    x = x+y
print(x)

# Problem 1.2
print((17*9+24*10+21*11+27*12)/(17+24+21+27))

# Problem 1.3
print(2**-20)

# Problem 1.4
print(4356//61)

# Problem 1.5
print(4356%61)

"""
Problem #2
(1 pts)

Given the following variable myString, 

    myString = "goodbye"

write a BOOLEAN expression that checks the following, and prints the results:

1) The seventh character of myString is "g" 
    -- should evaluate to False
2) The first two characters fo myString are "g" and "a" 
-- should evaluate to False
3) The next to last characters of myString is "x" 
    -- should evaluate to False
4) The middle character of myString is "d" 
    -- should evaluate to True
5) The first and last characters of myString are equal 
    -- should evaluate to False
6) The last four characters of myString match the string "tion" 
    -- should evaluate to False

Example:

Q: The first character of myString is "g" -- should evaluate to True
A: print(myString[0] == "g")

"""
# Please enter your answers here
#
myString = "goodbye"

# The first character of myString is "g" -- should evaluate to True
# print(myString[0] == "g")

# Problem 2.1
print(myString[6] == "g")

# Problem 2.2
print(myString[0] == "g" and myString[1] == "a")

# Problem 2.3
print(myString[-2] == "x")

#Problem 2.4
print(myString[len(myString)//2] == "d")

# Problem 2.5
print(myString[0] == myString[-1])

# Problem 3.6
print(myString[-1]+myString[-2]+myString[-3]+myString[-4] == "tion")

"""
Problem #3 part 1
(1 pts)

Write the corresponding Python assignment statements, and then print the variables:

1) Assign 6 to variable a and 7 to variable b
2) Assign to variable c the average of variables a and b
3) Assign to variable inventory the list containing the following strings:
    paper, staples, pencils
4) Assign to variables first, middle, and last the following strings respectively:
    John Fitzgerald Kennedy
5) Assign to variable fullName the concatenation of the 
    string variables first, middle, and last.  Be sure to include spaces.

Example:

Q: Assign the string goodbye to variable myString
A: myString = "goodbye"
   print(myString)

"""
# Please enter your answers here
#
# Assign the string goodbye to variable myString
# myString = "goodbye"
# print(myString)

# Problem 3.1.1
a = 6
b = 7
print(a)
print(b)

# Problem 3.1.2
c = (a + b)/2
print(c)

# Problem 3.1.3
inventory = ["paper", "staples", "pencils"]
print(inventory)

# Problem 3.1.4
first, middle, last = "John", "Fitzgerald", "Kennedy"
print(first)
print(middle)
print(last)

# Problem 3.1.5
fullName = first + " " + middle + " " + last
print(fullName)


"""
Problem #3 part 2
(1 pts)

Using the variables defined in Problem #3 part 1, 
    write Boolean expressions corresponding to the following logical statements 
    AND evaluate the expressions 
    AND print the results.

NOTE: you can copy the variables you defined above below

1) The length of list inventory is more than five times the length of string fullName
2) Variable c is no more than 24
3) The float 6.75 is between the values of variables a AND b
4) The length of string middle is larger than string first 
    AND smaller than the length of string last.
5) Either the list inventory is empty OR it has more than 10 objects in it.

Example:

Q: The length of myString is greater than 5
A: myString = "goodbye"
   print(len(myString) > 5)

"""
# Please enter your answers here
#
# The length of myString is greater than 5
# myString = "goodbye"
# print(len(myString) > 5)

# Problem 3.2.1
print(len(inventory)>(5*len(fullName)))

# Problem 3.2.2
print(c<=24)

# Problem 3.2.3
print(a < 6.75 < b)

# Problem 3.2.4
print(len(last) > len(middle) > len(first))

# Problem 3.2.5
print(len(inventory) == 0 or len(inventory) > 10)

"""
Problem #4 part 1
(1 pts)

Using the variable gradeList below that contains a list 
    of the following letter grades as strings:

    gradeList = ["B", "B", "F", "C", "B", "A", "A", "D", "C", "D", "A", "A", "B"]

Write a sequence of Python statements that ultimately produce 
    a list (variable name: grades) that contains the number of occurences of each grade
    in alphabetic order.


Running the following command:
print(grades)

Should result in the following:
[4, 4, 2, 2, 1]

"""
# Please enter your answers here
#
gradeList = ["B", "B", "F", "C", "B", "A", "A", "D", "C", "D", "A", "A", "B"]

grades = [0, 0, 0, 0, 0]

for i in gradeList:
    if i == "A":
        grades[0] = grades[0] + 1
    elif i == "B":
        grades[1] = grades[1] + 1
    elif i == "C":
        grades[2] = grades[2] + 1
    elif i == "D":
        grades[3] = grades[3] + 1
    elif i == "F":
        grades[4] = grades[4] + 1

print(grades)

"""
Problem #4 part 2
(1 pts)

Repeat Problem #4 part 1, except the variable gradeTuple should 
    be a TUPLE instead of a LIST:

gradeTuple = ("B", "B", "F", "C", "B", "A", "A", "D", "C", "D", "A", "A", "B")

Running the following command:
print(grades)

Should still result in the following:
[4, 4, 2, 2, 1]
"""
# Please enter your answers here
#
gradeTuple = ("B", "B", "F", "C", "B", "A", "A", "D", "C", "D", "A", "A", "B")

grades = [0, 0, 0, 0, 0]

for i in gradeTuple:
    if i == "A":
        grades[0] = grades[0] + 1
    elif i == "B":
        grades[1] = grades[1] + 1
    elif i == "C":
        grades[2] = grades[2] + 1
    elif i == "D":
        grades[3] = grades[3] + 1
    elif i == "F":
        grades[4] = grades[4] + 1

print(grades)


"""
Problem #5
(2 pts)

Compute the height a ladder can reach using the given variables of length and angle.

The math module will need to be imported to use the trig formula:
    height equals length multiplied by the sine of angle
    hint: height = length * sin(angle in radians) 

The module sin() function takes input in the form of radians.  You will need
    to convert the angle provided in degrees to the angle given in radians:
    radians equals pi multiplied by degrees divided by 180
    hint: radians = pi * degrees / 180

Print the results for each of the following:

1) 16 length, 75 degrees
2) 20 length, 0 degrees
3) 24 length, 45 degrees
4) 24 length, 80 degrees

"""
# Please enter your answers here
#

# Problem 5.1
print( 16 * math.sin(math.radians(75)))

# Problem 5.2
print( 20 * math.sin(math.radians(0)))

# Problem 5.3
print( 24 * math.sin(math.radians(45)))

# Problem 5.4
print( 24 * math.sin(math.radians(80)))

"""
Problem #6
(2 pts)

Write a sequence of python statements (a program) that requests 
    a positive integer x from the user (assume it is always positive)
    and prints the first five multiples of x (x * 0, x * 1, etc)

Example of the solution display:

Enter x: 5
0
5
10
15
20

NOTE: I should be able to comment out ALL of the above text 
    and RUN this program using this file
"""
# Please enter your answers here
#

xInt = input("Enter a positive integer.")

for i in range(5):
    print(int(xInt) * i)

"""
BONUS PROBLEM
EXTRA CREDIT
(Bonus 1 pts)

The following code does not work - it does not function as expected...
Try to resolve any issues/bugs/problems you can...

hint: there are two known issues

To get credit please comment (using # tags) EVERY issue/bug/problem you 
find as well as make the appropriate correction!

"""


fahrenheit = input("Enter the temp in degrees Fahrenheit: ")
celsius = (float(fahrenheit) - 32) * 5 / 9  # Fahrenheit needs to be changed to a float
print("The temperature in degrees Celsius is " + str(celsius)) #Celsius needs to be changed to a string

"""
END
"""