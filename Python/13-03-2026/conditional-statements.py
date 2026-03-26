# Indentation needs to maintained in Python for all the conditional statements

# If Statement
number = 20
if (number > 10):
    print("The given number is greater than 10")

if (number % 2 == 0):
    # f-string is used to pass the value within a single line
    print(f"{number} is even number")

# If-Else
if(number % 2 == 0 and number % 5 == 0):
    print(f"{number} is divisible by both 2 & 5")
else:
    print(f"{number} is not divisible by either 2 or 5")

# Elif is used to check multiple conditions
num1 = 25
num2 = 35

if(num1 > num2):
    print(f"{num1} is greater than {num2}")
elif(num2 > num1):
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} is equal to {num2}")

# Shorthand If and If-else
if num1 > num2 : print(f"{num1} is greater than {num2}")

# true statement | if condition | else | False Statement
print(f"{num1} is greater than {num2}") if num1 > num2 else print(f"{num2} is greater than {num1}")

# Nested If 
num3 = 45
if (num1 > num2):
    if(num1 > num3):
        print(f"{num1} is greatest")
    else:
        print(f"{num3} is greatest")
else:
    if(num2 > num3):
        print(f"{num2} is greatest")
    else:
        print(f"{num3} is greatest")

# Match Statement
month = 5
match month:
    case 1: 
        print("January")
    case 2: 
        print("Febraury")
    case 3: 
        print("March")
    case 4: 
        print("April")
    case 5: 
        print("May")
    case 6: 
        print("June")
    case 7: 
        print("July")
    case 8: 
        print("August")
    case 9: 
        print("September")
    case 10: 
        print("October")
    case 11: 
        print("November")
    case 12: 
        print("December")

# dictionary is represented by key-value pairs

# Dictionary Properties:
# Ordered, Mutable (Changeable), Duplicate Values not allowed

student = {
    "name" : "Akshay Rao",
    "college": "ABC College",
    "degree": "B.E",
    "branch": "ISE",
    "sem": 8,
    "hobbies": ["Singing", "Playing", "Gaming", "Learning"]
}

print(student)

print(type(student))

print("Student Name:", student["name"])
print("Student Hobbies:", student["hobbies"])

# Dictionary Methods:
# keys, values, items, get, pop, popitem, update, copy, clear

# Keys method is used to get all the keys in a list format
print(student.keys())

# Values method is used to get all the values in a list format
print(student.values())

# Items method is used to get all the key-value pairs in tuple format
# We will get all the items in List format but each pair is formatted in tuple format (Outer part is list, Inner part or each key value pair is in tuple)
print(student.items())

# Get method is used to get the individual key-value pair using its key
# print(student["college"])
print(student.get("college"))

# Update method is used to add a new key-value pair or update the existing key-value pair
# Adding new key-value pair (new item)
student.update({"skills": ("HTML", "CSS", "Bootstrap", "JavaScript")})
print(student)

# Update the existing key-value pair
# dict.update({key: value})
student.update({"college": "ParvaM"})
print(student)

# Pop method is used to remove the specific item from the dictionary
# dict.pop("key")
student.pop("sem")
print("Student Details (sem has been removed):", student)

# Pop Item method is used to remove the last inserted key-value paid
student.popitem()
print("Student Details:", student)

# Copy method is used to copy the key-value pairs from one dictionary to another
new_student = student.copy()
print(new_student)

# Clear method is used to clear all the key-value pairs from the dictionary
new_student.clear()
print(new_student)

# while loop
# syntax:
# while condition:
#       print Statement

i = 0
while i < 10:
    print(f"{i}")
    # In python, increment(++) and decrement(--) operator, we should use += or -=
    # i += 1 <=> i = i + 1
    i += 1 

print("Even numbers from 10 to 20")
while i <= 20:
    if i % 2 == 0:
        print(i) 
    i += 1

print("Odd numbers from 20 to 30")
while i <= 30:
    if i % 2 != 0:
        print(i) 
    i += 1

# While Loop problems
# Work on Sum of Natural Numbers, Sum of Digits, Sum of Even Digits, Sum of Odd Digits, Count Even and Odd Digits, Reverse a Number, Palidrome or Not

# For Loop
# Syntax:
# range limit is exclusive
# for key in range(limit):
#       Print Staments
x = 1
# Print from 1 to 9, because 10 is exclusive
for x in range(11):
    print(x)

# print multiples of 3
for x in range(20):
    if x % 3 == 0:
        print(x)

# range(start, end)
# Printing the multiples of 3 from 10 to 30
print("Multiples of 3 from 10 to 30:")
for x in range(10, 30):
    if x % 3 == 0:
        print(x)

# range(start, end, step)
print("Multiple of 5:")
for x in range(0, 21, 5):
    print(x)

# For Loop with List, Tuple:
# List
milkProducts = ["Milk", "Curd", "Ghee", "Butter", "Paneer", "Cheese"]
print(milkProducts)

# for item in list:
#   print(item)

# for loop with list
for item in milkProducts:
    print(item)

# Tuple
movies = ("KGF", "KD", "Toxic", "Hebbuli", "Kantara")
print(movies)

# for loop with tuple
for movie in movies:
    print(movie)

# Nested For Loop
languages = ["Kannada", "Tamil", "Marathi", "Malayalam"]
states = ["Karnataka", "Tamil Nadu", "Maharashtra", "Kerala"]

for state in states:
    for lang in languages:
        print(f"({state}, {lang})")

# Monday Topics:
# Functions, Math Methods and Date Methods, "Regular Expressions"