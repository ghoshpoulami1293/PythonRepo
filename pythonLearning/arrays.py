# use LISTS as ARRAYS.
# to work with arrays in Python you will have to import a library, like the NumPy library.
cars = ["Ford", "Volvo", "BMW"]

# access items
print(cars[1])

#length of the array
print(len(cars))

#  Loop over array
for x in cars:
    print(x)

# adding elements in array
cars.append("Honda")

# Pop an element
cars.pop(1)

# Remove an element
cars.remove("BMW") # The list's remove() method only removes the first occurrence of the specified value.

#insert
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)