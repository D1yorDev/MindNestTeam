# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Note: in the result
# the line breaks are inserted at the same position as in the code.


# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

a = "Hello World!"
print(a[0])

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":
    print(x)

# String Length
# To get the length of a string, use the len() function.

x = ("Abdulazimov Mukhammaddiyor")
print(len(x))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!!!"
print("free" in txt)
print("Free" in txt)

# if

txt = "The best thing in Life is Respect"

if "Respect" in txt:
    print("Yes,I RESPECT YOU!!")
else:
    print("No , You are coward and Chicken, sisy , yellow-belly")

# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

txt = "The best thing in Life is Respect"
print('expensive' not in txt)

txt = "The best thing in Life is Respect"
if "expensive" not in txt:
    print('NO, "Expensive" is not present!')

# Python - Slicing Strings
# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

# Slice From the Start
b = "hello World"
print(b[2:5])

# Slice To the End
b = "hello World"
print(b[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:

b = "hello world"
print(b[-5:-2])

# Python - Modify Strings

# Upper Case
x = "Amir Temur"
print(x.upper())

# LowerCase
x = "Elon Musk"
print(x.lower())

# Remove Whitespace
x = "Hello , World              "
print(x.strip())

# Replace String
x = "Optimus Trime"
print(x.replace("T", "P"))

# Split String
a = "Hello, World!"
print(a.split(","))

# Python - String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
d = a + " " + b
print(c)
print(d)

# Python - Format - Strings
# F-Strings
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# To specify a string as an f-string, simply put an f in front of the string literal,
# and add curly brackets {} as placeholders for variables and other operations.

age = 25
txt = f"I am {age} years old"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

print(bool("15"))
