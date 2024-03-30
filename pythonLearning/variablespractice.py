#Variables and String Practice

# Variables
x = 1
y = 2.8
z = 1j #complex

print(type(x))
print(type(y))
print(type(z))

#Float
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

#Complex
x = 3+5j
print(type(x))

#TypeCasting
x = 1    # int
y = 2.8  # float
z = 1j   # complex

a = float(x)
b = int(y)
c = complex(x)

# prints a random number between 1 and 9
import random
print(random.randrange(1, 10))


#Python strings
a = "Hello World"
print (a[1])

# Looping through a string
for x in "banana":
  print(x)

print(len("Banana"))

#Check presence of substring in string
txt = "The best things in life are free!"
print("free" in txt)

# Using if , in,  not in
txt = "The best things in life are free!"
if "free" in txt:
    print("Present")
if "toodles" not in txt:
    print("Not present")

# String Slicing - Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])
print(b[3:9])
print(b[2:])
#Use negative indexes to start the slice from the end of the string:
print(b[-5:-2]) # from the string character -5 position to character in -2 position

#Build in methods for Strings
a = "Hello World"
print(a.upper()) # uppercase
print(a.lower()) # lowercase
print(a.strip()) # remove whitespaces from beginning or the end
print(a.replace("H" , "J")) # replaces a string with another string

c = "Hello, World"
print(c.split(",")) #returns a list where the text between the specified separator becomes the list items.

#String Concatenation
a = "Hello"
b  ="World"
c = a + b
print(c)
print(a + " " + b)

# Format Strings - format method
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,itemno,price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape Characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt)


# Booleans
print(10==9)
print(10>9)
print(10<9)

a = 200
b = 33
if(a>b):
    print(a)
else:
    print(b)

print(bool("Hello"))
print(bool(15))
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print(bool(" ")) # whitespace is not false
print(bool("")) #Empty is false
print(bool()) # empty
print(bool(0))
print(bool(None))
print(bool([])) #list
print(bool({})) #dict/set
print(bool(())) #tuple