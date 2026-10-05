i = 1
while i<=5:
    if i == 3:
        break
    print(i,end=" ")
    i += 1
    
n = int(input("\nEnter the number: "))
i = 1
while i<=n:
    if i % 3 == 0:
        i += 1
        continue
    print(i,end=" ")
    i += 1
    

while(1):
    n = int(input("\nENter the number: "))
    if n == 42:
        break
    print(n)