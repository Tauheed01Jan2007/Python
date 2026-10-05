#Ques 10
n = 123456789
s = 0
c = 0
while(n>0):
    r = n%10
    n = n//10
    if r%2==0:
        s = s + r
        c = c+1
print(s)