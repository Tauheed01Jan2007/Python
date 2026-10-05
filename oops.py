# class Fruits:
#     taste = "sweet"
#     price = 200
# Banana = Fruits()
# print(Banana.taste)

# Apple = Fruits()
# print(Fruits.price)

#====================================================================================================================

# class Person:
#     # name = "Rahul"
#     # age = str(20)
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(f"Hello ! my name is {name} and my age is {age}")

'''
p1 = Person("Rahul",20)
p2 = Person("Shivam",25)
p3 = Person("Abhishek",10)
'''

# n = input("Enter name: ")
# a = input("Enter age: ")
# p4 = Person(n,a)



#==========================================================================================================================
# class Student:
#     def __init__(self , name, age, email_id):
#         self.name = name
#         self.age = age
#         self.email_id = email_id
        
#     def greeting(self):
#         print(f"Hello ! my  name is {self.name} and my age is {self.age} and my email_id is {self.email_id}")
        
# name = input("Enter name: ")
# age = input("Enter age: ")
# email_id = name+age+"@gmail.com"
# s1 = Student(name , age , email_id.lower())
# s1.greeting()

#=====================================================================================================================

# class Cube:
#     def __init__(self , length , bright , height):
#         self.length = length
#         self.bright = bright
#         self.height = height
        
#     def Volume(self):
#         volume = self.length * self.height * self.bright
#         print("Volume = "+str(volume))
    
#     def Total(self):
#         total = 2 * (self.length *  self.bright) *self.height
#         print("Total surface area = "+str(total))
        
#     def Lat_surface(self):
#         lat_surface= 2 * (self.length *  self.bright + self.bright * self.height + self.height * self.length) 
#         print("Total surface area =" +str(lat_surface))
        
# length =int(input("ENter legth: "))
# bright = int(input("ENter bright: "))
# height = int(input("ENter height: "))


# c = Cube(length , bright , height)
# c.Volume()
# c.Total()
# c.Lat_surface()

#==================================================================================================================

class Calculater:
    def __init__(self, num):
        self.num = num
    def factroial(self):
        fact = 1
        for i in range(1 , self.num + 1):
            fact = fact * i
        print(fact)
        
    def fibanacci(self):
        fib1 = 0
        fib2 = 1
        for i in range(1,self.num-1):
            fibN = fib1 + fib2
            fib1 = fib2
            fib2 = fibN
        print(fibN)

num = int(input("Enter num: "))
f1 = Calculater(num)
f1.factroial()
f1.fibanacci()

# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(fact)