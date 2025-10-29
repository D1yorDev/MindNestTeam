#homework loop-practicd.py

# first task
for x in range(2, 100, 2):
    pass  # print(x)

# second task
x = int(input("write number:"))
fac = 1
for i in range(1, x + 1):
    fac *= i
print(f"{x}! = {fac}")

# third task
n = int(input("Please enter number 1-20: "))

if n > 20:
    print(f"Your number is {n} and {n} is out of requiarment")
    exit()
elif n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print("your number is not divisible")
