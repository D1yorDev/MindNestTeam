# loops in pthon two various:  1.While, 2. For

i = 1
while i <= 6:
    print(i)
    i += 1

i = 7
while i < 12:
    print(i)
    if (i == 10):
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# For loops

fruits = ["banan", "apple", "peach"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

# range
for x in range(7):
    print(x)

for x in range(2, 8, 2):
    print(x)

for x in range(4):
    print(x)
else:
    print("Finaly it finished!!")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Well done!")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

Color = ["Black", "Red", "yellow"]
animal = ('Hourse', "Dog", "Cat")
for x in Color:
    for y in animal:
        print(x, y)