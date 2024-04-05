'''
Specifying a Variable Type:
Using Casting in Python can be done using Constructor Functions
Example of Constructor Functions:
int()
float()
str()
'''
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
print("------------")

#This can also be done with float (Floating point numbers)
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)
print(type(x))
print(type(y))
print(type(z))
print(type(w))
print("------------")
#If there are no decimal present in the orignial Variable, float will add a decimal after converting
#Conversion can also happen using str() method
x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))