marks=int(input("Enter the marks: "))
if marks>100:
    print("Marks should not be greater then 100")
elif marks<0:
    print("Marks should not be less then 0")
elif marks>90:
    print("A+")
elif marks>80:
    print("A")
elif marks>70:
    print("B+")
elif marks>60:
    print("B")
elif marks>50:
    print("C+")
elif marks>40:
    print("C")
else:
    print("fail") 