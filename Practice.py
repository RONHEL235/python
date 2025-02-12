#Scopes

"""def enclosing_func ():
    m = 13

    def local():
        print(m)

    local()

m = 5
print(m)

enclosing_func()"""

#Saturday [19:10]
# 08 February 2025
 

"""x = [1,2,3]

def local():
    x[1] = 42

print(x)
local() #This now changes the x variable in the global scope and can be seen when printing x below.
print(x)"""

#Classes and Objects

#defining a class called Bike

"""class Bike:

    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material

    def brake(self):
        print("Braking")

red_bike = Bike ("Red", "Carbon fiber")
blue_bike = Bike("Blue", "Steel") """

"""
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.   
Although that way may not be obvious at first unless you're Dutch.      
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.        
Namespaces are one honking great idea -- let's do more of those! 
"""

# Sunday [21:20]
# 09 February 2025

#Numbers and Integers
"""a = 14 
b = 3
print(a / b) #This will return a float
print(a // b) #This will return an integer

print(a % b) #This will return the remainder of the division

print(a ** b ) #This will return a to the power of b

print(a / b) # true division
print(a // b) # integer division, truncation returns 1
print(-a / b) # true division again, result is opposite of previous
print(-a // b) # integer div., result not the opposite of previous

#Underscores
n = 1_024
print(n)

#Booleans
int(True) #This will return 1
int(False) #This will return 0

bool(1) #This will return True
bool(0) #This will return False
bool(-4) #This will return True 

print(not False) #This will return True
print(not True) #This will return False
print(True or False) #This will return True
print(True and False) #This will return False

#1 = True and 0 = False
print(1 + False) #This will return 1
print(1 + True) #This will return 2

#Comlex Numbers
a = 1 + 2j

#Difference between complex numbers and real numbers
c = 3.14 + 2.75j
a = -2.5 - 6j
print(c.imag)
print(c.real)

#Conjugate 
print(c.conjugate())
print(a.conjugate())"""

#Fractions and decimals 
"""from fractions import Fraction

f = Fraction(10,6)
print(f)
print(f.numerator)
print(f.denominator)"""

"""Apparently the amount of data stored for numbers is far grater for that which is stored for fractions."""

#Setting the precision of a decimal number
#from decimal import Decimal as D
#print(D("3.14"))

#print(D("3.5") - D("3.8") + D("6.3"))

#Wednesday [18:18]
# 12 February 2025

#print(D("1.1").as_integer_ratio()) #This will return the ratio of the decimal number 1.1

#print(D(1.1).as_integer_ratio()) #This will return the ratio of the decimal number 1.1
#This is soo cool.

#We have 4 ways of strings in python 
#1. Single quotes
#str1 = 'This a string'
#2. Double quotes
#str2 = "This too is a string"
#3. Triple single quotes
#str3 = '''This tooo is also a string'''
#4. Triple double quotes
#str4 = """This tooooo is a string"""

#The firth way to create a string is 
#str5 = 'This too\nis '
#print (str5)

#Let us check the length of my string
#print(len(str5)) 
#It is 12 because it counts the \n and space as unique characters.

#Encoding and decoding strings
"""string = "This is a string"
print(type(string))"""

string = "This is a string"

encoded_string = string.encode("utf-8")
print(encoded_string) #The result was going to be a byte object
