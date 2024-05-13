import json

# json format
x = '{ "name":"John", "age":30, "city":"New York"}'

# convert to dictionary
y = json.loads(x)
print(y["age"])


# dictionary
a = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert dictionary to json
b = json.dumps(a)
print(b)


# conversion of various types of objects to json
print(json.dumps({"name": "John","age": 30,"city":"New York"}))
print(json.dumps(["apple","banana"]))
print(json.dumps(("apple","banana")))
print(json.dumps("apple"))
print(json.dumps(45))
print(json.dumps(45.78))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Convert a Python object containing all the legal data types
c = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(c))

# indent parameter to define the numbers of indents
print(json.dumps(c, indent = 4))

#changed separator values
print(json.dumps(c, indent = 4, separators=(". ", ": ")))

#default separator values
print(json.dumps(c, indent = 4, separators=(", ", ": ")))

#to order keys in the result
print(json.dumps(c, indent= 4, sort_keys=True))
