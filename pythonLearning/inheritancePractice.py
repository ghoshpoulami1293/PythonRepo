class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()


# To create a class that inherits the functionality from another class,
# send the parent class as a parameter when creating the child class:

# student class has the same properties as the person class
class Student(Person):
    pass


childobj1 = Student("Baba", "Yaga")
print(childobj1.firstname)
print(childobj1.lastname)
childobj1.printname()


# child class with init method -
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
#OR
class Student1(Person):
    def __init__(self, fname, lname):
        super().__init__(self, fname, lname)
        # Add a property called graduationyear to the Student class
        self.graduationyear = 2019


# If year 2019 should be a variable,
# and passed into the Student class when creating student objects -
# add another parameter in the __init__() function:

class Student2(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname,self.lastname, 'to the class of' , self.graduationyear)

x = Student2("Mike","Olsen",2019)
print(x.lastname)
print(x.firstname)
print(x.graduationyear)
x.welcome()