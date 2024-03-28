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