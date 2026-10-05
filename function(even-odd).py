def odd_even(x):
    if x%2 == 0:
        print("Even")
    else:
        print("Odd")
n= int(input("How many time you want to check: "))
for i in range(n):
    x = int(input("Enter the number: "))
    odd_even(x)  
