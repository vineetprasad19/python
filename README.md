# python
Cheatsheet for Python Commands

This Python Cheatsheet provides a quick reference to essential commands and concepts, designed to help developers, especially beginners, efficiently navigate Python's vast functionality. Below is an overview of key categories and their associated commands: Author Vineet Prasad

1. Basic Syntax and Operations
Print and Comments:
 
print("Hello, World!")  # Print statement
# This is a comment
Variables and Data Types:
 
x = 5           # Integer
y = 3.14        # Float
z = "Python"    # String
Basic Arithmetic:
 
sum = 5 + 3
product = 4 * 7
division = 10 / 2


2. Data Structures
Lists:
 
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits[0])
Tuples:
 
coordinates = (10, 20)
print(coordinates[1])
Dictionaries:
 
user = {"name": "Alice", "age": 25}
print(user["name"])
Sets:
 
colors = {"red", "green", "blue"}
colors.add("yellow")


3. Loops and Conditionals
If-Else Statements:
 
if x > 5:
    print("Greater")
else:
    print("Smaller or Equal")
For Loop:
 
for i in range(5):
    print(i)
While Loop:
 
count = 0
while count < 5:
    print(count)
    count += 1
	
	
4. Functions
Defining Functions:
 
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))


5. File Handling
Reading and Writing Files:
 
with open("file.txt", "r") as file:
    content = file.read()
with open("file.txt", "w") as file:
    file.write("Hello, World!")
	
	
6. Exception Handling
Try-Except Block:
 
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
	
	
7. Libraries and Modules
Importing Modules:
 
import math
print(math.sqrt(16))
Popular Libraries:
NumPy for numerical computations
Pandas for data manipulation
Matplotlib for plotting


8. Object-Oriented Programming (OOP)
Classes and Objects:
 
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return "Woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())


9. Advanced Topics
List Comprehensions:

squares = [x**2 for x in range(5)]
Lambda Functions:

add = lambda a, b: a + b
print(add(2, 3))
Decorators:

def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def say_hello():
    print("Hello!")
	
	
10. Debugging Tools
Using Debugger:

python -m pdb script.py