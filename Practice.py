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
"""def func(b, c, a):
    print(a, c, b)

func(1, 2, 3)
"""
#Changing a mutable affects the caller
# key.points.mutable.py
"""x = [1, 2, 3]
def func(x):
 x[1] = 42 # this affects the caller!
func(x)
print(x) # prints: [1, 42, 3]
"""

#Friday [18:19]
#21 February 2025

"""class BudgetCalculator:
    def __init__(self, user_code, gross_income):
        self.user_code = user_code
        self.gross_income = gross_income
        self.tax = 0.0
        self.after_tax_income = 0.0
        self.expenses = {
            'Utilities': 0.0,
            'Rent': 0.0,
            'Transport': 0.0,
            'Health': 0.0,
            'Groceries': 0.0,
            'Communication': 0.0
        }
        self.total_expenses = 0.0
        self.net_income = 0.0

    def calculate_tax(self):
        annual_income = self.gross_income * 12
        if annual_income <= 237100:
            self.tax = annual_income * 0.18
        elif 237101 <= annual_income <= 370500:
            self.tax = 42678 + (annual_income - 237100) * 0.26
        elif 370501 <= annual_income <= 512800:
            self.tax = 77362 + (annual_income - 370500) * 0.31
        elif 512801 <= annual_income <= 673000:
            self.tax = 121475 + (annual_income - 512800) * 0.36
        elif 673001 <= annual_income <= 857900:
            self.tax = 179147 + (annual_income - 673000) * 0.39
        elif 857901 <= annual_income <= 1817000:
            self.tax = 251258 + (annual_income - 857900) * 0.41
        else:
            self.tax = 644489 + (annual_income - 1817000) * 0.45
        self.tax /= 12
        self.after_tax_income = self.gross_income - self.tax

    def calculate_expenses(self):
        self.expenses['Utilities'] = self.after_tax_income * 0.05
        self.expenses['Rent'] = self.after_tax_income * 0.15
        self.expenses['Transport'] = self.after_tax_income * 0.30
        self.expenses['Health'] = self.after_tax_income * 0.03
        self.expenses['Groceries'] = self.after_tax_income * 0.10
        self.expenses['Communication'] = self.after_tax_income * 0.02
        self.total_expenses = sum(self.expenses.values())
        self.net_income = self.after_tax_income - self.total_expenses

    def display_budget(self):
        print("\nMonthly Budget\n")
        print("Income\n")
        print(f"Gross Monthly Income (Before Tax): R{self.gross_income:.2f}")
        print(f"Gross Monthly Income (After Tax): R{self.after_tax_income:.2f}\n")
        print("Expenses\n")
        for category, amount in self.expenses.items():
            print(f"{category}: R{amount:.2f}")
        print(f"\nTotal Expenses: R{self.total_expenses:.2f}")
        print(f"\nNet Income: R{self.net_income:.2f}\n")

def main():
    while True:
        print("Budget Portal\n")
        print("1. Create New Entry")
        print("0. Exit\n")
        choice = input("Select an option: ").strip()
        if choice == '0':
            print("Exiting program. Goodbye!")
            break
        elif choice == '1':
            user_code = input("Enter user code: ").strip()
            try:
                gross_income = float(input("Enter gross income before tax: "))
                if gross_income < 0:
                    print("Income cannot be negative. Please try again.\n")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
                continue
            budget = BudgetCalculator(user_code, gross_income)
            budget.calculate_tax()
            budget.calculate_expenses()
            budget.display_budget()
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
"""

#Diving into functions and how they work

"""def do_report (data_source):
    #Fetching and preparing data.
    data = fetch_data (data_source)
    parsed_data = parse_data (data)
    filtered_data = filter_data (parsed_data)
    polished_data = polish_data (filtered_data)

    #Running algorithms on the data
    final_data = analyse (polished_data)

    #Create and return report
    report = Report (final_data)
    return report
"""
#Matrix multiplication
# matrix.multiplication.func.py
# this function could also be defined in another module
"""def matrix_mul(a, b):
    return [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)]
    for r in a]


a = [[1, 2], [3, 4]]
b = [[5, 1], [2, 1]]
c = matrix_mul(a, b)
print(c)"""

#Functions and scoping 
"They still follow the same scoping principles"

#Scoping example
"""def scope_function ():
    test = 99 #Local scope
    print("Scope Function:", test)

test = 100 #Global scope
scope_function()
print ("Global:", test)
"""
#Parsing arguments
"""x = 100
def func (y):
    print(y)

func(x)"""    

#Lets check out if I can do it 
"""x = 3
def printing_x ():
    x = 7
    print(x) 

print (x)
printing_x ()"""

#Tuesday [19:59]
#Error Handling

#Exception - An error detected during execution.

"""gen = (i for i in range(3))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
"""
"""a_dictionary = {"a": 3, "b": 4}
print(a_dictionary["a"])
"""
#If there is an error, the python code with show the error message and exit immediately. 

#Okay now lets raise an error
"""raise NotImplementedError ("This is an Error Bruv")"""

#Okay now let me define my own Exceptions 
"""def squareroot(number):
    if number < 0:
        raise ValueError ("No negative numbers please")
    return number ** .5

def quadratic(a, b, c):
    d = b ** 2- 4 * a * c
    return ((-b - squareroot(d)) / (2 * a), (-b - squareroot(d)) / (2 * a))

quadratic(1, 0, 1)"""

#There are 4 clauses to be considered when dealing exceptions

#try
#except
#else
#finally  
 
"""def try_syntax(numerator, denominator):
    try: 
        print(f'In the try block: {numerator} {denominator}')
        result = numerator / denominator
    
    except ZeroDivisionError as error:
        print(error)
    
    else:
        print('The result is:', result)
        return result
    finally:
        print('Exiting')
print(try_syntax(12, 4))
print(try_syntax(11, 0))"""

#Wednesday [18:43]
#26 February 2025

#Exceptions: try, except, else, finally

#[23:12]
"""values = (1, 2)

try: q, r = divmod() 
"""#Hi divmod is a method in python that takes two numbers and return a tuple of containing two values: the quotient and remainder of their division. 

"""result = divmod (8, 4)

Quotient = result[0]
Remainder = result[1]

print("The Quotient is:", Quotient)
print("The Remainder is:", Remainder)
"""
"""Quotient, Remainder = divmod (10, 3)
print(f"The Quotient is {Quotient} and the Remainder is {Remainder}") """

#Lets continue with the key-word-arguments
"""def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


example_function(name="Ronee", surname="Helepi", age=27, positon="Senior Software Engineer", company="BET Software Cape Town")

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

    person = {"name": "Bob", "age": 27}

    greet(**person)"""

#I sleep now

#Thursday [22:36]
#27 February 2025

#Okay I am creating an app that can will calculate the tax of the person after payday.

#1. The person would probably have to imput the salary

"""class BudgetCalculating:
    def __init__(self, user_code, gross_income):
        self.user_code = user_code
        self.gross_income = gross_income
        self.tax = 0.0
        self.after_tax_income = 0.0
        self.expenses = {
            "Utilities": 0.0,
            'Rent': 0.0,
            'Transport': 0.0,
            'Health': 0.0,
            'Groceries': 0.0,
            'Communication': 0.0
        }
        self.total_expenses = 0.0
        self.net_income = 0.0"""

#Friday[20:21]
# 28 February 2025

"""Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum."""

"""number1 = input('Insert number1:')
number2 = input('Insert number2:')

product = number1 * number2
addition = number1 + number2

if product < 1000:
    print(f'The product is {product}')
else:
    print(f'The sum is {addition}')"""


#Let practice on my own 

"""def product_and_sum (num1, num2):
    try:
        product = num1 * num2
        if product <= 1000:
            return product
        else:
            return num1 + num2

    except TypeError:
        return "Error: Please provide valid integer number."

    else: 
        print("Calculation completed successfully.")

    finally:
        print("The code was successful")

try:
    num1 = int(input("Input number 1:"))
    num2 = int(input("Input number 2:"))
    result = product_and_sum (num1, num2)
    print(result)

except ValueError:
    print("Error: Please enter valid integer number.")

else: 
    print("Inputs were valid nad processed correctly")

finally:
    print("Program execution completed")"""

#Exercise 2: Print the Sum of a Current Number and a Previous number
#Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

#I need a "for" loop

"""print("Printing current and previous number sum in range(10)")

try:
    for i in range(10):
        previous_number = 0
        
        print(f'Current Number {i} previous_number {previous_number} Sum {i + previous_number}')

        previous_number = i
        
except SyntaxError:
    print("Please fix the typos.")

else:
    print("The are no calculation of type errors.")
    
finally:
    print("Code Successfully Executed!")"""
    

#Exercise 3: Print characters present at an even index number
#Write a Python code to accept a string from the user and display characters present at an even index number.

#For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

#Easy

"""def dissecting_string (string): 
        for char in list(string[::2]):
            return char

string = input("Type an string word")
characters = dissecting_string (string) 
print(characters)
"""
#Exercise 4: Remove first n characters from a string
#Write a Python code to remove characters from a string from 0 to n and return a new string.

#For Example:

#remove_chars("PYnative", 4) so output must be native. Here, you need to remove the first four characters from a string.
#remove_chars("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string.
#Note: n must be less than the length of the string.def remove_chars(word, number):
    
"""def remove_chars(word, number):
    try:
        if number < 0 or word > len(word): 
            raise ValueError("Error: Number must be between 0 and the length of the string.")
        return word[number: ]
    except ValueError as e:
        return str(e)
    

try:
    word = input("Input a string: ")
    number = int(input("Input the number of characters to remove: "))
    remaining = remove_chars(word, number)
    print(remaining)

except ValueError:
    print("Error: Please enter a valid positive integer within the string length")

finally:
    print("Program execution completed") """


#Exercise 5: Check if the first and last numbers of a list are the same

#Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.

"""def first_and_last (numberList):
    try:
        if not numberList:
            raise ValueError("Error: This cannot be empty.")

        first = list[0]
        last = list[-1]
        
        if first == last:
            return "True"
        else:
            return "False"

    except IndexError:
        print("Error: List out of range.")

    except TypeError:
        print("Error: Please provide a list of numbers")
    
try:
    print(first_and_last([18,12,20,30,18]))

except Exception as e:
    print(f'The eas a error occurred: {e}')

finally:
    print("Program Executed Successfully")"""


#Notes: 
"""
When catching errors, if using a function , one has to take heed of the types of traps you set inside and outside the function in order to successfully catch the errors. 

Inside the functions, just ensure that you anticipate the types of errors you might find by raising an error in relation to what might be the actual error. 

While inside the function, the next thing to be done is to just write one except statement inside the function before going outside. 

Then outside you are going to write the "try", "except" and "finally" statements when calling the functions and or prompting the user. Then you will be done. 

Remember, no finally statements inside the function, only outside. 

What errors do I know?
except ValueError
expect TypeError
except IndexError

So far those are those in terms of specifications, and by that I mean if you know and understand what type of error you are expecting. But then there is a special one.

except Exception as error
    print(f'The is and error which is: {error}') 

"""

#Exercise 15: Get an int value of base raises to the power of exponent
#Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

#Note here exp is a non-negative integer, and the base is an integer.

"""def exponent(base, exp):
    try:
        if exp == 0 or base == 0:
            raise ValueError

        result = base ** exp

        return result
    
    except ValueError:
        print("Give me any number other than zero human!")
    
try:
    exponent_result = exponent(0,4)
    print(exponent_result)

except ValueError:
        print("Give me any number other than zero human!")
    
finally: 
    print("Code executed successfully")"""


#English-to-French Dictionary

#4. create an English-to-French dictionary that allows a user to input an English word, and its French translation as a (k,v) pair.

"""english_to_french = {}

while True:
    english_word = input("Input English Word or press 'stop': ")

    if english_word.lower() == 'stop':
        break
    
    french_word = input(f"Input the French Word that translates to {english_word}: ")

    english_to_french[english_word] = french_word

print("The French English Dictionary ", english_to_french)"""


#1. Define a generator function called get_odds() that returns the odd numbers from range(10). Use a for loop to find and print the third value returned.

"""def get_odds():
    for num in range(10):
        if num % 2 != 0:
            yield num

count = 0
for odds in get_odds():
    count += 1
    if count == 3:
        print("The third odd number is: ", odds)
        break"""

#2. Assign the value 7 to the variable guess_me, and the value 1 to the variable number. Write a while loop that compares number with guess_me. Print 'too low' if number is less than guess me. If number equals guess_me, print 'found it!' and then exit the loop. If number is greater than guess_me, print 'oops' and then exit the loop. Increment number at the end of the loop. Use a function.

"""def guessing_game():
    guess_me = 7
    number = 1

    while number <= guess_me:
        if number != guess_me:
            print("Guess Again Human!")
        elif number == guess_me:
            print("Yay, you found me!")
            break

        number = number + 1

    else:
        print("Opps")


guessing_game()"""

#3. Write a Python program that plays a game of guess-the-number with the user. The program asks the user to enter the lower, and upper bounds of a range if numbers. The computer will the select a random number from that range and ask the user to guess the number, until the correct one is found. The computer provides a hint to the user after each guess, and displays the number of guesses after it is done.

"""import random

def guess_the_number():
    lower = int(input("Input the lower bound: "))
    upper = int(input("Input the upper bound: "))"""


#OOP Exercise 1: Create a Class with instance attributes
#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

"""class Vehicle:
    def __init__(self, max_speed, mileage): #Methods
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)"""

#OOP Exercise 2: Create a Vehicle class without any variables and methods
"""class Vehicle:
        pass"""


#OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

"""class Bus (Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)"""

#My brain is doing a thing right now but I want to get to 10 commits but I do not want copy and paste. 

#OOP is cool and all, i think its just as easy to understand like any other python concept just that it has a way of getting a bit messy without you even noticing it.

#What is focusing on the right thing? The basics, I have to master what the little things do and I will be great. I believe I am already great and thee most creative human being to ever grace earth. That is just a simple fact, but I brush up on these little things everyday. 

#Wednesday [12:18]
#05 March 2025

#Chapter 8: Files and Data Persistence

# files/open_try.py

"""fh = open('fear.txt') # r: read, t: text

try: 
    for line in fh:
        print(line.strip()) # remove whitespace and print

finally: 
    fh.close()
    print("\nFile has been opened successfully")"""

#Reading and writing to a file using Context manager.

#Context manager to open a file 
"""with open("fear.txt", "rt") as fh:
    for line in fh:
        print(line.strip())"""

#Context manage to write to a file  
"""with open("Print_example2.txt", "w") as fw:
    print ("Hey I am printing into a file", file=fw)"""


#Copying contents of a file into another file
with open ("Print_example.txt") as f: #File now opened & text read by default
    lines = [line.rstrip() for line in f]

with open ("Print_example_copy.txt", "w") as fw:
    fw.write("\n".join(lines))