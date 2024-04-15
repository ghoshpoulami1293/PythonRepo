# class creation
class myFirstClass:
    x= 5

#object creation
obj1= myFirstClass()
print(obj1.x)

#using init() function
class mySecondClass:
        def __init__(self,name,age):
            self.name = name
            self.age=age
obj2 = mySecondClass("John", 36)
print(obj2.name)
print(obj2.age)

print(type(obj2.name))
print(type(obj2.age))

#using str() function - controls what should be returned when the class object is represented as a string.

#initializes the values
class mythirdClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age

#controls the return statement for the object
    def __str__(self):
        return f"{self.name}({self.age})"   #John(36)

p1 = mythirdClass("John", 36)

print(p1)
print(type(p1))


#methods in objects - functions belong to the object
class myFourthClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello" + self.name)

p1 = myFourthClass("John" , 36)
p1.myfunc()

#methods in objects - functions belong to the object
class myFifthClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello" + self.name)

p1 = myFifthClass("John" , 36)
p1.myfunc()

p1.age = 40
print(p1.age)

# Delete the age property from the p1 object:
del p1.age

#delete the object p1
del p1

#class definitions cannot be empty,
# but if you for some reason have a class definition with no content,
# put in the pass statement to avoid getting an error.

class Person:
    pass



