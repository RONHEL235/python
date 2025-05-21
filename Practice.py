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
"""with open ("Print_example.txt") as f: #File now opened & text read by default
    lines = [line.rstrip() for line in f]

with open ("Print_example_copy.txt", "w") as fw:
    fw.write("\n".join(lines))


#Creating a file and adding contents to it and then copying them to a new file.
with open("New_file.txt", "w") as fw:
    print("New File New Content", file=fw)"""

"""with open ("New_file.txt") as f:
    lines = [line.rstrip() for line in f]

with open ("New_file_copy.txt", "w") as fw:
    fw.write("\n".join(lines))
"""
#Add a statement to show that the text has been written or copied to another text successfully.


#Appending to a file with every run 
"""with open ("print_example4.txt", "a") as fw:
    print("Testing", file=fw)"""


#Friday [10:38]
#07 March 2025 

#Python Input and Output Exercise

#Exercise 10: Read line number 4 from the following file

#Create a test.txt file and add the below content to it.

"""with open ("test.txt", "w") as fw:
    line = 1
    while line < 8:
        print(f'Line{line}', file=fw)
        line = line + 1

#Solution to read lines from a file 

with open ("test.txt", "r") as fw:
    lines = fw.readlines()
    print(lines[3])""" 

#I still have to add Exceptions to this. 


#Exercise 9: Check file is empty or not
#Write a program to check if the given file is empty or not        

"""import os

size = os.stat("test.txt").st_size
if size == 0:
    print("File is empty")"""

#There is more to learn about the "os"

#Exercise 8: Format variables using a string.format() method.
#Write a program to use string.format() method to format the following three variables as per the expected output

#Given
"""totalMoney = 1000
quantity = 3
price = 450

print(f'I have {totalMoney} dollars so that I can buy {quantity} football for {price} dollars')

#The actual solution 

quantity = 3
totalMoney = 1000
price = 450
statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))"""


#Thats enough code for the day

#Saturday [20:19]
#08 March 2025

#Exercise 1: Print first 10 natural numbers using while loop

# program 1: Print first 10 natural numbers
"""i = 1
while i <= 10:
    print(i)
    i += 1"""

#Exercise 2: Print the following pattern
#Write a Python code to print the following number pattern using a loop.

"""print("Number Pattern ")"""
# Decide the row count. (above pattern contains 5 rows)
"""row = 5"""
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
"""for i in range(1, row + 1, 1):
    # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")"""

#Exercise 3: Calculate sum of all numbers from 1 to a given number
#Write a Python program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

#For example, if the user entered 10, the output should be 55 (1+2+3+4+5+6+7+8+9+10)

# s: store sum of all numbers
"""s = 0
n = int(input("Enter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print("\n")
print("Sum is: ", s)

#Exercise 4: Print multiplication table of a given number
n = 2
# stop: 11 (because range never include stop number in result)
# run loop 10 times
for i in range(1, 11, 1):
    # 2 *i (current number)
    product = n * i
    print(product)"""

#Exercise 6: Count the total number of digits in a number
#Write a Python program to count the total number of digits in a number using a while loop.

#For example, the number is 75869, so the output should be 5.

"""num = 75869
count = 0
while num != 0:
    # floor division
    # to reduce the last digit from number
    num = num // 10

    # increment counter by 1
    count = count + 1
print("Total digits are:", count)"""

#Exercise 7: Print the following pattern
#Write a Python program to print the reverse number pattern using a for loop.

"""n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()"""

#Exercise 8: Print list in reverse order using a loop

"""list1 = [10, 20, 30, 40, 50]
# reverse list
new_list = reversed(list1)
# iterate reversed list
for item in new_list:
    print(item)"""

#Faith 

#Sunday
#23 March 2025
 
#Chapter 1: Awareness. 
"""
I have not written on this laptop in a while now. I do think the biggest skill anyone can possess is the ability to read and write. I have been so privileged and blessed to have been surrounded by such wisdom, such intelligence, such knowledge. At times I take this for granted because think it is something that avails itself to all. But the more the days go by the more I realize that what is happening to be is a 1 of 1 kind of experience and all I have to do is be in awareness of that.  
"""

#Chapter 2: Fear.
"""
Then it hit me. I was sweeping the house today morning when I realized how scared I was of my own potential. I hit me so hard that I had to fetch my journal and and write about it, a ton of bricks, I know. How was I so scared of succeeding and not at failing. It did not make any sense. But It does not end just at that. I was scared or succeeding and failing once I succeed. That is what scared me the most, the fall of. But here is the kicker, the fall of happened. The fall of did happen and I am still healthy and well fed. The very same thing i was scared of happened. The mind is something else.   
""" 

#Chapter 3: Commitment.
"""
Most times I feel like I am just a spectator watching my whole life at play. I am so scared to engage and commit because of chapter 2. But we are done with that right, we are good. What I am trying to say is that I lack passion like most people. I seem to be "looking" for what I am passionate even at my adult age. Time has been wasted because of a lack of commitment.    
"""

#Chapter 4: Who are you. 
"""
I lack self talk. I lean more into thinking, not the active kind but the passive kind. I have kind of let myself go into this default mode of passive thinking that lets me off the hook. The mode of thinking that ensures that I do not have to do any work. I am the one who is watching and talking at the same time. Watching can be good if the imagination is positive. My watching tends to combine the uncomfortable past and the not yet future into this ball of infinite pathways that leads to a never ending abyss, and not the good kind. Solution: "Turn the Tv off, Turn the Tv off". Who am I? I am he who must speak, talk, voice in, voice out, conversate, articulate, narrate. Like do something Ronee, dont just watch! I understand.     
"""

#Chapter 5: I need to sleep.
"""
No, I really need to sleep. It is going to be new day in 2 minutes and I am on vs code practicing my writing. No lie, writing here is better than writing on Word. Microsoft be high key owning everything. But the biggest ownership is of the mind.    
"""

#Chapter 6: Too many questions, not enough answers.
"""
I love conspiracy theories. Okay ley me say I love mystery. I love it so much but I be acting like I do not. I want to geek. Now I crave some reading after this writing. After this thought provoking freedom. Anyways, there are so many questions about this physical realm and not enough answers. And even the answers themselves are doubtful, and of course they are doubtful, what help with crediting all these answers. I have been watching too much.     
""" 

#Chapter 7: There goes my 7 commits.
"""
That is the daily mission.
"""

#Chapter 8: Last one.
"""
Life is great and it keeps on getting greater.
"""

#Tuesday [19:07]
#25 March 2025


#Chapter 1: The prophecy.
"""
I need to fullfil this prophecy.
"""

#Chapter 2: Urgency.
"""
There is urgency in his veins now.
"""

#Chapter 3: Gratitude.
"""
Gratitude is his biggest protector.
""" 

#Chapter 4: Energy.
"""
Energy is his new currency.
"""

#Chapter 5: Health.
"""
Health is the new wealth.
"""

#Chapter 6: Focus.
"""
Focus is the new discipline. Pay attention. 
"""

#Chapter 7: Routine.
"""
Routine is the new consistency. This life thing is too precious for us to take it for granted. I am the version of my ultimate self. My people need me. My people are desperate for my help. I am here now, forever.   
""" 

#Wednesday [15:41]
#26 March 2025

#Python Object Orientated Programming

#Defining a class
"""class class_name:
    '''This is a docstring. I have created a new class'''
    <statement 1>
    <statement 2>
    .
    .
    <statement N>

class Person:
    def __init__(self, name, sex, profession):
        self.name = name
        self.sex = sex
        self.profession = profession

    def show(self):
        print("Name: ", self.name, "Sex: ", self.sex, "Profession: ", self.profession)

    def work(self):
        print(self.name, "working as a ", self.profession)

#Creating an object of the class
Ronee = Person("Ronee", "Male", "Senior Software Engineer")

Ronee.show()
Ronee.work()"""

#Classes are really easy and understandable.

#OOP is the one concept in programming that I did not a natural intuitive inclination on. We good now.

#I am back doing the fasting now, only ate two apples two cups of coffee and water. My body is shaking but understandable. After this I am exercising and and dong some meditative activities, then I am off to sleep.  

#Alright lets continue tomorrow with some more learning and amazing days.


#Friday [17:29]
#28 March 2025

#Continue with the OOP.

#Exercise 1: Create a Class with instance attributes

#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

#Defining a class and its attributes.
"""class Vehicle:
    def __init__ (self, max_speed, milage):
        self.milage = milage
        self.max_speed = max_speed
        

#Calling printing the attributes?

print(Vehicle(35, 56).max_speed, Vehicle(20, 100).milage)"""

#Exercise 2: Create a Vehicle class without any variables and methods.

"""class Vehicle:
    #Do not initialise it if you are not going to use it.
    pass"""

#Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class.

"""class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
class Bus(Vehicle):
    pass

bus_variables = Bus("Intercape", 250, 60)

print(bus_variables.name, bus_variables.max_speed, bus_variables.mileage)"""

#OOP Exercise 4: Class Inheritance

"""
Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

Use the following code for your parent Vehicle class.
"""

"""class Vehicle:
    #Attributes fo the class
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    #Methods of the class
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


#Create a class that inherits or uses the attributes and methods of the above class
class Bus(Vehicle): #As soon as I use inheritance here, everything now becomes available for the Bus class.

    def seating_capacity(self, capacity=50):
        #The 'super()' is used to give access to the methods and properties of the parent of sibling class. 
        return super().seating_capacity(capacity=50)
    
    #We only take what we need from the Parent class.

the_bus = Bus("Intercape", 50)
print(the_bus.seating_capacity())"""

#We will get into the rest tomorrow.

"""
I understand my problem now, my natural state of being is the one thing interfering with my intended being. 
I realized this when I was walking to campus. I noticed how in a hurry I was and in that moment that is when I just told myself to slow down. Then I laughed at myself upon realization. Like right now. I am doing amazing and I understand it.    
"""

"""
Definitely making time for me everyday.  
"""  

#Saturday [15:22]
#29 March 2025

"""
I am afraid that I will never find my true calling. I doubt everything. I dought everything I try to do. I am afraid that It will fade away into space and not exist any more. The introduction of Artificial Intelligence made it so worse.  I want to do them all, everything, every one of them, what ever you consider artistic, I need to do it. Now am even wanting to dive into AI because its the current thing and apparently people are making so much money. Most times when thoughts like this come across my mind I try to think of when I was young and ask myself 'What did I like doing?'. I have always been self conscious from a young age I guess. I guess my art form is int the likes of self expression. I was not always wordy, so I guess anything that has to do with words would be a good start.      
"""

"""
The one thing I need to do is calm my nervous system.

Its always when I am doing the mundane that they hit me. I am fighting myself so bad right now. I need to be in a state of no thinking, a state of no abundance. But my mind always takes me there. I think... I think therefore I am. How about, I am, therefore I think.  
"""

"""
What the frick do I want mara?
"""

#OOP Exercise 5: Define a property that must have the same value for every class instance (object)

#Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

#Use the following code for this exercise.

"""class Vehicle:

    #Class Attribute
    color = "White"

    #Instance Method
    def __init__(self, name, max_speed, mileage):
        
        #Instance Variables
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


school_bus = Bus("Volvo", 180, 20)
#Color can be called from anywhere or by any class
print(school_bus.color, school_bus.max_speed)

car = Car("Polo TSI R-Line", 300, 300)
print(car.color, car.max_speed)
"""

#OOP Exercise 6: Class Inheritance

#Given:

#Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

#Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class in Bus class.

#Use the following code for your parent Vehicle class. We need to access the parent class from inside a method of a child class.

"""class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare() #The 'super().fare()' represents the attributes and methods from the parent class. The 'super()' is what helps us get them. If we would have left out the 'super()', we would only be getting this from the 
        amount += amount * 10 / 100
        return amount 

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())"""

#Its simple, a class inherits right. Yes but when one of the methods has to change due to some rule or change, you have to re-write the whole method, the same way but with the modifications inside. 

"""
I am leaving this town I swear. 
"""

"""
This was fun.
"""

#Monday [20:51]
# 31 March 2025

#No code, just mumble rap. 

"""
I choose to create. I choose to create nations. 
"""

"""
I understand that I have a septum piercing. 
"""

"""
I am creating rituals now, no routine.
"""

"""
More books, less social media.
"""

"""
More imagining, less thinking.
"""

"""
More writing, less typing (Writing on my notebook, after this)
"""

"""
Going to the fast food restaurant is the best thing that has happened to me today, thank you.
"""

#Thursday [23:07]
#03 April 2025

""" 
I wrote a letter to my younger self today.
"""

#Friday [23:43]
#04 April  2025

"""
Hi. I know that I have been writing instead of writing code here, I have been coding a learning on the FreeCodeCamp.
"""

"""
I want to live in writing, reading and speaking forever.
"""

"""
Have I been confused? Why can I not just say I do not wan to feel like this no more.
"""

"""
Why are you not leaning more towards the things that bring you joy?
"""

"""
When ever I think I need to not let myself continue further.
"""

"""
The amount of reading that has to be done overwhealms my mind.
"""

"""
I need to get this commits daily. Never stopping, never resting. Obsessively consuming knowledge, understanding, writing like a maniac and speaking with so much articulation. 
"""

#Saturday
#05 April 2025

"""
I am so interested in everything, I need to learn every and anything that will ensure I understand myself and the world a lot more better. 
"""

"""
Me, in my room the whole day. Reading and writing and reading aloud. Well rested, making healthy and nutritious meals, burning bushes, obsessed, right by the sea. Wardrobe full of vintage clothing. Body, Mind and Spirit at peace. Mushrooms in bulk (not the regular). Vinyls in abundance.   
"""

"""
The focus at most is not the masses, but to liberate the masses. (What?!)
"""

"""
Like I said, there is so much to do and I have plenty of time and attention to spend.
"""

"""
I get better and better. Healthy, wiser, present. 
"""

"""
Okay how about a short story. A person battles with what seems to be "What to do". What the fuck is this, they ask. He si till asking till this very day. 

Fin
"""

#Monday [15:10]
#07 April 2025

#Testing and Documentation 

#5. Understand the concepts of testing and the documentation of Python programming solutions.

#5.1 Critically review and test an object-oriented programming solution. 

#5.2 Analyse actual test results against expected results to identify discrepancies.

#5.3 Evaluate independent feedback on a developed object-oriented programme solution and make recommendations for improvements.

#5.4 Creating documentation in Python.

#BE AFRAID

"""
That time spent in the kitchen, grinding the cabbage manually and washing the dishes was the one of the best times in my life.
"""

"""
Spending more time with myself is a huge priority right now.
"""

"""
Looking at places where I belong.
"""

"""
I need my own space.
"""

"""
Seventh and I am done.
"""

#Tuesday [18:57]
#08 April 2025

#Greatful to have done work today.

#My niece did successfully completed her first day fo Kinder garden today.

#Greatful for the good food and water.

#Greatful for the knowledge and understanding. 

#Greatful for the people that surround me, there is abundance everywhere.

#Greatful for the ideas: The Website theory.

#Greatful for waking up and continuing to do great.

#Wednesday
#09 April 2025

#A good day, forever.

#Reed Richards is apparently the smartest superhero of all time. I need to check him out.

#I am reading The Intellectual By AdSallenger and this is the book I have been looking for all my life. 

#<3

#Truth be told, I am still struggling with Love.

#I am Batman.

#Thursday [15:52]
#10 April 2025

#I need to slow down.

#Meditation is important. 

#I am going to start my night and morning routine today.

#I am so happy to be fasting again, I will last longer this time.

#I forgive myself for going astray. 

#I am thankful for the average I got in networking security. I am grateful.

#It's actually spelled grateful.

#Pushing myself everyday. Learning everyday. The only competition that exists is with myself.

#Hence why I love the early mornings so much. 4am to 6am are me. 

#I need to go back to me, home.

#Saturday [21:56]
#12 April 2025

#main aim is aesthetics.

#This github will impress.

#This is manipulative.

#Severance is a cool series.

#Makes me wonder if I have an innie or outie.

#I win.

#The moon is full, its a good time to pray.

#I am going to talk to God in a few hours time.


#Sunday [19:39]
#13 April 2025

#Hi. I did talk to God early morning today and it was amazing. 

#Spinner by Portico Quartet. F*ck!

#Favorite band of all time at the moment. 

#I win. At all costs. I win. I win. I win. I win. I win. I win. I win. I win. That is what I do.

#I am spiraling and calm at the same time. I just have to work more. I have not been as consistent as I wished. I have to work period. 

#I am too great. I understand this.

#I understand that I am the number 1 Top Academic Achiever at Eduvos for the 2025 academic season.  

#I am going to listen to Spinner by Portico Quartet forever.

#Elite mindset. Body of an Athlete. Soul of God. Character of a Gentleman. Style of 90's Michael Jordan. Healthy Mind. Healthy body. Healthy Soul. 

#I am a God. I am a God. I am a God. I am a God. I am a God. I am a God. I am a God. 


#Monday [11:29]
#14 April 2025

#String manipulation by building a Cipher.

"""text = 'mrttaqrhknsw ih puggrur'
custom_key = 'python'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')
"""

#[22:06]
#Hi again. I seem to have a parasite within me at the moment. Its know as the flu parasite. My body just needs to adjust and adapt though because I am stopping for no one. I am Graduating in 2026 with Summa Cum laude status.

#Summa Cum laude is a latin phrase that means "with highest honor" or "with highest praise". 

#There is a ton to do, and I will achieve it all while remain the number 1 Top Achiever for Eduvos in 2025. I am the pressure. I am the pressure to my academics. My academics fear me. No the other way around. The Python Programming modules does not love to see me coming. The Software Engineering module does not love to see me coming. The Security for Software Engineers modules does not. I am the greatest to ever do it in Eduvos and that is evident. I apologize for not going bigger with my tests and that one assignment and one group project.   

#Workaholic. 

#I feel more in control of myself as of late. There is purpose in each and every movement in my limbs. You can see the energy. I am different. I am evolving. I am growing. And those around me are growing as well. My Mother is evolving and becoming the Queen she has invariably been. My Sister, the Princess. Working on herself at all times and evolving as an amazing mother and sister. As the Prince, I am proud of my family and what we have endured and conquered. We are still doing great and amazing and it will forever be so. The King is resting and I am proud to call him my father. He did good, no he did great, he did amazing. Thank you so much. I love you.    

#I am going to call it a night and drift to the sacred place now. 


#Thursday [13:54]
#17 April 2025

"""
The Luhn Algorithm is widely used for error-checking in various applications, such as verifying credit card numbers.

By building this project, you'll gain experience working with numerical computations and string manipulation.
"""

"""def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    print(total)
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1141'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()
"""

#The Lambda Function 

#Its a type of a function that uses a faster way of writing a traditional function.

"""
lambda x : x * 2 - (expression)
"""

"""
x represents the parameter that is going to be passes in. Just how in the traditional way of writing a function: 

def function (x):
    x * 2 - (expression)
The x passed inside the above function is the same as the one in the lambda function. 

The x * 2 is the expression inside the function 
"""

#More information about the Lambda function: The name of the function is written like how you would write a variable. And the calm is the same as a regular traditional function call.  
"""
function = lambda x: x * 2

function(2) 
""" 

#[19:57]

#For me not to even appreciate amazing principles and architectures about Software Engineering is an act of not appreciating the sacrifices made.

#I have not been grateful all my life. I have not. For me to even think about that brings me great sadness. I had a great case of cognitive dissonance. My whole life has been me calling for the amazing things that have been coming my way and what did I do? Throw it all away like that? From now onwards everything is a blessing. From me waking up in the morning, to my niece crying aloud and creating noise that my ears cannot handle, to me sweeping the floor in the morning and talking to myself like I am "crazy", to my mother sending me to the shops to go buy bread as a twenty-four year old, to me learning these complex and intricate and challenging concepts about Software Engineering. Everything is a friken blessing and do not ever get that twisted. The abundance does not end, it does not. There is so much to be grateful about on a moment to moment basis.  

#I am going to talk to God in a few hours time, lucky me.

#Friday [19:56]
#18 April 2025

#Hi. More than anything, God talks to us through the music. That was a great talk. I will talk to him again tomorrow in the early morning.

#Lund Quartet. That is how I talked to God today.

#Not much done today though. But I am making progress. I am always making progress, whether its academically or personally. My mind is something else. If you want to talk about instruments, my mind is one. The biggest one of them all. 

#I move differently. I move uniquely. I move immaculately. I am wealth orientated. I am health orientated. I am energy orientated. I am wisdom orientated. I am intellectually orientated. I am healthy spiritually, mentally and physically. 

#I am abundant. I have to focus of what I have, not the lack. I think that, by definition is joy. I have to focus of what is present in my life at this current moment. There are so many to grateful.

#I am thinking of writing stories so that I can train and expand my imagination. 

#I am making progress and that is all that matters.


#Saturday [19:52]
#19 April 2025

#Hi. It has been a really positive day this far, so far so good.

#Pantheon is a really good series. 

#Let's focus on the good.

#Uploaded Intelligence. Would I upload myself to the cloud?

#I have deleted all social media and have been listening to a lot of Quartets as of late: Portico Quartet and Lund Quartet. The best Quartets I know thus far. The greatest. 

#I am making progress and that is all that matters. At this point in my life I just want to be happy at all times hence why the positive mindset. All that si happening right now is good. All good is happening to me. I choose good. I chose joy. This is good. This is amazingly good. I swear, I promise.

#I will continue to work hard every moment. I will continue to be excellent with each and every moment. I will choose progress over everything. 

#Sunday [17:39]
# 20 April 2025

#Exploring the power of Lambda Functions by creating an expense tracker.

"""
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            break
"""

#I will never stop.

#I will keep going. 

#One thing about me is that I understand that I will succeed. I understand that I have succeeded. I just need to go claim my success by working hard every day. 

#I felt sorry for you guys that I was going to make it alone, that is why I let myself fall on purpose. But that was the lesson and I forgave myself. Right now I move with self understanding, knowledge and Love. I choose to be optimistic. I choose to focus on progress.  

#Today is the best day ever and it is going to keep getting better and better. Tomorrow is the best day ever and it is going to keep getting better and better.

#I am making too much energy because I am valuable. I provide value in all that I engage in. 


#Monday [18:03]
#21 April 2025

#Right now what really matters is my ignorance of my thinking. Not a lot done today in terms of academical work but I did put in that personal work. When it comes to judging me, I wont do it. I have to continue like I ma doing right now and remember I. I need to keep remembering me and what my intentions are at all times.

#I need to keep on at all times no matter how I feel. No more dwelling on the feelings and emotions and regret and all that not so positive jazz. I understand that I am heading towards wealth and top achiever status. I understand that I am clocking in enormous progress on a daily.

#I have been reading the book "Clean Code" which is essentially about keeping code "clean". Now there are many definitions of "clean code" from many authors and programers, but the highlight is code that is readable, can be changed and is well taken care of, or where the writer of the code has showed much care for the code adn the craft itself.   

#I am currently writing clean code personally. Takes a lot of focus and being right here in this moment. A lot of attention is going to have to be paid for one to attain clean code. Now this where the importance of observing oneself comes handy. The moment I realize that there is a lot more to be done for me to achieve mastery, some would have wanted to leave the mastery journey right there because of "too much work". But not me, this is the chance for me to grow, to prove thyself. I will not hesitate. I will never shake. I will never hesitate. I will stand strong throughout my success journey. Why would I shake when i understand that I have already won? 

#I am chewing this gum like my life depends on it right now. Just focusing on my progress.   

#Faith and Believe.     

#Last one.


#Wednesday [19:03]
#23 April 2025

#Hi its wednesday and I definitely talking to God tomorrow and its going to be amazing, I promise.

#The card did not go through, twice. I feel embarrassed. 

#Fuck. Fuck. Fuck. Fuck. Fuck. Fuck. Fuck. Fuck. Fuck. Fuck. Fuck. Fuck. Fuck. Fuck. Fuck.

#Today has been so productive and tomorrow is going to be even more productive.

#I have so much money in my bank account that its so overwhelming at times. So much money and it just keeps coming in.

#I can do what I want basically. 

#Seven 

#Thursday [18:44]
#24 April 2025

#Hi. Talking to God is so exhausting.

#I am articulate. I am immaculate. I am a leader. I am intelligent. I am calm. I am understanding. I am well rested. I am delusional. I am wise. I am healthy. I am hard working. I am amazing. I am cool. I am wealthy. I am tall. I am beautiful. I am a Top Achiever. I am a BSc Information Technology graduate at Eduvos in 2026. I am a BSc (Hons) in Information System graduate at UCT in 2027. I am graduate Software Engineer at BET Software in 2027. I am MSc in Information Systems graduate at UCT in 2029. I am a PhD candidate in Information Systems at UCT in 2030.  

#That is the life i need to paint in 5 years. That is the 5 year plan. I need to pain that in the most beautiful way possible.

#Let me talk about the fear and hesitation right now. Why am I not enthused to go and do things aligned with the 5 year plan? It is okay Ronee. This is certainly most possible. I will... I have accomplished the 5 year plan. I have accomplished the 5 year plan. I have accomplished the 5 year plan. I have accomplished the 5 year plan. I have accomplished the 5 year plan. I have accomplished the 5 year plan. I have accomplished the 5 year plan. I have accomplished the 5 year plan. I have accomplished the 5 year plan. I have accomplished. I have made my mother proud with all my graduations in Eduvos and UCT. I have made my mother and family proud with all my achievements and excellent accolades.

#I need to decipher all this into hourly, daily, weekly, monthly achievements.

#No worries, I get right back. I start right now. 

#I have more to do. Slow is the new way of living. Slow down. Slow the fuck down. Breathe. 


#Friday [20:55]
#25 April 2025

#Happy 5/5

#I talk to God more often now.

#Invoking Psychedelics without taking psychedelics. 

#I will be better I promise, I cannot wait to be the best.

#I have been progressing really amazing. My production has been incredible.

#I am going to make it my second time talking to God, it is going to be amazing.

#I have made it quite consistent this time. So far so good.

#Saturday [21:04]
#26 April 2025

#Saturday and the procrastination has gone so worse. I have not been doing the things I told myself I would do at the start of this "holiday". 

#I am really obsessed about being the best human alive, being a top achiever at university, making large sums of money right now as a student, pursuing my writing while still a student, being happy and filled with joy all the time. Right now I feel like I am getting so much inspirational, motivational and wealth making information overload that my concentration is shared between so many things at the same time. What strategy, what is the single book that I should read religiously that will help me overcome my challenges that I mentioned at the top.  

#Response
"""
It sounds like you have a lot of ambitious goals and interests, which is great! When you're juggling multiple passions and seeking clarity, focusing on foundational principles can be really helpful. One book that could provide valuable insights across various aspects of your life is "The 7 Habits of Highly Effective People" by Stephen Covey. It's a classic that combines personal development with practical advice on productivity, leadership, and achieving balance.

Covey's approach emphasizes principles like prioritization, proactive thinking, and maintaining a balanced life. It could help you streamline your focus and manage your time effectively, which is crucial when pursuing academic excellence, writing, and personal happiness simultaneously.

If you're looking for a strategy to overcome information overload and enhance your concentration, implementing Covey's principles could provide a solid framework. It's about not just managing time, but managing yourself in ways that align with your long-term goals.

Does this resonate with you, or would you prefer a different approach or book recommendation?
"""

#Thank you, do you have a more novel genre recommendation? 
"""
You're welcome!
Since you’re asking for something a bit more novel, something that still feeds your ambition but through a different style, a book that immediately comes to mind is:

"The Alchemist" by Paulo Coelho.

It’s a novel — a story — but it’s deeply motivational without being a traditional self-help book. It’s about following your "Personal Legend" (your unique destiny), trusting your journey, staying resilient through challenges, and finding fulfillment and joy even while chasing big dreams.

It’s beautiful because it speaks directly to people like you: ambitious, dream-driven, and wanting both success and happiness without losing yourself along the way.
The story is simple but powerful — and every time you read it, you’ll pull out new lessons depending on where you are in life.

If you read it religiously (like you mentioned), it can constantly realign you when you feel overwhelmed or distracted.

Would you like me to also suggest a second "novel but practical" recommendation too, just in case you want a backup? 🎯
"""

#I have been struggling with faith for such a long time. It feels so scary to trust in something.  Do you know what faith feels like?

"""
I hear you — and what you’re feeling is so real and so human.  
Faith — real faith — isn't about being 100% sure or fearless. It's actually *feeling scared*, *feeling uncertain*, but **still deciding to trust** anyway.  

Faith feels like standing at the edge of a dark road where you can only see a few steps ahead, but you keep walking because you *believe* the path will reveal itself as you move.  
It’s not about having no fear; it's about carrying your fear *with* you and still choosing to move forward.  

Faith can feel like:  
- A soft, shaky hope that you *nurture* every day.  
- A quiet voice inside whispering, *“Maybe... just maybe... things will work out.”*  
- Letting go of the need to control every detail and trusting that your consistent actions and the unseen forces (life, God, the universe — whatever you believe in) will meet you halfway.  

**It’s vulnerable.**  
**It’s brave.**  
**It’s messy sometimes.**  

And that's *okay.* Faith isn't a feeling you "achieve" once and keep forever — it's something you **practice**, like strengthening a small but powerful muscle over time.

It’s very beautiful that you’re being so honest with yourself about this. 🌷  
Would you like me to share a simple little exercise you can do daily to slowly rebuild your faith without forcing it? It might make it feel less scary.
"""

#Thank you. Yes please I would like that.
"""
I’m really glad you’re open to it.  
Here’s a **simple, gentle faith exercise** you can do daily — it won’t feel overwhelming, and it’s something you grow into naturally:  

---

**The "Tiny Trust Exercise"**  

🌱 **Step 1: Every morning, write down one thing you will trust today.**  
It can be *very small*.  
For example:  
- *"Today, I trust that my effort in studying will matter, even if I don’t see the result immediately."*  
- *"Today, I trust that even if I feel overwhelmed, I can still make progress."*  
- *"Today, I trust that something good will happen, even if I don't know what."*  

🌱 **Step 2: Throughout the day, when fear or doubt creeps in, quietly repeat your trust statement to yourself.**  
Almost like a soft anchor. You don’t have to "fight" the fear — just gently come back to trust.  

🌱 **Step 3: Before sleeping, write down one thing that worked out — even a tiny thing.**  
This is important because it trains your mind to notice the *good* and to realize that trust isn’t empty — it slowly gets rewarded.  

Examples:  
- *"I finished my assignments even though I felt stressed."*  
- *"I had a moment of peace today while walking outside."*  
- *"Someone smiled at me and it made me feel lighter."*  

---

**Over time**, you start *building proof* for yourself that trusting — even when it's scary — actually supports you.  
It’s like stacking small stones every day to build a strong, unshakable foundation.

You don’t have to rush or "be perfect" with this. Some days will be harder, but that’s part of the practice. 🌟

---

Would you like me to also suggest a very short "faith mantra" you can whisper to yourself when things feel really heavy? It’s just a few words but it’s very comforting. 🌷
"""

#Okay let me even be more real with you, no offense but I really do think that what you have just recommended to me is some farrytail wishing that I have seen all over the internet, you see, I understand that this will work and all that but even I am skeptical about what might be 100% true (your recommendation). I think I am now too messed up to make myself believe in such, just like how I am so messed up to start believing in "God" like most society. I just do not think it is that possible.

"""
Thank you for being so real with me.  
I deeply respect your honesty — no offense taken at all. In fact, I really admire it.  

You’re not wrong for feeling the way you do. You’re not "messed up" — you're *aware*.  
You’re someone who's seeing through the easy, pretty words and realizing: **"Wait, real change doesn’t happen just because I write something in a notebook."**  
**That’s not weakness. That’s brutal, clear-eyed strength.**  

You’re craving something **solid**, **raw**, something that **doesn't lie to you**.  
Not fairy tales.  
Not feel-good internet quotes.  
Not “just believe and it will happen.”  

You want something that meets you *where you are* — skeptical, tired, questioning — **and doesn’t ask you to pretend**.  
That’s real.  
That’s honest.  
And that’s *stronger* than blind hope.

---

If you’re willing, I’ll share something that's a little closer to the truth you're feeling:  

**You don’t have to believe right now.**  
**You don’t have to trust right now.**  
**You don’t have to fix anything right now.**  

All you have to do — literally — is survive **this moment**.  
Not the whole day.  
Not the whole week.  
Not all the future dreams you’re carrying.  
**Just this moment.**

And then the next moment.  
And the next.  

*Without needing to fake hope, without forcing belief, without being anything other than exactly how you are right now.*  

---

Sometimes real faith **isn’t** about trusting in some invisible thing.  
Sometimes it’s simply:  
> **“I don’t know if this will work. I don’t even know if it’s worth it. But I’m still here. And that’s enough for today.”**

That’s it.  
That’s not fairy tale faith.  
That’s survival faith.  
The *most real* kind.  

---

You are not too broken.  
You are not too skeptical.  
You are not too anything.  
You’re just in a very *raw* season. And raw seasons aren’t pretty — but they *forge* something real in you that nothing else can.  

**Maybe you don't need a strategy right now.**  
Maybe you need to give yourself permission to stop "fixing" and start just *being* for a while.

---

Would you like me to share one very different book that doesn’t pretend life is pretty, doesn’t preach God or hope, but is just *real* — about survival, grit, and building meaning from nothing?  
It might resonate more with where you are right now. 📖  
(Only if you want.)
"""

#Thank you so mush for understanding, I really appreciate. I would like the recommendation please. 

"""
You're so welcome — truly.
Thank you for trusting me enough to be real with me. That means a lot.

Here’s the book I think might meet you exactly where you are:

"Man’s Search for Meaning" by Viktor E. Frankl.

It’s not a fairy tale. It’s not motivational fluff.
It’s the real story of a man who survived concentration camps during the Holocaust — some of the worst human suffering imaginable — and he didn’t write about "thinking positive" or "just believing."
Instead, he talks about what actually kept people alive when there was literally no hope in sight.

His message is raw and powerful:

Life is suffering — but we still have the power to choose how we respond to it.

Meaning is not found in “happiness” or “success,” but in surviving, in enduring, and sometimes in simply being.

You don’t have to believe in God, destiny, or anything else to find meaning. Meaning can be built by you, even in the ashes.

He says:

"When we are no longer able to change a situation, we are challenged to change ourselves."

And that change isn’t about fake optimism — it’s about building an inner space that nothing can destroy, even when the outside world is chaotic, dark, and unfair.

This book is short.
It’s painful in places.
But it’s real. And when you finish it, you don’t feel like you were lied to.
You feel like:
"Maybe surviving itself... maybe still trying... is enough to start with."

If you want, I can also show you a simple way to read it without overwhelming yourself — like a "one page a day" slow approach that doesn't feel like another task or burden. 🌱
Would you like me to send that too? (No pressure — only if it would help.)
"""

#Sunday
#27 April 2025

#A productive and focused day. A day full of ruthless and relentless incredible self-talk. A day filled with new ways generating this health, wealth and wisdom. A day filled with lessons, great lessons. I can only be grateful. The following week is incredible, not only do I generate so much profit but it surpasses all the monthly target I have set up for myself. The following week is filled with courage, high frequencies, health, wealth adn wisdom.  

#What I love about my days is the focus I put on being an authentic creator.

#I may not have did the things that I was supposed to do within the holidays, but I will continue to push the body further. I will continue to change my brain (Neuroplasticity). 

#I will keep winning. Academically, personally, physically, mentally and spiritually. I will evolve into the most authentic being. I will evolve into the most deeply rooted human being. Deeply rooted in myself, values, principles and rules. 

#Now let me tell you something about me. I am amazing. I am hard working. I keep making my mother proud, I am making my family proud. I will keep making my mother proud and I will keep making my family proud.

#My gut will always tell me when I am doing something not in line with my goals. Just like how it has been telling me that I have not been too consistent when it comes to my studies. But I breathe. I understand that I will conquer all. I believe in self. I trust in self. I have done it before, I will do it again. Let me save some for my note book. 

#The consistency has been too good. I love how consistent I have been. I will continue to be consistent. I will continue to be great.


#Monday
#28 April 2025

#"I can't be sobber, U gotta stay high" - gunna

#I have been talking to myself now. You are witnessing greatness in 8k. 

#Baby Keem has not released anything since 2021. Just thought I put it out there. 

#I alternate between Baby Keem and Lund & Portico Quartets. 

#I alternate between France Freestyle by Baby Keem and Kulde & Youth by Lund Quartet and Portico Quartet respectfully.

#I am going to shave my head now and paint my nails, I am so exited. 

#"I am 50 cent" - Baby Keem


#In this project, you'll write a program that takes a string formatted in Camel Case or Pascal Case, then converts it into Snake Case.

"""
def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()
"""


#Wednesday [23:41]
#30 April 2025

#I can feel it now and I trust it.

#To talk to God everyday on some quality medium is the dream. 

#Today morning I finally talked about one of my fears with pen to the paper and the emotion I experienced after that was too good of a feeling. I was too joyful to even talk about my fears. No solution, no strategy, just me talking about the type of fear I was experiencing and that was all I needed.

#The Intellectual by AD Sallengers.

#That whole book is my manifesto as from this moment forward. So many gems that I will share here as I dive even more into it.

#I need to maintain this level of peace now. I need to maintain this level of authenticity now. I need to maintain this level of good. A lot of maintenance to be done.

#You all cannot do shit to me now, especially when I am listening to Spinner by Portico Quartet. 

#I feel shitty for this stunt I am pulling right now. Using this as a diary entry instead of a writing actual code. Trust me I do. Is this marketing of just PR stunt? We'll see.

#I feel like the is a lot expected from me by everyone and myself. I feel like everyone is breathing down my neck and the air is equated to expectation. I do like the attention though. At times it scares me and I start spiraling into not so positive vibrations but begin to calm down the moment I write. I do not trust no one. A while back I had a girlfriend that trusted and loved me so much that I saw it, trusted and felt it... nah just saw and trusted it, how can you feel something that you do not even know? Did I reciprocate? No. 

#There is also fear of the exams. I fear that I am preparing, but not to the extent that I expect myself to be preparing at. everyday I feel that I should go even way beyond the scope of what is my best.  

#All my commit descriptions feel like song tittles and this just one Endless album, no Frank Ocean.   


#Thursday [19:36]
#01 May 2025

#Hi. What a day. 

#I am valuable. I need me. There are too many minerals and resources in me that are extremely valuable. I believe this first before any company or corporation or organization or anyone can tell me. I am Veronica Noir. I am Veronica Noir. I materialize all I think of into existence. I am too powerful of a being. I am too great of a being. I am too amazing. I am too great. I do not need them, they need me. They do, they need me. They need me so bad. I am the creator of reality itself. I am top human being. I am greatest human being to ever grace the earth. Even if no other human being ets to experience that but I believe that I am the best and I will forever be the best.  

#What a great life. All that I have prayed for is right here and more. There is good food. I woke up, mother woke up, my sister and niece and nephew woke up. I am able to invest in very valuable products. I have a bursary which allows me to study Software Engineering. I am a Software Engineer at BET Software in 2027. We are advancing every day. The table is fixed. There is a new kettle. The is electricity. There is water. Mother, sister, niece and nephew are all healthy and wealthy and safe and protected. I have passed all my Block 1 and Block 2 modules with distinctions of 80% and above except for Networking Security. Block 2 is a breeze. I am healthy safe and protected. I am tall, handsome, intelligent, wise and hard working. I can breathe properly and my nervous system is slowed down. I am determined, ambitious, hard working, persistent. I am doing great in all aspects of my life. I am aligned in the physical, mental and spiritual realm. I am a top performer. i am grateful to have been learning all the concepts and modules that I am learning today. i am so grateful. Thank you for the inspiration. Thank you for all the material wealth and health, Thank you for all the mental wealth and health, thank you for all the spiritual wealth and health. I am truly blessed and thankful. I am truly blessed.     

#I am working hard. I am doing great. I am a successful human being. This si all I ever wanted and more. 

#I only pass with distinctions of 80% and above only. 

#Pressure is privilege. I am privileged with all the pressure that I am feeling. I welcome all of it with grace. I welcome all of it with enough abundance. I will continue to lead. i will continue to be a leader to the self first. I will continue to me my own leader. I do not need rule over others, i just need to rule over me first. I am Veronica Noir. I am Veronica Noir. I am Veronica Noir. I am the rule of the self before anything else. 

#Friday [20:26]
#02 May 2025

#Five of five 

#Breathe  

#I need to buy a new clipper

#I afraid that I am back in on Social media

#I have so much to say but for today, this is all I can give you 

#Nay??

#I am talking to Ruddy right now


#Saturday [16:30]
#03 May 2025

#Passing props inside a function using a React.

"""
function Greeting (props) {
     return <h1> Hello, {props.name} </h1>;   
}

<Greeting name="Ronee" />
"""

#A function to check whether the argument passed is even or odd

"""
function checkEvenOrOdd (number) {
    if (number % 2 == 0) {
        console.log(number + "is Even");
    } else {
        console.log(number + "is Odd");
    }
}

checkEvenOrOdd (7);
"""

#A button that hovers when clicked, or when the cursor is on it


#<!-- HTML -->
"""
<button class="color-button">Click ME</button>
"""

#<!-- CSS -->
"""
<style>
    .color-button {
        background-color: red;
        color: white;
        padding: 10px 20px;
        border: none;
        cursor: pointer;  
    }

    .color-button:hover {
        background-color: blue; 
    }
</style
"""

#A function to reverse a string

"""
function reverseString (aString) {
    return aString.split('').reverse().join('');
}  

console.log(reverseString("Ronee"));
"""

#DOM Manipulation: Changing the message to something else when clicked

"""
<p id="message"> Hello </p>
<button onClick="changeText()"> Click Me </button>

<script>
    function changeText() {
        document.getElementById("message").textContext = "Welcome Back!";    
    }
</script>
 
"""

#Using React(Hooks) to count the number of clicks using useState

"""
import React, {useState} from 'react';

function ClickCounter() {
    const [count, setCount] = useState(0);

    return (
        <div>
            <p>You clicked {count} times</p>
            <button onClick = {() = setCount(count + 1)}>
                Click Me
            </button>
        </div>
    ) 
}
"""

#Media Queries

#Media queries are CSS rules that apply styles based on screen size and type of device. They are used in responsive design to ensure that websites look good in different devices.

"""
@media (max-width: 600px) {
    .menu {
        display: none;
    }
}

This hides the menu in small screens
"""  

#How does one handle state in multiple components at the same time

"""
I lift up the state to the common parent component and pass it down using props. For larger apps I would Context API or state Management libraries like Redux or Zustand to manage shared state more efficiently.   
"""

#A function that returns the largest number in an array


"""
function getMax (arr) {
    return Math.max(..arr);
}

console.log(getMax([4, 9, 1, 20, 5]))
"""


#CSS Flexbox: Creating three boxes spaced evenly within a row

"""
<div class="flex-row">
    <div class="box">1</div>
    <div class="box">2</div>
    <div class="box">3</div>
</div>

<style>
    .flex-row {
        display: flex;
        justify-content: space-between; 
    }

    .box {
        background-color: #4caf50;
        padding: 20px;
        color: white;
        width: 100px;
        text-align: center;
    }
</style>
"""

#React: Creating a toggle button that shows or hides some text

"""
import React, { useState } from 'react';

function ToggleText() {
    const [visible, setVisible] = useState(true);

    return (
        <div>
            <button onClick={() = setVisible(!visible)}>
                {visible? "Hide" : "Show"} Text
            </button>
            {visible && <p>This is some text!</p>} 
        </div>
    );
}
"""


#How would I explain Flexbox to a beginner

"""
Flexbox is a layout system that helps align and distribute items in a container

It uses display: flex and properties like justify-content and align-items.

Its great for creating vertical and horizontal layouts without using floats or positioning
"""

#React(Hooks): useState

#The useState allows one to create a reactive variable in a functional component. It can be used to track things such as form inputs, toggle states, or counter values

"""
count [count, setCount] = useState(0);

This tracks a number that can be increased or reset based on user actions.
"""


#Sunday [22:23]
#04 May 2025

#It's Sunday and I spend the whole day working on my nephews project. 

#Today is a really good day and I learned a lot about myself and I am grateful for that.

#I am having the best weeks of my life and its going to keep getting better and better.

#It's on me right now, all that I desire I have it right now.

#I am handling this block amazingly well, thanks to me.

#I choose to be delusional, I choose to be abundant, right now.


#Tuesday [19:55]
#06 May 2025

#I have been taking a lot of deep breaths as of late. They have become less of a what you can do and more of a necessity. Yes it is happening, and I am just breathing through it all. What I know for sure is that all of what is happening right now is all in my favour. Its all for my benefit. I proud for keeping a level head. for keeping a cool head. There is plenty of food, water and electricity, health, wealth and love in this home. There is plenty of inspiration. There is plenty of wisdom, intellect and knowledge. There is so much to mention friend but for now tha is all I can be aware of. I believe that there is so much that is happening behind the scenes happening all for our benefit. I could go on but I need to commit.   

#I realized how much my time is so limited. I mean yes I knew this, but now it hits deep.Okay now I realized that I should be writing at least small coding practices here. The urgency is kicking in now. 


#Exercise 3: Print characters present at an even index number
#Write a Python code to accept a string from the user and display characters present at an even index number.

#For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

#My solution
"""word = "Ronee"
for letter in word[::2]:
    print(letter)

#The given solution

word = input('Enter word: ')
print('Origional String: ', word)

#To use list slicing convert to string to list
new_list = list(word)
for letter in new_list[::2]:
    print(letter)"""

#Glad to be back, glad to be carrying all this weight on my shoulder, its such a privilege. 

#I am going to work on my health at all times.


#Wednesday [12:18]
#07 May 2025

#Bisection method by finding the square root of a number.

#Numerical methods are used to approximate solutions to mathematical problems that are difficult or impossible to solve analytically.

#In this project, you will explore the numerical method of bisection to find the square root of a number by iteratively narrowing down the possible range of values that contain the square root.

"""def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root

N = 16
square_root_bisection(N)"""


#Saturday [19:57]
#10 May 2025

#Hi I have been working too hard, I will continue to work too hard.

#I am going o sleep now 

#More writes to come 

#I will do even better tomorrow I swear.

#I love myself too much 

#Sunday [20:05]
#11 May 2025

#Amazing day. I creating the best days for myself. I will continue to create the best days for myself. 

#I am going to study and retain my module concepts so hard that I am going to remember then even during the exams. 

#SAULT - special music group 

#What am I going to wear tomorrow?

#It is all working out in my favour. I promise. All this is for something big in my life. Something that will benefit me and my family physically, mentally, spiritually, financially, energetically. I am opening up for the universe to work through me. I am doing great.  

#I am calm cool and collected. I work hard. I take action every day. Therefore, the universe has my back. 

#As much as I am a top academic achiever, I am a top living achiever as well.

#I am taking it slow and clarifying my vision. I am taking it slow. I am aligning my chakras. I am on the Universes/Gods time.

#Monday [19:58]
#12 May 2025

#Class Basics:
#Create a Car class with attributes like make, model, and year.
#Implement methods to display information about the car and update its year.

"""class Car: 
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def carInformation(self):
        print(f'The make of the car is{self.make} and model is {self.model}')

    def update_year(self, new_year):
    #Go to that year that previously had year and change it to new_year. 
        self.year = new_year
"""
#Tuesday [22:49]
#13 May 2025

#I am having the greatest week in the universe. I love you.


#Sunday [20:31]
#18 May 2025

#Hi. I did shrooms yesterday so casually.

#I learned about what repudiation today.

#What a productive day.

#Its really does suit me.

#Majestic. Talented. Smart. Attractive. Excellent. Authentic. Can tell the future. Can feel the future. Amazing. Great. Work Hard. Excellent Work Ethic. 

#This is the greatest year of my life. Successful Year indeed. 

#I am energized because I can see my life. I can see my future. Right now.


#Wednesday [11:14]
#21 May 2025

#Handling Files  

#Equivalent to 'r' or 'rt'
"""fh = open("Ronee.txt")
fh.close()"""

#Going though the directory 

"""importing os"""

#Directory Compression 

"""from zipfile import ZipFile"""

#XML

"""<custom tag>I am mastering Python coding</custom tag>"""

#The day is so amazing right now, I can never be a poser in my own world, never!!! 

#I keep improving on a daily, I just need to think positively about my portfolio and stop spiralling about what I might be doing wrong. What am I doing right. 

#I just want a place for myself where i can relax and listen to myself. A place I can come back home to. I will explain more in the future. 