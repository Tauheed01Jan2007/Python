#====================================================
#Create email
fname = input("enter first_name: ")
lname = input("enter last_name: ")
company_name = input("enter company_name: ")
# email = (fname+'.'+lname)+'@'+company_name+'.com'
# email = "{}.{}@{}.com".format(fname,lname,company_name)
email = "{1}.{0}@{2}.com".format(fname,lname,company_name)
print("Email Id is :",email)
#====================================================
#Create Password
mob_no = (input("Enter mobile number: "))
dob = (input("Enter date_of_birth: "))
# password = mob_no[6:]+'@'+dob[6:]
password = mob_no[6:]+'@'+dob[-4:]
print("password is: ",password)
#====================================================