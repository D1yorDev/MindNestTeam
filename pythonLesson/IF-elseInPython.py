a = 23
b = 21

# if a > b:
#    print("a greater than b")
number = 2

if number > 0:
    print("The number is positive!")
else:
    print("The number is negative")

is_logged_in = True
if is_logged_in:
    print("Welcome back!")


a = 7
b = 7

if  a > b:
    print("a greater than ")
elif a == b:
    print("a equal to b")

score = 90.5

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")



number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

username = "0"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")


x = 23
y = 213

bigger = x if x > y else y
print("Bigger is ", bigger)

a = 331
b = 330
print("A") if a > b else print("=") if a == b else print("B")

score = int(input("write your score: "))
attendance = int(input("write your attendance: "))
submitted = bool(input("Did you submit: "))
print(submitted)
if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")
