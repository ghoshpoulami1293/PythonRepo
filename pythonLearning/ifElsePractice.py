a = 33
b = 200
if b > a:
    print("b is greater tahn a")
elif a > b:
    print("a is greater than b")
else:
    print("a and b are equal")

a = 567
b = 200
if b > a:
    print("b is greater than a")
elif a > b:
    print("a is greater than b")
else:
    print("a and b are equal")

a = 200
b = 200
if b > a:
    print("b is greater than a")
elif a > b:
    print("a is greater than b")
else:
    print("a and b are equal")

a = 567
b = 200
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

if a > b : print(" a is greater than b!!") # single line (short hand if)
print("A") if a > b else print("B") #short hand if else

a = 330
b = 330
print("A") if a>b else print("A=B") if a==b else print("B") # ternary operators


a = 200
b = 33
c = 500
if a>b and c>a:
    print("c is the greatest") #using and
if a>b or b>a:
    print("At least one condition is true") #using or

#The not keyword is a logical operator, and is used to reverse the result of the conditional statement
if not b>a :
    print("b is not greater than a")

#Nested if
x=41
if x>10:
    if x> 20:
        if x>30:
            if x>40:
                print("x is greater than 40")

#if statements cannot be empty,
# but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.

a = 30
b = 40
if b> a:
    pass