def factroial(n):
    sum = 1
    for i in range(1,n+1):
        sum = sum * i
    print(sum)
a = int(input("How many time you want to check: "))
for i in range(a):
    n = int(input("Enter the num: "))
    factroial(n)