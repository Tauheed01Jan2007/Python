n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()



for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    for k in range(2*i):
        print(" ",end=" ")
    for p in range(n-i):
        print("*",end=" ")
    print()
    
    
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for k in range(n-i-1):
        print(" ",end=" ")
    for p in range(n-i):
        print("*",end=" ")
    print()