'''
Python strings can be written using eith '' or ""
A string can be displayed by using the print() function
'''
print('Hello')
print("Hello")
print("-----------")

#Strings can also be assigned as a value to a variable
a = "Hello"
print(a)
print("-----------")

#Multiline strings can be assigned to a variable
a = """Hello there,
this is a multiline string,
it also shows up like a multiline in the print
"""
print(a)
print("-----------")
#It can also be done using single quotes
a = '''This is also a multiline,
again this also shows up as a multiline in the print,
but it is achieved using single quotes
'''
print(a)
print("-----------")
#Where you break off each line in the code, is also how it will show up in the print
'''
Strings are like Arrays
Python does not have a character Data Type, a single character is just a string with a length of 1
Square Brackets can be used to access elements of the string
'''
a = "Hello, World!"
print(a[1])
print("-----------")
#This gets the second character of the string so in this instance it is "e" that gets printed

'''
Looping Through a String
Since strings are arrays it can loop through the characters in a string, using a for loop
'''
for x in "Nana banana":
    print(x)

print("-----------")

#String Length
#To get the length of a string use the len() Function
a = "Hello, World!"
print(len(a))

print("-----------")

#Check String
#To check if a certain phrase or character is in a string, using the keyword "in" will check for it
txt = "The best thing in life is Nana"
print("Nana" in txt)
#It will return "True" if the phrase or character is in the string that is being checked

print("-----------")

#This can be used in an if statement
txt = "The best thing in life is Nana"
if "Nana" in txt:
    print("Yes, Nana is present.")
print("-----------")
#It can also check if a phrase or character is NOT present in a string using the keyword "not in"
txt = "The best thing in life is Nana"
print("Andreas" not in txt)
#It will return True if the phrase or character is NOT present in the string that is being checked

print("-----------")
#This can also be used in an if statement
txt = "The best thing in life is Nana"
if "Andreas" not in txt:
    print("Andreas is not present.")
