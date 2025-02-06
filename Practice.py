#Scopes

def enclosing_func ():
    m = 13

    def local():
        print(m)

    local()

m = 5
print(m)

enclosing_func()