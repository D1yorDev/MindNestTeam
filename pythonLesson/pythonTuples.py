#Today I will learn Tuples


# Tuple
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data,
# the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.


myTuple = ("dior", 1, 4.5)
print(myTuple)
print(type(myTuple))
mylist = ["dior", 1 , 3, 2.3, "dior"]
print(mylist)
print(type(mylist))


thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))

onetuple = ("apple",)
print(type(onetuple))

second = ("dior")
print(type(second))

yourTuple = tuple(("dior", 1, 3, 4))
print(yourTuple)


#Change Tuple Values
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

loo = ("Apple", "Apple", "Apple")
print(loo)
print(type(loo))
koo = list(loo)
koo[1] = "Banan"
koo[2] = "Peach"
print(koo)
print(type(koo))
loo = tuple(koo)
print(loo)
print(type(loo))
fruits = ("apple", "banana", "cherry")

fruitsr = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruitsr

print(green)
print(tropic)
print(red)


thistuple = ("apple", "banana", "cherry", "diyor")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

ruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

