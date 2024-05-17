txt = f"The price is 49 dollars"
print(txt)

# Placeholders and Modifiers
# a placeholder can contain variables, operations, functions, and modifiers to format the value
price = 59
txt = f"The price is {price} dollars"
print(txt)

# A modifier is included by adding a colon : followed by a legal formatting type,
# like .2f which means fixed point number with 2 decimals
price = 59
txt = f"The price is {price : .2f} dollars"
print(txt)
txt1 = f"The price is {95:.2f} dollars"
print(txt1)

#Operations inside the placeholder
txt2 = f"The price of the item is {20*59} dollars"
print(txt2)

price1 = 100
tax = 0.56
txt3 = f"The price of the item is {price + (price + tax)} dollars"
print(txt3)

#if else inside the placeholders
# Return "Expensive" if the price is over 50, otherwise return "Cheap"
price3= 50
txt4 = f"It is very {'Expensive' if price >50 else 'Cheap'}"
print(txt4)

#Execute functions in f strings
fruits = "apples"
txt5 = f"I love {fruits.upper()}"
print(txt5)

#using custom functions
def myconverter(x):
    return x*0.3048
txt6 = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt6)

# modifiers
price = 59000
txt7 =f"The price is {price:,} dollars"
print(txt7) #The price is 59,000 dollars


#Using the format method for versions below 3.6
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

txt = "The price is {:.2f} dollars"
print(txt) #did not work

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

myorder1 ="I want {0} pieces of item number {1} for {2:.2f} dollars"
print(myorder1.format(quantity, itemno, price))

myorder2 ="I want {0} pieces of item number {1} for {1} dollars"
print(myorder2.format(quantity, itemno, price))

#named indexes
myorder3 ="I have a car {carname} , it is a {model}"
print(myorder3.format(carname = "Ford", model = "Mustang"))

