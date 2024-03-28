if 5 > 2:
   print("Five is greater than two!")
elif 5 < 2:
    print("Five is lesser than two!")
else:
    print('Nope')


x = 5
y = "Hello, World!"
print(x)
print(y)


"""
This is a comment
"""
a = 4
print(a)
a = "Sally"
print(a)

x = str(3)    # x will be '3'
print(type(x))
print(x)
y = int(3)    # y will be 3
print(type(y))
print(y)
z = float(3)  # z will be 3.0
print(type(z))
print(z)


# "A" will not overwrite a
a = 4
A = "Sally"
print(a)
print(A)

# declaration in one line
c, d, e = "mumma","babai", "eggs"
print(c)
print(d)
print(e)


x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x,y,z)
print(x+y+z)


x = 5
y = "John"
#print(x+y) -  Error
print(x,y)
z=16
print(x+z)
print(x, z)


def myfunc():
    global x
    x = "global variable"

myfunc()
print(x)

# use the global keyword if you want to change a global variable inside a function.
# if global is not used, the value cannot be changed
g = "Poulami"
def myfunc2():
    global g
    g = "kitu"

myfunc2()
print(g)

x = 5
print(type(x))
