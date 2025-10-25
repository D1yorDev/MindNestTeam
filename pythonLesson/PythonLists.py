#List
#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data,
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#Lists are created using square brackets:

thisList = ["apple", "banan", "cherry"]
print(thisList)

thislist = ["apple", "banana", "cherry"]
print(thislist[-2])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Learn len() function in python list
x = [1, 2, 3,4 ,4 ,6]
print(len(x))

# Learn single element change
bar = [1, 2, 2, 4]
bar[1] = 3
print(bar)

# Learn multiple element change
bar[1:3] = [2, 3]
print(bar)

# Learning append() function
bar.append(7)
print(bar)
bar[4] = 5
print(bar)

# learning extend() function
bar.extend([6, 7, 8, 9])
print(bar)

# instert() metodi
odd = [1, 9]
print(odd + [2, 3, 4])

print(["re"] * 3)
odd.insert(1, 2)
print(odd)
odd[2:2] = [5, 7]
print(odd)

# del() method
my_list = ["a", "b", "c", "d", "f", "i"]
del my_list[2]
print(my_list)
del my_list[1:4]
print(my_list)
del my_list
print()

# remove method
mypist = ['a', 'b', 'c', 'd', 'f', 'l', 'r']
mypist.remove('a')
print(mypist)

# pop method
mypist = ['a', 'b', 'c', 'd', 'f', 'l', 'r']
print(mypist)
print(mypist.pop(1))
print(mypist)
mypist.pop()
print(mypist)

# clear() methodi
mypist.clear()
print(mypist)

A = ['A', 'B', 'C', 'D']
A.remove("B")
print(A)

a = [1, 2, 3, 4, 5]
del a[4]
print(a)

b = [4, 3, 5]
print(b.pop(1))

h = [1, 2, 3, 5, 6, 12, 5, 9, 42, 3]
print(h)
# sort method
h.sort()
print(h)

# count method
h.reverse()
print(h)

foo2 = [2 ** x for x in range(10)]
print(foo2)

bar3 = []
for x in range(10):
    bar3.append(4 ** x)
print(bar3)

pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)

odd = [x for x in range(19) if x % 2 == 1]
print(odd)

x = [x + y for x in ['Python ', 'C ', 'Php '] for y in ['Language', 'Programming', "WebSite", "Hello"]]
print(x)

dior = list(range(1,11))
print(dior)
print(8 in dior)
print(12 in dior)
print(35 not in dior)
print(6 not in dior)

for fruit in ['apple', 'nok', 'shaftoli']:
    print('I like', fruit)