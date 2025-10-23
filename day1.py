import sys

print(sys.version)

print("Hello World!")

if 5 > 2:
    print("Five is greater than two")

# I start to Learn Statements now
print("Python is fun!")

# many Statements
print("Hello MindNest Team!")
print("Never give up!")
print("Good luck!")

# Semicolons ;
print("Hi");
print("Diyor");
print("Ai Engineer")

# Python Output/Print
print("This will work!")
print('This will also work!')

# print without new line
print("Pyton ", end="")
print('is very important for AI')

# Python Output Numbers
print(708200)
print(5000)
print(1)

print(4 / 2)
print(4 * 2)
print(4 + 2)
print(4 - 2)

# Python Output Mix numper && Text
print("i am ", 25, "years old")

# Variables in Python

# Variables are containers for storing data values.
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
x = 5
y = "Diyor"
print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 5  # x is of type int
x = "Saidbek"  # x is now of type str
print(x)

# Casting
# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)
y = int(3)
z = float(3)
print(x, y, z)

# Get the Type
# You can get the data type of a variable with the type() function.
x = 7
y = "Sam"

print(type(x))
print(type(y))

# Case-Sensitive
# Variable names are case-sensitive.
a = 5
A = str("Diyor")
print(a)
print(A)

# Variable Names
# Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

myname = "Otimus Prime"
_myname = "Ooo Prime"
#  2myname = "diyor"  this is wrong because of Rule

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
x, y, z = "Joshqin", "Jack", "John"
print(x)
print(y)
print(z)

x = y = z = "Apple"
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x)
print(y)
print(z)
print(x, y, z)

x = "Said"
y = "Diyor"
print(x, y)

# Python Global Variables
x = "Best one"


def diyor():
    print("Python is " + x)


diyor()


def myfun():
    global b
    b = "Diyor"
    print("My name is " + b)


myfun()
print(b)

# Getting the Data Type

x = 5
y = "Name"
z = range(3)
print(z)
print(type(x))
print(type(y))
print(type(z))
