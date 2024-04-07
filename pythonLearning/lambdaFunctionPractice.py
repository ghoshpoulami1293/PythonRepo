x = lambda a : a + 10
print(x(5))

x = lambda a,b : a*b
print(x(5,10))

x = lambda a,b,c : a + b + c
print(x(5,10,15))

#Function implementation - same lambda function call be used for the calculation of different numbers
# Use lambda functions when an anonymous function is required for a short period of time.
def myfunction(n):
    return lambda a : a * n

mydoubler = myfunction(2) #value of n is set to 2
print(mydoubler(11)) #value of a is set to 11

mytripler = myfunction(3) #value of n is set to 2
print(mytripler(44)) #value of a is set to 11