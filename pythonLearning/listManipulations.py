thisList = ['apple', 'banana', 'cherry']
print(thisList)
print(len(thisList)) #prints length of the list


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 30, True, 40, "male"]

print(type(list4))

#using list constructor
thislist2 = list(("apple", "banana", "cherry"))
print(thislist2)
print(thislist2[1])
print(thislist2[-1])#negative indexing

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #5 is not included
print(thislist[:5]) #By leaving out the start value, the range will start at the first item
print(thislist[3:]) #By leaving out the end value, the range will go on to the end of the list:
print(thislist[-4:-1]) # does not include the element in -1
if "kiwi" in thislist2:
    print("present")

thisList1 = ['apple', 'banana', 'cherry']
thisList1[1] = "blackcurrant"
print(thisList1)


#Replacing values
thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist3[1:3] = ["blackcurrant", "watermelon"]
print(thislist3)
#Change the second value by replacing it with two new values
thislist3[1:2] = ["blackcurrant", "watermelon"]
print(thislist3)
#Change the second and third value by replacing it with one value
thislist3[1:3] = ["watermelon"]
print(thislist3)

#inserting values
thislist4 = ["apple", "banana", "cherry"]
thislist4.insert(2, "watermelon")
print(thislist4)

#append - to the end of the list
#insert - at a specific position
#extend - append elements from another list to the current list, tuples, sets, dictionaries etc.(any iterable object)
thislist4.append("orange")
print(thislist4)

thislist4.insert(1, "kiwi")
print(thislist4)

thislist5 = ["tomato" , "carrot" , "beans"]
thislist4.extend(thislist5)
print(thislist4)

#Remove Items
#remove - to remove a specific item
#If there are more than one item with the specified value, the remove() method removes the first occurance:
thislist6 = ["apple", "banana", "cherry"]
thislist6.remove("banana")
print(thislist6)

thislist7 = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist7.remove("banana")
print(thislist7)
