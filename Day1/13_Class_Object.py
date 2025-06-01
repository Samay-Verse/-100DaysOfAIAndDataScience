# # Declare the class
# class MyClass:
#     x = 10
# print(MyClass)

# Creation Object

# class Myclass:
#     x = 10000

# obj = Myclass()

# print(obj.x)

# class sample:
#     x = 10
#     print(x)

# class Myclass:

#     def  __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Myclass("Samay",18)

# print(p1.name)
# print(p1.age)


# constructor 

# class myclass:

#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.age = age
    
#     def printInfo(self):
#         print(self.name)
#         print(self.age)

# o1 = myclass("Samay",18)
# o1.printInfo()





# class Myclass:
#     def __init__(self):
#         mydict = {
#             "Name": "Samay",
#             "Age": 18,
#             "Class": "CO5I",
#             "Collage": "gramin Tecnical and management Campus"
#         }


# obj1 = Myclass()


# class factorialCalculation:
#     def factorial(self, n):
#         if n == 0:
#             return 1
#         else:
#             return n * self.factorial(n - 1)


# claculator = factorialCalculation()
# result = claculator.factorial(5)
# print("The factorial number is :", result)

# class listInfo:
#     def __init__(self):  # it is called as Constructor
#         list1 = []
#         for x in range(4):
#             items = int(input("Enter the list items:"))
#             list1.append(items)
#         print(list1)


# obj = listInfo()

# class Myclass:
#     x = 10
#     y = 20


# Student1 = Myclass()
# Student2 = Myclass()
# Student3 = Myclass()

# Student1.name = "Samay"
# Student1.age = 18
# Student1.std = "CO4I"
# Student1.Id = "C1AF"


# Student2.name = "Shivam"
# Student2.age = 18
# Student2.std = "CO4I"
# Student2.Id = "C2AF"


# Student3.name = "Vedant"
# Student3.age = 18
# Student3.std = "CO4I"
# Student3.Id = "C3AF"

# print("The Student 1 is:")
# print(Student1.name)
# print(Student1.age)
# print(Student1.std)
# print(Student1.Id)
# print("-"*10)
# print("The Student 2 is:")
# print(Student2.name)
# print(Student2.age)
# print(Student2.std)
# print(Student2.Id)
# print("-"*10)
# print("The Student 3 is:")
# print(Student3.name)
# print(Student3.age)
# print(Student3.std)
# print(Student3.Id)
# print("-"*10)

# print(Student1.__dict__)
# print(Student2.__dict__)
# print(Student3.__dict__)

# print(Myclass.__dict__)


# class student:

#     def __str__(self) -> str:
#         return f"Name is {self.name}.Age is {self.age}.Std is {self.std}"

# samay = student()
# samay.name = "Samay"
# samay.age = 18
# samay.std = "Co4I"

# # print(samay)

# class student:
#     def __init__(self, N, A, S) -> None:
#         self.name = N
#         self.age = A
#         self.std = S

#     def __str__(self) -> str:
#         return f"Name:{self.name}. \n Age:{self.age}. \n Std:{self.std}"
# list = ["Samay","Vedant","Sachin"]
# object = student(list,18,"Co5I")
# print(object.__dict__)
# print(object.name)

# print(type(object))
# 56 


# Changing class variabal 

# class Company:
     
#      company = "Apple"

#      def myFunction(self):
#           print(f"Myname is: {self.name} And company name is : {self.company}")

#      @classmethod
#      def changeCompany(cls,Newcompany):
#           cls.company = Newcompany

# c1 = Company()
# c1.name = "Samay"
# c1.myFunction()
# c1.changeCompany("Tesla")
# c1.myFunction()

# print(Company.company)


# class Myclass:
     
#      myDict = {
#           "name":"Samay",
#           "Std":12,
#           "Age":18,
#           "Collage":"gramin tecnical and management campus",
#           "Staf":"Wahi Sir"
#      }

#      def Info(self):
#           for key,name in self.myDict.items():
#                print("Key:",key)
#                print("Value",name)
#                print("-" * 10)

#      def ChangeValue(cls):
#           cls.myDict["name"] = "Vedant"

# o1 = Myclass()
# # o1.Info()
# o1.ChangeValue()
# o1.Info()

# print(Myclass.myDict)

# class myclass:
#     name = "Samay"

#     def Pname(self):
#         print(f"The Name is: {self.name}")
#     @classmethod
#     def changeName(self,NewName):
#         self.name = NewName

# o1 = myclass()
# o1.Pname()
# o1.changeName("Vedant")
# o1.Pname()
# print(myclass.name)

# Self parameter use as any name

# class sample:
#     n1 = 10
#     n2 = 20
#     n3 = 30
    
#     def Number(abc):
#         print(abc.n1)
#         print(abc.n2)
#         print(abc.n3)

# o1 = sample()
# o1.Number()


# modify object property and delete object property

# class myclass:
#     n1 = 20
#     n2 = 30
#     n3 = 40
#     n4 = 60
    
#     def printValues(self):
#         print(self.n1)
#         print(self.n2)
#         print(self.n3)
#         print(self.n4)

# o1 = myclass()
# o1.n1 = 200
# o1.n3 = 300
# print("Values Changing after:")
# o1.printValues()
# print("-"*10)
# print(myclass.n1)
# print(myclass.n3)

# del o1.n1 
# o1.printValues()


class samay:
    a = 10
    b = 20

    def function(self):
        print(self.a + self.b)
o1 = samay()
o1.function()
