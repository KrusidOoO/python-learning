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

print("-----------")
'''
Slicing Strings
A range of characters can be returned by using the slice syntax
Specifying the start of the index and the end of the index
Seperated by a colon
To return a part of a String
'''
a = "Hello, World!"
print(a[2:5])
print("-----------")
#Slicing from the Start
#By leaving the start index blank, the slicing will start from the first character
print(a[:5])
print("-----------")
#Slicing to the End
#By leaving the end index blank, the slicing will go to the end
print(a[2:])
print("-----------")
#Negative indexing
#Using negative indexes to "wrap around" the string
#It is to but not including the End character
print(a[-5:-2])
print("-----------")
'''
Modifying Strings
'''
#The upper() method returns the string in upper case
#Using this method converts the entire string to upper case letters
print(a.upper())
print("-----------")
#The lower() method returns the string in lower case
#Using this method converts the entire string to lower case letters
print(a.lower())
print("-----------")
#Remove Whitespace
#Whitespace is the space before and/or after the text, and often you would want it removed
#The strip() method removes any whitespace from the beginning and end of a string
b = " Hello, World! "
print(b.strip())
print("-----------")
#Replace String
#The replace() method replaces a letter in a string with a different letter
print(a.replace("H", "J"))
print("-----------")
#Split String
#The split() method returns a list of text between the specified seperator
#The split() method splits the String into Substrings if instances of the seperator is found
print(a.split(","))
print("-----------")
'''
String Concatenation
To concatenate (combine) two Strings the "+" operator can be used
'''
#Merge variable a with variable b and turn it into variable c
a = "Hello"
b = "World"
c = a+b
print(c)
print("-----------")
#To add a space between the variables, add some dead air (" ")
c = a + " " + b
print(c)
print("-----------")
'''
String Formatting
Strings and numbers cannot combine, they do not want to play with each other
However they can be combined using the format() method
The format() method takes the passed arguments, formats them, and places them where placeholders ({}) are
'''
#Using the format() method to insert numbers into Strings
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
print("------------")
#The format() method can take an unlimited amount of arguments, and are placed in their respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity, itemno, price))
print("------------")
#Index numbers ({0}) can be used to be sure an argument is placed in the correct placeholders ({})
myOrder = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myOrder.format(quantity, itemno, price))
print("------------")

'''
Escape Character
To insert characters that are illegal in a string, use an escape character
An escape character (\) followed by the character that is to be inserted
An example of an illegal character is a double quote inside a string that is surrounded by double quotes
'''
#The escape character allows the use of double quotes when it normally would not be allowed
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
print("-------------")
'''
Other escape characters used in Python:
\' = Single Quote
\\ = Backslash
\n = New Line
\r = Carriage Return
\t = Tab
\b = Backspace
\f = Form Feed
\ooo = Octal Value
\xhh = Hex Value
'''
#String Methods
'''
capitalize()
    Converts the first character to upper case
casefold()
    Converts string into lower case
center()
    Returns a centered string
count()
    Returns the number of times a specified value occurs in a string
encode()
    Returns an encoded version of the string
endswith()
    Returns true if the string ends with the specified value
expandtabs()
    Sets the tab size of the string
find()
    Searches the string for a specified value and returns the position of where it was found
format()
    Formats specified values in a string
format_map()
    Formats specified values in a string
index()
    Searches the string for a specified value and returns the position of where it was found
isalnum()
    Returns True if all characters in the string are alphanumeric
isalpha()
    Returns True if all characters in the string are in the alphabet
isascii()
    Returns True if all characters in the string are ascii characters
isdecimal()
    Returns True if all characters in the string are decimals
isdigit()
    Returns True if all characters in the string are digits
isidentifier()
    Returns True if the string is an identifier
islower()
    Returns True if all characters in the string are lower case
isnumeric()
    Returns True if all characters in the string are numeric
isprintable()
    Returns True if all characters in the string are printable
isspace()
    Returns True if all characters in the string are whitespaces
istitle()
    Returns True if the string follows the rules of a title
isupper()
Returns True if all characters in the string are upper case
join()
    Joins the elements of an iterable to the end of the string
ljust()
    Returns a left justified version of the string
lower()
    Converts a string into lower case
lstrip()
    Returns a left trim version of the string
maketrans()
    Returns a translation table to be used in translations
partition()
    Returns a tuple where the string is parted into three parts
replace()
    Returns a string where a specified value is replaced with a specified value
rfind()
    Searches the string for a specified value and returns the last position of where it was found
rindex()
    Searches the string for a specified value and returns the last position of where it was found
rjust()
    Returns a right justified version of the string
rpartition()
    Returns a tuple where the string is parted into three parts
rsplit()
    Splits the string at the specified separator, and returns a list
rstrip()
    Returns a right trim version of the string
split()
    Splits the string at the specified separator, and returns a list
splitlines()
    Splits the string at line breaks and returns a list
startswith()
    Returns true if the string starts with the specified value
strip()
    Returns a trimmed version of the string
swapcase()
    Swaps cases, lower case becomes upper case and vice versa
title()
    Converts the first character of each word to upper case
translate()
    Returns a translated string
upper()
    Converts a string into upper case
zfill()
    Fills the string with a specified number of 0 values at the beginning
'''