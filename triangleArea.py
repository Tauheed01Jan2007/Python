# import math
a= int(input("Enter a: "))
b= int(input("Enter b: "))
c= int(input("Enter c: "))
s=(a+b+c)/2
x=s*(s-a)*(s-b)*(s-c)
# Area=pow(x,0.5)
Area=x**0.5
print("Area is : ",Area)