"""
PYTHON PROGRAMMING 1
HOMEWORK
WEEK SIX

author: <Taran Kalle>
** be sure to RENAME the file <Last><First>_Week_6_Homework.py
** example: BeemerBill_Week_6_Homework.py
"""
#
"""
Complete the following problems
"""
#
"""
Problem #1
(2 pts)

Define a dictionary called agencies that stores a mapping of the acronyms
"CCC", "FCC", "FDIC", "SSB", "WPA" (the keys) to the government agencies
"Civilian Conservation Corps", "Federal Communications Commission", 
"Federal Desposit Insurance Corporation", "Social Security Board", 
"Works Progress Administration" (the values) created by 
President Roosevelt during the New Deal.

Using dictionary methods:

1) add the following agency "SEC" "Securities Exchange Commission" and
print the dictionary
2) change the following agency "SSB" to "Social Security Administration"
and print the dictionary
3) remove both the CCC and WPA and print the dictionary

"""
# Please enter your solution here
#

agencies = {
    "CCC": "Civilian Conservation Corps",
    "FCC": "Federal Communications Commission",
    "FDIC": "Federal Deposit Insurance Corporation",
    "SSB": "Social Security Board",
    "WPA": "Works Progress Administration"
}

agencies["SEC"] = "Securities Exchange Commission"
print(agencies)

agencies["SSB"] = "Social Security Administration"
print(agencies)

agencies.pop("CCC")
agencies.pop("WPA")
print(agencies)

"""
Problem #2
(2 pts)

Repeat problem #1 from scratch, but PRIOR to running step 1) do the 
following:

a) set a variable acronyms to contain all the keys in agencies and print
the variable

After completing steps 1-3 above again, perform the following:

b) print the variable acronyms

"""
# Please enter your solution here
#

agencies = {
    "CCC": "Civilian Conservation Corps",
    "FCC": "Federal Communications Commission",
    "FDIC": "Federal Deposit Insurance Corporation",
    "SSB": "Social Security Board",
    "WPA": "Works Progress Administration"
}

acronyms = list(agencies.keys())
print(acronyms)

agencies["SEC"] = "Securities Exchange Commission"
print(agencies)

agencies["SSB"] = "Social Security Administration"
print(agencies)

agencies.pop("CCC")
agencies.pop("WPA")
print(agencies)

print(acronyms)



"""
Problem #3
(2 pts)

Rewrite (refactor) the following function to use a dictionary instead of
a multiway if statement.

"""
# the following is working code that needs to be refactored
#
# def letter2number(lgrade):
#     """
#     converts letter grade to a number grade

#     @param lgrade: str. letter grade
#     """
#     # handle + and - signs first
#     if len(lgrade) == 1:
#         add = 0.0
#     elif lgrade[1] == '-':
#         add = -0.3
#     elif lgrade[1] == '+':
#         add = 0.3

#     if lgrade[0] == 'A':
#         return 4 + add
#     elif lgrade[0] == 'B':
#         return 3 + add
#     elif lgrade[0] == 'C':
#         return 2 + add
#     elif lgrade[0] == 'D':
#         return 1 + add
#     else:               # lgrade[0] must be 'F'
#         return 0

# print(letter2number("A-"))
# print(letter2number("C+"))
# print(letter2number("C"))
# print(letter2number("D+"))
# print(letter2number("F"))
# print(letter2number("B-"))


# Please enter your solution here
#

def letter2number(lgrade):
    """
    converts letter grade to a number grade

    @param lgrade: str. letter grade
    #return float. GPA
    """


    base_grades = {
    'A': 4.0,
    'B': 3.0,
    'C': 2.0,
    'D': 1.0,
    'F': 0.0
    }

    modifiers = {
    '+': 0.3,
    '-': -0.3
    }

    letter = lgrade[0]

    if len(lgrade) == 2:
        modifier = lgrade[1]
    else:
        modifier = " "


    if letter == 'F':
        return base_grades[letter]

    return base_grades[letter] + modifiers.get(modifier, 0.0)

print(letter2number("A-"))
print(letter2number("C+"))
print(letter2number("C"))
print(letter2number("D+"))
print(letter2number("F"))
print(letter2number("B-"))


"""
Problem #4
(2 pts)

Create a function called lookup that accepts a dictionary as input.

The function should ask for user input of LAST name and then ask for 
user input of FIRST name.

Using this input, print either the phone number associated with 
the name provided or print a statement that the name was not found.

Use the provided dictionary of names and phone numbers.

key             value
(first, last) : phone number

"""
# phonebook = {
#     ("Jenny", "Thompson"): "(864)230-9753",
#     ("Paul", "Simon"): "(987)665-4321",
#     ("Hans", "Anderson"): "(415)601-1210"}
#
# Please enter your solution here
#




"""
Problem #5 
(2 pts)

Using the set operators learned in Chapter 6.2 p 180 use the 
provided variables to anwswer the following problems.

Variables for Problem #5:

myLottery = {10, 13, 15, 25, 36, 51}
winningNums = {2, 13, 17, 29, 36, 52}
favoriteNums = {25, 36}

1) Did myLottery numbers win the lottery? Print the boolean
result.

2) Were either of my favoriteNums pulled as 
a winning number in winningNums? Print the boolean result.

3) Were my favoriteNums included in myLottery? Print the 
boolean result.

4) Create and print the set of all numbers from myLottery that 
are NOT in my favoriteNums.

5) Create and print the set of all myLottery picks that MATCHED
the winningNums.

Example:

Which of yukiFavNums where drawn as the winningNums?

yukiFavNums = {1, 2, 3, 4}
winningNums = {2, 13, 17, 29, 36, 52}

Solution:

print(yukiFavNums & winningNums)

"""
myLottery = {10, 13, 15, 25, 36, 51}
winningNums = {2, 13, 17, 29, 36, 52}
favoriteNums = {25, 36}

# Please enter your solution here
#

print(myLottery <= winningNums)

print(bool(favoriteNums & winningNums))

print(favoriteNums <= myLottery)

print(myLottery - favoriteNums)

print(myLottery & winningNums)


"""
BONUS PROBLEM
EXTRA CREDIT
(Bonus 1 pts)

The following code does not work - it does not function as expected...
Try to resolve any issues/bugs/problems you can...

hint: 
there are five known issues

NOTE: you will have to think logically through the code and possibly 
do the math by hand to confirm that you have indeed repaired the code.
You may need to look at the document strings to confirm the authors
intent when building the functions.

To get credit please comment (using # tags) EVERY issue/bug/problem you 
find as well as make the appropriate correction!

"""
closet = {"socks": 12,
          "shoes": 3,
          "pants": 4,
          "shirts": 7,
          "jackets": 2,
          "hats": 4} # Curly Brackets

shopping = ["socks", "shoes", "shirts", "shirts", "hats"] # Changed to list

def returnHome(current, trip):
    """
    merge current and trip

    @param current: dict[str: int]. item and amount
    @param trip: dict[str: int]. item and amount
    """
    for item in trip.keys(): # Changed to trip.keys()
        current[item] = current[item] + trip[item]

def damagedItem(current, item):
    """
    remove item due to damage

    @param current: dict[str: int]. item and amount
    @param item: str. name of item damaged
    """
    current[item] -= 1

def shoppingTrip(current, item):
    """
    add new items to closet

    @param current: dict[str: int]. item and amount
    @param item: str. name of item purchased
    """
    if item in current:
        current[item] += 1
    else:
        current[item] = 1 # Increment by 1 if exists, otherwise add


print(closet)

suitcase = {"socks": 4,
            "shoes": 1,
            "pants": 2,
            "shirts": 4,
            "jackets": 1,
            "hats": 1} # Moved up

returnHome(closet, suitcase)

damagedItem(closet, "shoes")

shopping.append("jackets")
for item in shopping:
    shoppingTrip(closet, item)


print(closet)

"""
END
"""
