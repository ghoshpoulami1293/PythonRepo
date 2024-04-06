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
