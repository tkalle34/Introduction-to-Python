"""
PYTHON PROGRAMMING 1
HOMEWORK
WEEK FIVE

author: <YOUR NAME HERE>
** be sure to RENAME the file <Last><First>_Week_5_Homework.py
** example: BeemerBill_Week_5_Homework.py
"""
#
"""
Complete the following problems
"""
#
"""
Problem #1
(2 pts)

Create the swapLinePickles() function that takes as input a string 
that represents the name of a file.  

(For this problem use "example.txt" from the lecture which should 
be in the resources section of this weeks module.)

The function should print out the contents of the input string
text file, with the following modification. 

Every instance of the string "line" should be replaced with "pickle".

This function should NOT modify the example.txt file.

-- calling this function:
swapLinePickles("example.txt")

-- would result in the following:
The 3 pickles in this file end with the new pickle character.

There is a blank pickle above this pickle of characters.


"""
# Please enter your solution here
#

def swapLinePickles(fileName: str):
    inFile = open(fileName, "r")
    content = inFile.read()
    inFile.close()
    content = content.replace("line","pickle")
    print(content)

swapLinePickles("example.txt")

"""
Problem #2
(2 pts)

Create a fullCopy() function that takes two inputs, a string that 
represents the name of the first file (to be copied), and a string 
that represents the name of the second file (the duplicate).

The function should copy all the contents of the first file 
into the second.

To get credit for your solution, your function MUST use the built-in 
function open() learned in Chapter 4.3. 

"""
# Please enter your solution here
#

def fullCopy(inputFile: str, outputFile:str):
    orFile = open(inputFile,"r")
    newFile = open(outputFile,"w")
    content = orFile.read()
    orFile.close()
    newFile.write(content)
    newFile.close()


"""
Problem #3
(2 pts)

Write a function fileStats() that takes one argument: 
the name of a text file. 

The function should print on the screen, the number of 
lines, words, and characters in the file.

To get full credit for your solution your function must 
OPEN the file only ONCE!!

-- calling this function:
fileStats("example.txt")

-- would result in the following:
line count: 3
word count: 20
character count: 98

^^ This is wrong
"""
# Please enter your solution here
#

def fileStats(fileName:str):
    lineCount = 0
    wordCount = 0
    charCount = 0

    with open(fileName, "r") as file:
        for line in file:
            lineCount += 1
            wordCount += len(line.split())
            charCount += len(line)
        file.close()
    print("line count: {0}".format(lineCount))
    print("word count: {0}".format(wordCount))
    print("character count: {0}".format(charCount))

fileStats("example.txt")

"""
Problem #4
(2 pts)

Implement function gradeDistro() that takes as input the name of 
a file (as a string). 

The provided one-line file (grades.txt) will 
contain letter grades separated by blanks.

e.g. B+ A- C F A B+

(For this problem use "grades.txt" which should be found in the 
Resources section of this weeks module.)

To get full credit your function should print out the 
distribution of grades AS SHOWN below. 
(NOTE the singular: 1 student got C-)

-- calling this function:
gradeDistro("grades.txt")

-- would result in the following:
6 students got A
2 students got A-
3 students got B+
2 students got B
2 students got B-
4 students got C
1 student got C-
2 students got F

HINT: don't try to "sort"! And it is okay to create a list of the grades as strings...
myList = ["A", "A-", "B+" ... etc ]

"""
# Please enter your solution here
#


def gradeDistro(fileName:str):
    myList = ["A+", "A", "A-", "B+","B","B-","C+","C","C-","D+","D","D-","F"]
    with open(fileName,"r") as file:
        grades = file.read().split()

        gradeIndex = 0
        for grade in myList:
            if grades.count(grade)>1:
                plural = "s"
            else:
                plural = ""

            if grades.count(grade):
                print("{0} student{1} got {2}".format(
                                            grades.count(grade),
                                                  plural, grade))
            gradeIndex += 1
gradeDistro("grades.txt")


"""
Problem #5 
(2 pts)

The function censor() takes the name of a file (a string) as 
input.  

The function should opwn the file, read it, and write into 
a file named "censored.txt" with the following modification: 

Every occurance of a four-letter word in the file should be replaced 
with the string "xxxx".

This function produces NO printed output, but it does create 
a new file called "censored.txt"

DO NOT include the censored.txt file when you turn in your homework!
When I run your code, if should create the file for me.  Cool?

"""
# Please enter your solution here
# 

def censor(fileName:str):
    with open(fileName,"r") as inFile:
        content = inFile.readlines()
        inFile.close()
    newLines = []

    with open("censored.txt","w") as outFile:
        for line in content:
            words = line.split()
            counter = 0
            for word in words:
                if len(word) == 4:
                    words[counter] = "xxxx"
                counter += 1
            newLines.append(" ".join(words))

        outFile.write("\n".join(newLines))
        outFile.close()

censor("example.txt")

"""
BONUS PROBLEM
EXTRA CREDIT
(Bonus 1 pts)

The following code does not work - it does not function as expected...
Try to resolve any issues/bugs/problems you can...

hint: 
there are five known issues

NOTE: this WILL create a file in your local working directory.

-- customerTest.txt should contain:

1: Richie Havens
2: 510
3: active

DO NOT include the customerTest.txt file when you turn in your homework!
When I run your code, if should create the file for me.  Cool?

To get credit please comment (using # tags) EVERY issue/bug/problem you 
find as well as make the appropriate correction!

"""

customerOne = ["Richie Havens", 456, "active"]
monthlyPoints = 18

def addRewards(cust, point, months):
    """
    adds monthly rewards points to customer total
    
    @param cust: list[str, int, str]. contains customer data
    @param points: int. amount of points to be added
    @param months: int. number of months (missing)
    """
    for month in range(1, months+1): # should be range
        cust[1] += point # Should be point

def saveCustomer(cust):
    """
    saves customer data into a text file

    @param cust: list[str, int, str]. contains customer data
    """
    lines = []
    for index, item in enumerate(cust):
        line = "{0}: {1}\n".format(index + 1, item)
        lines.append(line) # parentheses
    
    with open("customerTest.txt","w") as outFile: # Missing "w"
        outFile.write("".join(lines)) # Needed to join lines


addRewards(customerOne, monthlyPoints, 3)
saveCustomer(customerOne)


"""
END
"""
