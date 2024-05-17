#for file deletion
import os

f = open("demofile.txt","w") #no error - write creates file if not present

# error - no file present - to avoid create file first
f = open("demofile.txt") #default is read - errors out if the file is not present
f = open("demofile.txt", "rt") #r= read, t = txt


# File Reading
# Read entire file
file = open("demofile2.txt", "r")
print(file.read())

# If the file is in a different location:
# f = open("D:\\myfiles\welcome.txt", "r")
# print(file.read())

# Read parts of the file
# Return the 5 first characters of the file
file2 = open("demofile2.txt","rt")
print(file2.read(5))

#return one line by using readline()
file3 = open("demofile2.txt", "r")
print(file3.readline())

#read first 2 lines
file3 = open("demofile2.txt", "r")
print(file3.readline())
print(file3.readline())

# Looping through the lines
file4 = open("demofile2.txt", "r")
for x in file4:
    print(x) #readline() not required

#closing the file
file4.close()


#write to an existing file
file5 = open("demofile2.txt","a")
file5.write("Adding a line to the file")
file5.close()

file6= open("demofile2.txt","r")
print(file6.read())
file6.close()


file7 = open("demofile3.txt","w")
file7.write("Line1")
file7.close()

#overwrite
file7 = open("demofile3.txt","w")
file7.write("Overwriting a line to the file")
file7.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())


#creating a file
file8 = open("myfile.txt", "x")
file8.write("New file content")
file8.close()

#deleting a file
file9 = open("myfile1.txt", "x")
file9.close()
os.remove("myfile1.txt")

#check if file exists , if so, then delete it
file10 = open("myfile2.txt", "x")
if os.path.exists("myfile2.txt"):
    os.remove("myfile2.txt")
else:
    print("The file does not exist")


