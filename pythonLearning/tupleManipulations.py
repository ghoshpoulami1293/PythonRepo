thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))

# To create a tuple with only one item, you have to add a comma after the item,
# otherwise Python will not recognize it as a tuple.

thistuple1 =("apple",)
print(type(thistuple1)) #this is a tuple

nottuple=("apple")
print(type(nottuple)) #not a tuple

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

#using tuple constructor
tuple5 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(tuple5)

#Access tuple items
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[1])
print(thistuple[-2])
print(thistuple[2:5])
print(thistuple[-5:-1])
print(thistuple[3:])
print(thistuple[:-2])

if "apple" in thistuple:
    print("apple is present in thistuple")

#Update tuples

#Change tuple by converting to a list
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "mango"
x= tuple(y)
print(x)

#Add items
x = ("apple", "banana", "cherry")
y = list(x)
y.append("orange") #append takes only one argument
x = tuple(y)
print(x)

#add tuple to tuple
x = ("apple", "banana", "cherry")
y = ("mango","kiwi")
z= ("avocado" , )
x+=y
x+=z
print(x)

#Delete items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#Delete the tuple completely using del
x = ("apple", "banana", "cherry")
del x
#print(x)    #this will raise an error because the tuple no longer exists

#Packing and unpacking tuples
# The number of variables must match the number of values in the tuple,
# if not, you must use an asterisk to collect the remaining values as a list.
fruits = ("apple", "banana", "cherry") #Packing
(green, yellow, red) = fruits   #Unpacking
print(green)
print(yellow)
print(red)

fruits2 =  ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits2
print(green)
print(yellow)
print(red) #saves as a list

#If the asterisk is added to another variable name than the last,
# Python will assign values to the variable until the number of values left matches the number of variables left.
fruits3 = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits3
print(green)
print(tropic) #saves as a list
print(red)

#Loop Tuples
#For loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

for i in range(len(thistuple)):
    print(thistuple[i])

#While loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i< len(thistuple):
    print(thistuple[i])
    i+=1

#Multiply tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)