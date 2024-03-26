# function takes one parameter, name. Prints "Hi, " followed by the value of parameter name.
def print_hi(name):
    print(f'Hi, {name}')


#  ensures that the code inside it will only run if the script is executed directly
#  (not imported as a module into another script).
#   If the script is being imported from another script, __name__ is set to the name of the script/module.
if __name__ == '__main__':
    print("Hello World!")
    print_hi('PyCharm')
