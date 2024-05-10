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

