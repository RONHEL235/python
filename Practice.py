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

class Bike:

    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material

    def brake(self):
        print("Braking")

red_bike = Bike ("Red", "Carbon fiber")
blue_bike = Bike("Blue", "Steel")    