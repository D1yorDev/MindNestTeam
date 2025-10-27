# i start to Learn Dictionaries in Python

mydict = {
    'namel': "diyor",
    'age': 25,
    'job': "AI Engineer",
    'University': "Harbin Engineering University"
}
print(mydict)
print(type(mydict))
print(mydict.get("namel"))

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)

x = thisdict.keys()
print(x)

meMe = dict(LastName='Abdulazimov', name='Diyor', country='Turkey')
print(meMe)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1999
}

x = car.keys()
print(x)

car["color"] = "white"
print(x)
print(car.values())
b = car.items()
print(b)

Joiner = {
    "name": "Muhsin",
    "age": 23,
    "country": "Nigerya"
}
# Joiner.update({"country": "Maracco"})
print(Joiner)
Joiner["name"] = "Hamid"
Joiner.pop("age")
Joiner.popitem()
del Joiner["name"]
print(Joiner)
if "age" in Joiner:
    print("Yes, 'age' is one of the keys in the Joiner dictonary")

# Dictionaries Loop

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1999
}
for x in car:
    print(x)

for b in car:
    print(car[b])

print("Hozir ekranga Values chiqadi.")
for c in car.values():
    print(c)

print("Hozir ekranga Keys chiqadi.")
for c in car.keys():
    print(c)

myCar = car.copy()  # this command equall this myCar = dict(car)
print(myCar)

# Nested Dictionaries

myFamily = {
    "son": {
        "name": "MuhammadUmar",
        "year": 2029
    },
    "son2": {
        "name": "MuhammadTimur",
        "year": 2034
    },
    "dauter": {
        "name": "Aisha",
        "year": 2037
    }
}
print(myFamily)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

YourFamily = {"child1" : child1,"child2" : child2,"child3" : child3}
print(YourFamily)

for x, obj in YourFamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

print(myFamily["son2"]["name"])
print(myFamily["son2"]["year"])