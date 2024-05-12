# Function Polymorphism
# An example of a Python function that can be used on different objects is the len() function.

x = "Hello world"
y = ("apple","banana","cherry")
z = {
    "brand" : "Ford",
    "model" : "Explorer",
    "year"  : 1978
}
print(len(x)) # returns the number of characters
print(len(y)) # returns the number of items in the tuple
print(len(z)) # returns the number of key/value pairs in the dictionary

# Class Polymorphism
# Because of polymorphism we can execute the same method for all three classes.

class Car:
    def __init__(self,brand,model):
        self.brand= brand
        self.model=model
    def move(self):
        print("Drive Car")
class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive Boat")
class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive Plane")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747") #Create a Plane class

for x in (car1, boat1, plane1):
    x.move()

#Inheritance Class Polymorphism

#Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model= model
    def move(self):
        print("Parent class move method")

#Child classes
class Car(Vehicle):
    pass

class Plane(Vehicle):
    def move(self):
        print("Fly")
class Boat(Vehicle):
    def move(self):
        print("Sail")

#create child class objects
car1 = Car("Ford", "Mustang")
boat1 =Boat("Ibiza", "Touring20")
plane1 =Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()

# Local Scope
def myfunction():
    x = 300
    print(x)
    def innerfunction():
        print(x)
    innerfunction()
myfunction()

#Global Scope

y = 5000
def myfunction1():
    print(y)

myfunction1()
print(y)

#Naming variables
z = 5860
def myfunction2():
    z = 67
    print(z)
print(z)
myfunction2()

#Global keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
def myfunc():
    global a
    a = 300
myfunc()
print(a)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword
b = 460
print(b)
def myfunction5():
    global b
    b = 730
myfunction5()
print(b)

# Nonlocal keyword
# The nonlocal keyword is used to work with variables inside nested functions- makes the variable belong to the outer function
def myfunction6():
    x = "Jane"
    print(x) #Jane
    def myfunction7():
        nonlocal x
        x = "Hello"
    myfunction7()
    return x #Hello
print(myfunction6())





