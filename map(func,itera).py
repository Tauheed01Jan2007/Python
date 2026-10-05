def Add(n):
    return n+n
num = [1,2,3,4]
result = map(Add,num)
print(list(result))



def fact(n):
    if n==1 or n==0:
        return 1
    else:
       return n*fact(n-1)
num = [1,2,3,4,5]
result = map(fact,num)
print(list(result))