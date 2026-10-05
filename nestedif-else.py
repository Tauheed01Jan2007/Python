n=int(input("Enter a: "))
if n>30:
    print("Number is greater than 10")
    if n%5==0:
        print("Number is also multyply of 5")
    else:
        print("Number is not multyply of 5")
elif n%10==0:
    n=n*2
    print(n)
else:
    if n%2==0:
        print("number is even")
    elif n%3==0:
        print("Number is multyply is 3.")
    else:
        print("I don't not.")
        if n%7==0:
            print("Multyply is 7.")