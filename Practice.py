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
a = 14 
b = 3
print(a / b) #This will return a float
print(a // b) #This will return an integer

print(a % b) #This will return the remainder of the division