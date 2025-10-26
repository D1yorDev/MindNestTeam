# SET in Python

# Methods in Sets

A = {1, 2, 3, 4, 5, 6}
B = {4, 5, 6, 7, 8, 9}

# Union() method -> Birlashtirish A va B setlarni birlashtiramiz
print(A | B)
print(A.union(B))

# add() setga malumot qo'shish uchun ishlatiladi.
A.add(7)
print(A)
B.add(7)

# Clear methodi haqida, toplamdagi barcha elementlarni o'chiradi.
C = {1, 3, 4, 4, 5}
C.clear()
print(C)

# difference() methodi ikki set orasidagi farqni yangi set sifatida chiqaradi.
A = {1, 2, 3, 4, 5, 6}
B = {4, 5, 6, 7, 8, 9}

print(A.difference(B))
print(B.difference(A))

# difference_update() ushbu to'plamdan boshqa toplamning barcha elementlarini o'chiradi.
A = {1, 2, 3, 4, 5, 6}
B = {4, 5, 6, 7, 8, 9}
A.difference_update(B)
B.difference_update(A)
print(A)
print(B)

# discard set ko'rsatilgan element bo'lsa , setdan o'chiradi.
print("Bu Discard function")
A = {1, 2, 3, 4, 5, 6}
B = {4, 5, 6, 7, 8, 9}

t = {"dior", "said", "Hassan", "Fatima", "Aiysha", "dior", True, 1, 2}
for x in t:
    print(x)
print("dior" in t)
t.add("Zubaira")
print(t)

Ab = {1, 2, 3, 4, 5, 6}
Ba = {4, 5, 6, 7, 8, 9}

A.update(B)
c = [10, 11, 12, 12]
A.update(c)
print(A)
t.remove("Hassan")
t.discard("Fatima")
t.remove(True)
t.discard("said")
print(t)
t.pop()
print(t)
t.clear()
print(t)

del t

# Python Join Sets

# -> union() method

bar = {"Joy", "Maya", "Sam"}
foo = {1, 3, 4}
fooBar = bar.union(foo)  # fooBar = (foo | bar)
print(fooBar)

set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = {"Abbos", "Usmon"}
set4 = {"carrat", "Poteto", "Onion"}
myset = (set1 | set2 | set3 | set4)  # myset = set1.union(set2, set3, set4)
print(myset)

Aset = {1, 2, 3}
mytuple = ('a', 'b', 'c')
Bset = Aset.union(mytuple)  # Bset = (Aset | mytuple) is wrong
print(Bset)

# update() method

loo = {34,54,65,56}
print(loo)
soo = { "dior",'Alo', "mao"}
loo.update(soo)
print(loo)

# -> intersection() method , You can use the & operator instead of the intersection() method,
# and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2 # same set3 = set1.intersection(set2)
print(set3)

#intersection_update()

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

#difference ()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set2.difference(set1) # same result set3 = set1 - set3

print(set3)