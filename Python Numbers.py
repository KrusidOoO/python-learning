#There are three types of Numbers in Python
#int, float & complex

x = 1 # int
y = 2.8 # float
z = 1j # complex

print(type(x))
print(type(y))
print(type(z))

print("------------")
#Int (Integer) is a whole number, positive or negative, without decimals, of unlimited length
x = 1
y = 12345678901234567890
z = -1234567890
print(type(x))
print(type(y))
print(type(z))

print("------------")
#Float (floating point number) is a number, positive or negative, containing one or more decimals
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

print("------------")
#Float can also be scientific numbers with an "e" to indicate the power of 10
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

print("------------")
#Complex numbers are written with a "j" as the imaginary part
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

print("------------")
#You can convert one type to a different one using constructor methods
x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)
print("-")
print(type(a))
print(type(b))
print(type(c))

print("------------")
#You cannot convert complex numbers into other number types, it is complex for a reason dumby

#Random Number
#Python does not have a random() function to make a random number, but it has a module called "random" that can be used to make random numbers
import random
print(random.randrange(0,10))