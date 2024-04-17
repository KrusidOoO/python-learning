'''
Python Booleans
Booleans represent one of two values
True or False

Boolean Values
In programming it is often times needed to know if an expression is True or False
Any expression can be evaluated in Python, and get one of two answers, True or False
When two values are compared, the expression is evaluated and Python will return the Boolean answer
'''
print(10>9)
print(10==9)
print(10<9)
print("------------")
#When a condition is run in an if statement (if / if.. else) Python returns True or False
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
print("------------")
#Evaluate Values and Variables
#The bool() function allows to evaluate any value, and give True or False in return
print(bool("Hello"))
print(bool(15))
print("------------")
#Evaluate two variables
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
print("------------")
#Most Values are True
#Almost any value is evaluated as True if it has some sort of content
#Any String is True, except empty Strings
#Any number is True, except zero (0)
#Any List, Tuple, Set & Dictionary are True, except empty ones
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#Some Values are False
#Not namy Values evaluate to False
#Except empty Values such as (), [], {}, "", 0 & None
#And of course the value False will evaluate to False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#One more Value (or object) evaluates to False
#And that is an object from a class with a __len__ function
#That returns 0 or False
class myclass():
    def __len__(self):
        return  0
    
myobj = myclass()
print(bool(myobj))
print("------------")
#Functions can Return a Boolean
#Functions can be created that returns a Boolean Value
def myFunction():
    return True
print(myFunction())
print("------------")
#Code can be executed based on the Boolean answer of a function
def myFunction():
    return True
if myFunction():
    print("YES!")
else:
    print("NO!")
print("------------")
#Python has many built-in functions that return a Boolean Value
#Like isinstance() function
#Which can be used to determine if an object is of a certain data type
x = 200
print(isinstance(x, int))
print("------------")
