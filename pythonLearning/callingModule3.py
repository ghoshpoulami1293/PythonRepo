from mymodule import person1
import datetime
import math

print(person1["age"])

#date functions
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A")) # Saturday

# create a date
y= datetime.date(2020, 5,19)
print(y)

# The datetime class can take parameters for time and timezone (hour, minute, second, microsecond, tzone)
# but they are optional, and has a default value of 0, (None for timezone).
x = datetime.datetime(2020, 5,17)
print(x)

# strftime() - formatting date objects into readable strings, takes one parameter
z = datetime.datetime(2020, 5,17)
print(z.strftime("%B")) # May

# %a - weekday , %d - day of the month
# %b - month   , %M - month num


#Math functions
# max and min functions
a = min(5, 10, 15, 20)
print(a)
b = max(5, 10, 15, 20)
print(b)

#absolute function - abs
c = abs(-7.25)
print(c)

#power
d = pow(a, b)
print(d)

#importing the math module to use existing functions
e = math.sqrt(64)
print(e)

#ceiling -rounds a number upwards to its nearest integer
#floor -  rounds a number downwards to its nearest integer
f = math.ceil(1.4)
g = math.floor(1.4)
print(f) #2
print(g) #1

h = math.pi
print(h)

