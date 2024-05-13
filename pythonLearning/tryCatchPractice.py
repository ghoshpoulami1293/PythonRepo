# The try block will generate an exception, because x is not defined
try:
    print(x)
except:
    print("There is an error")

# try block raises a NameError and another for other errors
try:
    print(y)
except NameError:
    print("There is a name error")
except:
    print("Something else went wrong")

# define a block of code to be executed if no errors were raised
try:
    print("Hello")
except NameError:
    print("There is a name error")
else:
    print("Nothing went wrong")

#finally
try:
    print(x)
except:
    print("Error")
finally:
    print("Woohhoo finally!")


#Writing into a file
try:
    f = open("demofile.txt")
    try:
        f.write("Pinky ponky")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
        print("Something went wrong when opening the file")


# Raising an exception
x = -1
x = 6
if x < 0:
    raise Exception("Sorry no numbers below zero") #exception raised for -1

# Type Error
a = "Hello"
a = 789
if not type(a) is int:
    raise TypeError("Integers allowed only") #Exception raised for Hello