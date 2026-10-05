def fact(n):
    f=1
    for i in range(2,n+1):
        f=f*i
    print(f)
fact(5)



def fact(n):
    f=1
    for i in range(2,n+1):
        f=mul(f,i)
    print(f)
def mul(a,b):
    return a*b
fact(5)