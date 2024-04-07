#while loop
i =1
while i < 6:
    print(i)
    i+=1

#break statement in while
i = 1
while i<6:
    print(i)
    if i==3:
        break;
    i+=1;

#continue statement in while - check this once, changes in the order of statements inside caused an infinite loop
i = 0
while i<10:
    i+=1
    if(i==5):
        continue;
    print(i)


#else in while block
i =1
while i<6:
    print(i)
    i+=1
else: #executes when the condition no longer is true
    print(" condition is no longer true")



#For loop
fruits =["apple","banana","cherry"]
for item in fruits:
    print(item)

#looping through string
for x in "banana":
    print(x)

#break statement
fruits =["apple","mango","banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits =["apple","mango","banana","cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

#continue statement
fruits =["apple","mango","banana","cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#range
for x in range(6): #range values 0 - 5
    print(x)

for x in range(2, 30, 2):
    print(x)

#Else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
    if x== 3: break
    print(x)
else:
    print("over!") #not executed as there was a break statement in for loop


#Nested Loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

#Pass statement
for x in range[0,1,2]:
    pass










