# A RegEx or Regular Expression -->  sequence of characters that forms a search pattern.
import re

txt = "The rain in Spain"

# Returns a Match object if there is a match anywhere in the string
result = re.search("^The.*Spain$", txt)
print(result)

# findall() - prints a list of all the matches in the order in which they are found
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

y = re.findall("Portugal", txt)
print(y)    #empty list returned

z = re.findall("Spain", txt)
print(z)    #list of matches returned

#search() function - returns a match object

#Search for the first white-space character in the string
a = re.search("\s", txt)
print(a.start())    # returns start index

b = re.search("Portugal", txt)
print(b)    # returns None

#split function - returns a list where the string has been split at each match

#split at each whitespace character
c = re.split("\s", txt)
print(c)

# Split the string only at the first occurrence
d = re.split("\s", txt, 1)
print(d)

#have 2 splits (1st and 2nd whitespace character split)
e = re.split("\s", txt, 2)
print(e)

#sub() - replace the matches with the text of your choice
f = re.sub("\s", "9",txt)
print(f)


#control the number of replacements by specifying the count parameter - replace 1st 2 occurences
g = re.sub("\s", "5", txt, 2)
print(g)

#Match object
h = re.search("ai", txt)
print(h) # prints an object - <re.Match object; span=(5, 7), match='ai'>

# span=(5, 7) - start and end positions of the match
# .string  - returns the string passed into the function
# .group() - returns part of the string where there was a match

# looks for any words that starts with an upper case "S"
i = x = re.search(r"\bS\w+", txt)
print(i.span())
print(i.string)
print(i.group())

#If there is no match, the value None will be returned, instead of the Match Object.
j = x = re.search(r"\bP\w+", txt)
print(j)