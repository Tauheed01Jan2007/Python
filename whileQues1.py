#Ques 1 
n = 100
i = 0
sum = 0
while i<=n:
    if n%2==0:
        sum += i
        i += 2
print(sum,end=" ")