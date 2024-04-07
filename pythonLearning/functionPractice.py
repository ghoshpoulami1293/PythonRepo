def myfunction():
    print("Poulami Ghosh")
myfunction()

def myfunction2(fname):
    print(fname)
myfunction2("Kitu")
myfunction2("Mummum")
myfunction2("babai")

def myfunction3(fname, lname):
    print(fname, " ", lname)
myfunction3("Poulami", "Ghosh")

#arbitrary arguments *
def myfunction4(*kids):
    print(kids[2])

myfunction4("Lewis", "Charles","Alonso","Max")

#key value syntax - keyword arguments
def myfunction5(child1, child2, child3):
    print("Youngest child is " + child3)
myfunction5(child1="Emil", child2="Tobias", child3 ="Linus")

#arbitrary keyword arguments **
def myfunction6(**kids):
    print("his last name is " + kids["lname"])

myfunction6(fname = "Frank", lname = "Tobias")

#default parameter - If we call the function without argument, it uses the default value:
def myfunction7(country = "Norway"):
    print("country name " + country)

myfunction7("Bhutan")
myfunction7("India")
myfunction7() #default value printed

#Passing List as an argument
def myfunction8(food):
    for x in food:
        print(x)

food = ["apple", "banana" , "cherry"]
myfunction8(food)

#return statement
def function9(x):
    return 9*x
print(function9(6))

#pass statement
def myfunction():
    pass

# Positional-Only arguments
# To specify that a function can have only positional arguments, add , / after the arguments
def my_function(x , /):
  print(x)
my_function(3)

# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments
def my_function(x):
  print(x)
my_function(x = 3)

# But when adding the , / you will get an error if you try to send a keyword argument
def my_function(x, /):
  print(x)
#my_function(x = 3) #error

#Keyword only arguments
#To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, x):
  print(x)
my_function(x = 3)

#Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:
def my_function(x):
  print(x)
my_function(3)
# But when adding the *, / you will get an error if you try to send a positional argument:
def my_function(* , x):
  print(x)
#my_function(3)# error

# You can combine the two argument types in the same function.
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, * , c,d):
  print(a+b+c+d)
my_function(5,6,c = 7, d = 8)

#Recursion
def trirecursion(k):
    if(k>0):
        result = k+ trirecursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("\n\n Recursion Example Results ")
trirecursion(6)

