pan=input("ENter pan-Card: ")
first_name=input("Enter first_name: ")
last_name=input("Enter last_name: ")
# password=first_name[5:]+last_name[:2]+'@'+pan[5:10]
# password="{}{}@{}".format(first_name[5:],last_name[:2],pan[5:10])
# password=(f"{first_name[5:]}{last_name[:2]}@{pan[5:10]}")
password=("%s%s%s%s"%(first_name[5:],last_name[:2],"@",pan[5:10]))
print("password is :",password)