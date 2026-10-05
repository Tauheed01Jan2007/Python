def fun(var):
    letters = ['a','e','i','o','u']
    if var in letters:
        return True
    else:
        return False
seq = ['d','e','r','e','r','t','y','u']
filted = filter(fun,seq)
print("The filter letter are")
for s in filted:
    print(s)
    

def even(number):
    if  number%2==0:
        return True
    else:
        return False
seq = [1,2,3,9,6,5,3,4,5,6,54,7,8,9,0]
filted = filter(even,seq)
print("The filter letter are")
for s in filted:
    print(s,end=" ")
    

seq = [2,3,4,56,77,23,6,77,89,9,00,9,5,6]
a=filter((lambda x:x%2==0),seq)
x = list(a)
for i in x:
    print(i,end=' ')
         
         
    #how to read
#split()
#strip()
#join()