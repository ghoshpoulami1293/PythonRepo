#basic implementation

mytuple = ("apple","banana","cherry")
myiterator = iter(mytuple)

print(next(myiterator))
print(next(myiterator))
print(next(myiterator))

mystring = "banana"
myiterator2 = iter(mystring)

print(next(myiterator2))
print(next(myiterator2))
print(next(myiterator2))
print(next(myiterator2))
print(next(myiterator2))
print(next(myiterator2))

#Looping through an iterator

mytuple2 = ("apple","banana","cherry")
for x in mytuple2:
    print(x)

mystring2 = "banana"
for y in mystring2:
    print(y)

# Create an iterator that returns numbers, starting with 1,
# and each sequence will increase by one (returning 1,2,3,4,5 etc.):

class Numbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a      # print the 1st num
        self.a += 1     #increment it
        return x        # for the 1st iteration, 1st num printed, then next iteration has incremented num and so on

myclass = Numbers()
myiterator3 = iter(myclass) #create an iterator object for myclass

print(next(myiterator3))    #print iterator object value
print(next(myiterator3))
print(next(myiterator3))
print(next(myiterator3))
print(next(myiterator3))

# Stop after 20 iterations:
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a<=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass2 = MyNumbers()
myiterator4 = iter(myclass2)

for x in myiterator4:
    print(x)

