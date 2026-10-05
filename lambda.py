# a=int(input("Enter a: "))
# d=lambda a:a*a*a
# print(d(a))

# x = lambda a,b:(a*a)+(b*b)-2*(a*b)
# print(x(2,4))
 
d = lambda a:a+a
num = [1,2,3,4]
result = map(d,num)
print(list(result))
  
#   #string print
# str="Tauheed"
# (lambda str:print(str))(str)

r = int(input("Enter r:"))
h = int(input("Enter h: "))
#num = [r,h]
a = lambda r,h: 3.14*r*r*h

#res = map(a,num)
print(a(r,h))