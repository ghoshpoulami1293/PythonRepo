thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset2 = {"apple", "banana", "cherry", "apple"} #doubles are not printed, single instance is captured
print(thisset2)

thisset3 = {"apple", "banana", "cherry", True, 1, 2, False, 0}# 1 and True & False and 0 are considered the same value in sets
print(thisset3)
print(len(thisset3))
set1 = {"abc", 34, True, 40, "male"} # A set with strings, integers and boolean values
print(set1)
print(type(set1))

#using the set constructor
set2  = set(("apple", "banana", "cherry"))
print(set2)

#Accessing items
set3 = {"apple", "banana", "cherry"}
for x in thisset:
  print(set3)

if "apple" in set3:
    print("yabadabadooooo!")

print("apple" in set3)

#Adding Items
set4 = {"apple", "banana", "cherry"}
set4.add("orange")
print(set4)

#adding sets together using update method
set5 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
set5.update(tropical) #update() is used to add elements from another set
print(set5)

set6 = {"apple", "banana", "cherry"}
tropicalList = ["cucoo" , "caca" , "boogie"]
set6.update(tropicalList)
print(set6)

#Remove items from set
set7 = {"apple", "banana", "cherry"}
set7.remove("banana")
print(set7)
#set7.remove("banana") #raises error
#print(set7)

set8 = {"apple", "banana", "cherry"}
set8.discard("banana")#does not raise error
print(set8)

set9 = {"apple", "banana", "cherry"}
removeValue = thisset.pop()
print(removeValue)
print(set9)
set9.clear()
print(set9)
del set9
#print(set9)#raises error because deleted

set10 = {"apple", "banana", "cherry"}
print(set10)
del set10
#print(set10)#raises error because deleted

#Loop Sets
set11 = {"apple", "banana", "cherry"}
for x in set11:
    print(x)

#Join Sets
#union method |
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
set4 = set1|set2
print(set3)
print(set4)

#Join multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
set5 =set1.union(set2, set3, set4)
print(set5)
set6 =set1 | set2 | set3 | set4
print(set6)

#Join a set and a tuple
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)
print(x)#does not change set x

#The update() method inserts all items from one set into another.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1) #changes set 1

#Both union() and update() will exclude any duplicate items.

#Intersection