#Python Numbers
#There are three numeric types in Python:
#int
#float
#complex
#Variables of numeric types are created when you assign a value to them:

x = 1   #int
y= 2.0  #float
z = 4j  #complex
print(x, type(x), y , type(y), z ,type(z))

#Int
#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

x = 1121641
y = -45464646
z = 1
print(type(x), type(y), type(z))

#Float
#Float, or "floating point number" is a number, positive or negative,
# containing one or more decimals.

x = 1.0
y = -576.5
z = 54646646.3
print(x, type(x), y , type(y), z ,type(z))

#Complex
#Complex numbers are written with a "j" as the imaginary part:

x = 3 + 5j
x = 5j
x = -6j
print(x, type(x), y , type(y), z ,type(z))

""""
Random Number
Python does not have a random() function to make a random number, 
but Python has a built-in module called random that can be used to make random numbers:
"""
import random

print(random.randrange(1, 10))
print (random.randrange(1,99))

x = 2.88
print(int(x))