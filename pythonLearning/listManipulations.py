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
#If there are more than one item with the specified value,
thislist6 = ["apple", "banana", "cherry"]
thislist6.remove("banana")
print(thislist6)

thislist7 = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist7.remove("banana")  #the remove() method removes the first occurance
print(thislist7)

#pop - to remove the specified index.
thislist8 = ["apple", "banana", "cherry"]
thislist8.pop(1)
print(thislist8)

#The del keyword also removes the specified index and can also delete the list completely.
thislist9 = ["apple", "banana", "cherry"]
del thislist9[0]
print(thislist9)

thislist10  = ["apple", "banana", "cherry"]
del thislist10

#The clear() method empties the list.
thislist11 = ["apple", "banana", "cherry"]
thislist11.clear()
print(thislist11)


#Loop through Lists
thislist12 = ["apple", "banana", "cherry"]
for items in thislist12:
  print(items)

# Use the range() and len() functions to create a suitable iterable.
thislist13 = ["apple", "banana", "cherry"]
for item in range(len(thislist13)):
  print(thislist[item])


# While loop
thislist14 = ["apple", "banana", "cherry"]
item = 0
while item < len(thislist14):
  print(thislist14[item])
  item = item + 1

#List Comprehension offers the shortest syntax for looping through lists
thislist15 = ["berry", "boogie", "coogie"]
[print(x) for x in thislist15]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#newlist = [expression for item in iterable if condition == True]
newlist2 = [x for x in fruits if "a" in x]
print(newlist2)

newlist3 = [x for x in range(10)]
print(newlist3)
newlist4 = [x for x in range(10) if x < 5]
print(newlist4)

newlist5 = [x.upper() for x in fruits]
print(newlist5)

#Set all values in the new list to 'hello':
newlist6 = ["hello" for items in fruits]
print(newlist6)

#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
#Return "orange" instead of "banana":
#The expression in the example above says:
#"Return the item if it is not banana, if it is banana return orange".
newlist7 = [x if x != "banana" else "orange" for x in fruits]
print(newlist7)


#Sort Lists
alist = ["orange", "mango", "kiwi", "pineapple", "banana"]
alist.sort() #sorts alphanumerically
print(alist)
alist.sort(reverse=True) #sorts desc
print(alist)

alist2 = [100, 50, 65, 82, 23]
alist2.sort() #sorts in ascending order
print(alist2)
alist2.sort(reverse=True) #sorts in desc order
print(alist2)


# Customize Sort Function
# Sort the list based on how close the number is to 50:

def myFunc(n):
    return abs(n-50)

alist3 = [34, 45, 56, 67, 12, 49, 38]
alist3.sort(key=myFunc)
print(alist3)

#Case sensitive sort
alist4 = ["banana", "Orange", "Kiwi", "cherry"]
alist4.sort()
print(alist4)

# Case insensitive sort
alist4 = ["banana", "Orange", "Kiwi", "cherry"]
alist4.sort(key = str.lower)
print(alist4)

# The reverse() method reverses the current sorting order of the elements.
alist5 = ["banana", "Orange", "Kiwi", "cherry"]
alist5.reverse()
print(alist5)

# Copying Lists - copy()
list1 = ["apple", "banana", "cherry"]
list2 = list1.copy()
print(list2)
#Another way to make a copy is to use the built-in method list().
list3 = list(list1)
print(list3)

#Join Lists
# + operator
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# append()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)

# extend()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
