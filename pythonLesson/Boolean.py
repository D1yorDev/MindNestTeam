#Booleans represent one of two values: True or False.
import random

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 22
b = 23
if (a > b):
    print(f"{a} is greater than {b}")
else:
    print("This is False.")


print(bool("hello"))
print(bool(23))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#One more value, or object in this case, evaluates to False,
#and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

#Python also has many built-in functions that return a boolean value, like the isinstance() function,
# which can be used to determine if an object is of a certain data type:

x = 3j
print(isinstance(x, complex))

x = random.randrange(0,99)
def fun():
    x = random.randrange(1,9)

    if x >5:
        print(x, "is greater than 5")
    else:
        print(x ,"is less than 5")

fun()