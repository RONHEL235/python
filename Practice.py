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

"""string = "This is a string"

encoded_string = string.encode("utf-8")
print(encoded_string) #The result was going to be a byte object

#Decoding the string
decoded_string = encoded_string.decode("utf-8")"""

#Thursday [19:03]
# 13 February 2025

#Continuing with encoding and decoding strings
"""s = "This is s ÑÖÜc0de"
print(type(s)) #This is a type string  

encoded_s = s.encode("utf-8")
print(encoded_s)

print(type(encoded_s)) #It is now in Bytes

####Let's decode this one now 
decoded_s = encoded_s.decode("utf-8")
print(decoded_s)"""

"""Usually the encoded string is given in bytes and you can see it by it starting with a b'This a string'. That is how you can usually spot it."""

#Example 
"""bytes_obj = b"A bytes object"
print(type(bytes_obj))"""
#Indexing and slicing strings 
a_string = "There is no time left"
"""
print(a_string[0])
print(a_string[:4])
print(a_string[4:])
print(a_string[4:10])""" #Stop at 10 but do not give me 10
#print(a_string[3:10:2]) #Basically tell it what multiples to go in

#Friday [19:34]
#14 February 2025
#Alone

#More string manipulation 
"""a_string = "Ronee Helepi is the top 10 achiever for 2025"
new_a_string = a_string[::2]
print(new_a_string)"""

#String formatting 
"""
a_string = "Hello %s!"
print(a_string % "Fabrizio") 
"""

#I am guessing the % is the connector of the two
#The "s" is the string itself

#Example 2: Using the string as a template
#You have a string that can be set as default and in that string can be spaces that can be left for modification

"""the_first_string = "The name %s."
the_second_string = "is so %s."

the_final_string = the_first_string % "Ronee",the_second_string % "Unique"

print(the_final_string)"""

"""the_new_string = "The new string {} {}"
the_new_new_string = the_new_string.format("is", "good")
print(the_new_new_string)
"""
#Saturday [20:07]
#15 February 2025

"""print("The mind is the most powerful creative tool in the universe")
"""
#Monday [22:15]
# 17 February 2025

"""name = "Fab"
age = 42
print(f"Hello! My name is {name} and I'm {age}")"""

#Thursday [08:40]
#20 February 2025

#Conditional Programming 
# conditional.2.py
"""late = False
if late:
 print('I need to call my manager!') #1
else:
 print('no need to call my manager...') #2"""

#The else-if

# taxes.py
"""income = 15000
if income < 10000:
 tax_coefficient = 0.0 #1
elif income < 30000:
 tax_coefficient = 0.2 #2
elif income < 100000:
 tax_coefficient = 0.35 #3
else:
 tax_coefficient = 0.45 #4
print('I will pay:', income * tax_coefficient, 'in taxes') 
"""
# elif
# errorsalert.py
"""alert_system = 'console' # other value can be 'email'
error_severity = 'critical' # other values: 'medium' or 'low'
error_message = 'OMG! Something terrible happened!'
if alert_system == 'console':
 print(error_message) #1
elif alert_system == 'email':
 if error_severity == 'critical':
    send_email('admin@example.com', error_message) #2
elif error_severity == 'medium':
"""
#While Loop 
# binary.py
"""n = 39
remainders = []
while n > 0:
 remainder = n % 2 # remainder of division by 2
 remainders.insert(0, remainder) # we keep track of remainders
 n //= 2 # we divide n by 2
print(remainders)
"""

#Second example
# multiple.sequences.while.py
"""people = ['Conrad', 'Deepak', 'Heinrich', 'Tom']
ages = [29, 30, 34, 36]
position = 0
while position < len(people):
 person = people[position]
 age = ages[position]
 print(person, age)
 position += 1"""

#Positional arguments 
def func(b, c, a):
    print(a, c, b)

func(1, 2, 3)
