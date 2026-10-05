#Ques 8
n = 12345
m = n
n = n // 10
t = n
c = 0
while (n>0):
    c = c+1 
    n = n//10
    
while m>10:
    m = m//10
    mid_value =t - m*10**(c-1)
print(mid_value) 