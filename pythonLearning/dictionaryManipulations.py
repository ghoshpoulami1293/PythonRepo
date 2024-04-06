#Dictionary
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisdict)
print(thisdict["brand"])

#no duplicate keys
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "year" : 2000
}
print(thisdict)
print(len(thisdict))

dict1 = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "colours": ["red","blue","yellow","green"],
    "colours1": ["red","blue","yellow","green","1"]
}
print(dict1)
print(type(dict1))

dict2 = dict(name = "Joe", age =15, country = "Norway")
print(dict2)

#Accessing values :
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

#get value
x = thisdict.get("model")
print(x)

#keys()
x= thisdict.keys()
print(x)

#adding key value pairs to a dictionary
car = {
    "brand": "Dodge",
    "model": "Challenger",
    "year": 2014
}

y = car.keys()
print(y) #before the change

car["color"] = "black"
print(y) #after the change
print(car)

car["year"] = 2018
print(car)

print(car.items())

#check if key exists
dict3 = {
    "brand": "Audi",
    "model": "A4",
    "year": 1964
}
print(dict3)
if "model" in dict3:
    print("model key is present")

#change dictionary items
dict4 = {
    "brand": "Audi",
    "model": "A4",
    "year": 1964
}
dict4.update({"year": 2018})
print(dict4)

dict4["year"] = 2024
print(dict4)

#Adding items
dict5 = {
    "brand": "Audi",
    "model": "A6",
    "year": 1984
}
dict5["color"] = "Red"
print(dict5)

#Remove items
dict6 = {
    "brand": "Audi",
    "model": "A6",
    "year": 1984,
    "make": "Petrol",
    "price": 40000
}
dict6.pop("model")
print(dict6)

dict6.popitem()
print(dict6)

del dict6["brand"] #deleting a key value pair
print(dict6)

dict6.clear()
print(dict6)

del dict6  #deleting the dictionary
#print(dict6) #will throw an error

#Loop dictionaries
dict7 = {
    "brand": "Audi",
    "model": "A6",
    "year": 1984,
    "make": "Petrol",
    "price": 40000
}
#print all key names
for item in dict7:
    print(item)
#or
for x in dict7.keys():
    print(x)

#print all value names
for item in dict7:
    print(dict7[item])
#or
for x in dict7.values():
    print(x)

#loop through the entire thing:
for x,y in dict7.items():
    print(x,y)

#Copy dictionaries
dict8 = {
    "brand": "Audi",
    "model": "A6",
    "year": 1984,
    "make": "Petrol",
    "price": 40000
}
dict9 = dict8.copy()
print(dict9)

dict10 = dict(dict8)
print(dict10)

#Nested Dictionaries
myfamily ={
    "child1":{
        "name":"Emil",
        "age":15,
        "height":160,
        "weight":76
    },
    "child2":{
        "name":"Rob",
        "age":17,
        "height":168,
        "weight":79
    },
    "child3":{
        "name":"Chandler",
        "age":19,
        "height":176,
        "weight":86
    }
}
print(myfamily)

child1={
        "name":"Emil",
        "age":15,
        "height":160,
        "weight":76
    }
child2={
        "name":"Rob",
        "age":17,
        "height":168,
        "weight":79
    }
child3 = {
    "name": "Chandler",
    "age": 19,
    "height": 176,
    "weight": 86
}
myfamily2 ={
    "child1":child1,
    "child2":child2,
    "child3":child3
}
print(myfamily2)

print(myfamily2["child2"]["height"])

#loop through nested dictionaries
for x, obj in myfamily2.items():
    print(x)

    for y in obj:
        print(y +  ":", obj[y])

#fromkeys() - Create a dictionary with 3 keys, all with the value 0
x = ('key1', 'key2', 'key3')
y = 0
    
dict11 = dict.fromkeys(x, y)
print(dict11)

dict12 = dict.fromkeys(x)
print(dict12)