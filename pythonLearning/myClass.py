# when the bool() function is called on an object, Python tries to determine the truth value of the object
# It first looks for the __bool__ method.
# If __bool__ is not defined, Python then tries to call the __len__ method
# and if that's present, it checks if the length is zero or not to determine the truth value

class myClass():
    def __len__(self):
        return 0

myObj = myClass() #object instantiation
print(bool(myObj))


def myFunction():
  return True

print(myFunction())


def myFunctionAnother() :
  return False

if myFunctionAnother():
    print("Yes")
else:
    print("No") #value inside myFunctionAnother() is False --> hence No is printed

x = 500
print(isinstance(x, int)) #Check if the object is an integer or not
