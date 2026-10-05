# Ques 3
n = 123456789
c = 0
while(n>0):
    r = n%10
    n = n//10
    if r%2==0:
        c = c+1
print(c)