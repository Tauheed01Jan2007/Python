a = 12
b = "Hello"
try:
    c = a+b
except TypeError:
    print("Error Message: Controlledd integer and string")
    
x = 20
y = 0
try:   
    di = x/y
    print(div)
except ZeroDivisionError:
    print("ZeroDivisionError")
except TypeError:
    print("TypeError")
    
    
def funct(a):
    if a<4:
        b = a/(a-3)
    print("Value of ",b)

try:
    funct(5)
except ZeroDivisionError:
    print("ZeroDivisionError")
except NameError:
    print("NameError")