pwd = 2345
mypwd = int(input("Enter your password: "))
while (pwd>0):
    if (pwd != mypwd):
        pwd = 2345
        mypwd = int(input("Enter your password: "))
    else:
        print("Unlocked!!")
        break