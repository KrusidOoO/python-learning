x=5
y="John Wick"
print(x)
print("-")
print(y)

x=4 #x is now of type int
print(x)
x="Sally Sallison" #x is now of type string
print(x)

x="-----------"
print(x)
x=str(3) #x will be "3"
print(x)
y=int(3) #y will be 3
print(y)
z=float(3) #z will be 3.0
print(z)

print("------------")
x=5
y="John Wick"
print(type(x))
print(type(y))
#This is to get the type of the variable printed out on screen
x="John Wick"
#This is the same as
x='John Wick'

print("-----------------")
a=4
A="Sally Sallison"
#Capitalised a (A) will not overwrite a, thus creating two variables with one letter
print(a)
print(A)

print("-------------")
myvar="John Wick"
my_var="John Wick"
_my_var="John Wick"
myVar="John Wick"
MYVAR="John Wick"
myvar2="John Wick"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
#variable names cannot start with numbers, have a dash (-) or have spaces ( )

#Camel casing
myVariableName="John Wick"
#Pascal casing
MyVariableName="John Wick"
#Snake casing
my_variable_name="John Wick"

print("--------------")
#Many values to multiple variables
x,y,z="Orange","Banana","Cherry"
print(x)
print(y)
print(z)
print("-")
#One value to multiple variables
x=y=z="Orange"
print(x)
print(y)
print(z)
print("-")
#Unpack a collection
fruits=["apple","banana","cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)

print("--------------")
x="Python is awesome"
print(x)
print("-")
#To output multiple variables using commas
x="Python"
y="is"
z="awesome"
print(x,y,z)
#You can also use pluses (+)
print(x+y+z)
#For numbers the pluses (+) works as a mathematical operator
print("-")
x=5
y=10
print(x+y)
print("-")
#The print function can print different types of variables, as long as they are seperated by commas (,) however it does not work with pluses (+)
x=5
y="John Wick"
print(x,y)
