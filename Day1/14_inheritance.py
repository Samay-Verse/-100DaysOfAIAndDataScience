# class person:

#     def __init__(self,fname,lname) -> None:
#         self.firstname = fname
#         self.lastname = lname

#     def printName(self):
#         print("FirstName:",self.firstname)
#         print("LastName",self.lastname)

# class child(person):
#     pass

# obj1 = child("Samay","Powade")
# obj1.printName()


# class teacher:

#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def printName(self):
#         print("First Name", self.fname)
#         print("Last Name:", self.lname)


# class student(teacher):
#     def __inti__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def fun(self):
#         print(self.fname)
#         print(self.lname)


# o1 = teacher("Samay", "Powade")
# o1.printName()
# o2 = student("Vedant", "Patil")
# o2.fun()


# constructor override

# class company:

#     def __init__(self, company1, company2) -> None:
#         self.com1 = company1
#         self.com2 = company2
#         x = 2000
#         y = 3000
#         print(y - x)

#     def printName(self):
#         return f"Company 1:{self.com1},  company 2: {self.com2}"


# class subCompany(company):
#     def __init__(self, com1, com2):
#         # super().__init__( com1, com2)
#         company.__init__(self,com1,com2)
#         x = 10
#         y = 20
#         print(x + y)


# child = subCompany("Microsoft", "facebook")
# print(child.printName())


# class person0:
#     pass

# class person(person0):
#     def __init__(self,n1,n2):
#         self.n1 = n1
#         self.n2 = n2

#     def print(self):
#         print(self.n1)
#         print(self.n2)

# class person2(person):
#     def __init__(self, n1, n2):
#         super().__init__(n1, n2)
#         self.myname = "Samay"
#         self.Friend1 = "Vedant"
#         self.Friend2 = "Shivam"
#         self.Friend3 = "Shiriniva"

# child = person2(10,20)
# child.print()
# print(child.Friend1)
# print(child.myname)
# print(child.Friend2)
# print(child.Friend3)

# obj1 = person


# class sample1:

#     def __init__(self, fname, lname) -> None:
#         self.fname = fname
#         self.lname = lname

#     def Name(self):
#         return f"{self.fname} {self.lname}"


# class sample2(sample1):
#     def __init__(self, fname, lname, year) -> None:
#         super().__init__(fname, lname)
#         self.yearof = year


# obj = sample2("Samay", "Powade", 2023)

# print(obj.Name())
# print(obj.yearof)


# adding function

# # Input tuple using class and object

# class operetion:
#     def inputList(self, list1):
#         for x in range(3):
#             number = int(input("Enter the Number :"))
#             list1.append(number)


# obj = operetion()
# tuple1 = ()
# temp = list(tuple1)
# obj.inputList(temp)
# tuple1 = tuple(temp)
# print(tuple1)


# class samTec:

#     def __init__(self, Name, Date, Network) -> None:
#         self.Name = Name
#         self.Date = Date
#         self.Network = Network

#     def info1(self):
#         print("SamTec Info:")
#         print(self.Network)
#         print(self.Date)
#         print(self.Name, "\n")


# class subtec(samTec):
#     def __init__(self, Name, Date, Network, Marketing) -> None:
#         super().__init__(Name, Date, Network)
#         self.range = Marketing

#     def show(self):
#         print("SunTec Info:")
#         self.Network = "30Cr"
#         return f"{self.Date} {self.Name} {self.Network} {self.range}"


# object = subtec("Microsoft", "11-11-2005", "20Cr", "20%")
# object.info1()
# print(object.show())


# class company:

#     def empolyes(self):
#         pass

#     def manager(self):
#         pass


# obj = company()


# obj.empolyes()


# types of inheritance


# multilevel inheritance


# class operetion1:
#     list1 = ["1EE", "2EE", "3EE", '4EE']
#     a = 10
#     b = 20
#     c = 40

#     def show1(self):
#         if self.a > self.b and self.a > self.c:
#             print("The A is Greater")
#         else:
#             if self.b > self.c:
#                 print("The b is greater.")
#             else:
#                 print("The C is greater")


# class operetion2(operetion1):

#     tuple1 = (10, 20, 30, 40)

#     def show2(self):

#         temp = list(self.tuple1)
#         temp.append(50)
#         temp.append(70)
#         temp.insert(1, 1000)
#         temp.sort()
#         self.tuple1 = tuple(temp)

#         print(self.list1)


# class operetion3(operetion2):
#     def show3(self):
#         print(self.tuple1)


# obj1 = operetion1()
# obj2 = operetion2()
# obj3 = operetion3()

# obj3.show1()
# obj3.show2()
# obj3.show3()


# multiple constructor in inheritance

# class company1:
#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.age = age


# class company2(company1):21-
#     def __init__(self,name,age,year) -> None:
#         super().__init__(name,age)
#         self.year = year


# class company3(company2):
#     def __init__(self,name,age,year,std) -> None:
#         super().__init__(name,age,year)
#         self.std = std
    
#     def show(self):
#         print(self.name)
#         print(self.age)
#         print(self.year)
#         print(self.std)

# obj = company3("Samay",18,2023,"CO5I")
# obj.show()



# class empolye1():
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age 
#         self.salary = salary 

# class childEmploye(empolye1):
#     def __inti__(self,name,age,salary,id):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.id = id
# obj1 = empolye1("Samay",18,100000)  
# print(obj1.age)


class sample1():
    def __init__(self,name,age,email,password) -> None:
         self.name = name 
         self.age = age 
         self.email = email 
         self.password = password
   
         

class sample2(sample1):
     def __init__(self, name, age, email, password) -> None:
          super().__init__(name, age, email, password)
        
        
class sample3(sample1):
     def __init__(self, name, age, email, password) -> None:
          super().__init__(name, age, email, password)


obj2 = sample3("Samay",18,"Samay@gmail.com",12345)

print(obj2.name,obj2.age,obj2.email,obj2.password)

