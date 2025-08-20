"""
PYTHON PROGRAMMING 1
HOMEWORK
WEEK THREE

author: <Taran Kalle>
** be sure to RENAME the file <Last><First>_Week_3_Homework.py
** example: BeemerBill_Week_3_Homework.py
"""
#
"""
Complete the following problems
"""
#
"""
Problem #1
(2 pts)

Start by making the following assignment statement:

s = "abcdefghijklmnopqrstuvwxyz"

Now write expressions using string s and the indexing operator 
that evaluate to the following:

a) 'bcd'
b) 'abc'
c) 'defghijklmnopqrstuvwx'
d) 'wxy'
e) 'wxyz'

"""
# Please enter your answers here
# 
s ="abcdefghijklmnopqrstuvwxyz"
print(s[1:4])
print(s[0:3])
print(s[3:24])
print(s[22:25])
print(s[22:])

"""
Problem #2
(2 pts)

Translate each part into a Python statement using
appropriate string methods:

a) Assign the following string to a variable called message, 
then print the variable message:
"The secret of this message is that it is secret"

b) Assign to variable length the length of string message, 
using the operator len(), then print the variable length.

c) Assign to variable count the number of times the 
substring "secret" appears in string message, using
string method count(), then print the variable count.

d) Assign to variable censored a copy of string message
with every occurance of substring "secret" replaced by "xxxxxx",
using string method replace(), then print the variable censored.

"""
# Please enter your answers here
# 

# Problem 2.a
message = "The secret of this message is that it is secret"
print(message)

# Problem 2.b
length = len(message)
print(length)

# Problem 2.c
count = message.count("secret")
print(count)

# Problem 2.d
censored = message.replace("secret", "XXXXXX")
print(censored)

"""
Problem #3
(2 pts)

Write Python statements that print each of the following formatted 
outputs provided below using the assigned variables first, middle, 
and last:

first = "Marlena"
middle = "Mae"
last = "Sigel"


a) Sigel, Marlena Mae
b) Sigel, Marlena M.  # hint: remember strings are lists
c) Marlena M. Sigel
d) M. M. Sigel
e) Sigel, M.

"""
# Please enter your answers here
# 
first = "Marlena"
middle = "Mae"
last = "Sigel"

# Problem 3.a
print("{2}, {0} {1}".format(first, middle, last))

# Problem 3.b
print("{2}, {0} {1[0]}.".format(first, middle, last))

# Problem 3.c
print("{0} {1[0]}. {2}".format(first, middle, last))

# Problem 3.d
print("{0[0]}. {1[0]}. {2}".format(first, middle, last))

# Problem 3.e
print("{2}, {0[0]}.".format(first, middle, last))


"""
Problem #4
(2 pts)

Write Python statements that print the value of pi in 
the following formats:

import math   # be sure to import math prior to start

a) pi = 3.1
b) pi = 3.14
c) pi = 3.141593e+00
d) pi = 3.14159

"""
# Please enter your answers here
# 
import math

pi = math.pi

# Problem 4.a
print("{:.1f}".format(pi))

# Problem 4.b
print("{:.2f}".format(pi))

# Problem 4.c
print("{:.6e}".format(pi))

# Problem 4.d
print("{:.5f}".format(pi))


"""
Problem #5
(2 pts)

Write Python statements that print the current time in
the following formats:

import time   # be sure to import time prior to start 

a) current day = Thursday, July 13
b) current time = 09:40 PM
c) timestamp = 09:40:26    # that is hour, minutes, seconds
d) datestamp = 20240721    # that is year, month, date
e) datestamp = 07/21/24    # that is month, date, year

Note: The above time and dates should be relative to when you
complete the assignment!

"""
# Please enter your answers here
# 
import time

# Problem 5.a
print(time.strftime("%A, %B %d"))

# Problem 5.b
print(time.strftime("%I:%M %p"))

# Problem 5.c
print(time.strftime("%I:%M:%S", time.localtime(1752359219)))

# Problem 5.d
print(time.strftime("%Y%m%d", time.localtime(1752359219)))

# Problem 5.e
print(time.strftime("%m/%d/%Y", time.localtime(1752359219)))


"""
BONUS PROBLEM
EXTRA CREDIT
(Bonus 1 pts)

The following code does not work - it does not function as expected...
Try to resolve any issues/bugs/problems you can...

hint: 
there are three known issues

correct result:
7 students got: A
4 students got: B
5 students got: C
1 student got: D
2 students got: F

To get credit please comment (using # tags) EVERY issue/bug/problem you 
find as well as make the appropriate correction!

"""

classGrades = ["A", "A", "C", "F", "C", "C", "B", "B", "A", "D",
               "A", "B", "B", "F", "C", "C", "A", "A", "A"]

def gradeDistribution(grades):
    """
    Prints out the distribution of grades by grade using the list provided

    @param grades: list[str]. list of grades
    """
    for letterGrade in ["A", "B", "C", "D", "F"]: # Missing F
        gradeCount = grades.count(letterGrade)
        if gradeCount > 0:
            if gradeCount == 1: # Should be equals 1
                print("1 student got: {0}".format(letterGrade))
            else:
                print("{0} students got: {1}".format(gradeCount, letterGrade)) # Should display letterGrade instead of gradeCount

gradeDistribution(classGrades)

"""
END
"""
