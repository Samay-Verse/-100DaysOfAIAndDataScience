# # class company1:
# #     def __init__(self, name, network) -> None:
# #         self.name = name
# #         self.network = network

# #     def show(self):
# #         print("Company name:", self.name)
# #         print("Company Network", self.network)


# # class company2:
# #     def __init__(self, name, network) -> None:
# #         self.name = name
# #         self.network = network

# #     def show(self):
# #         print("Company name:", self.name)
# #         print("Company Network", self.network)


# # class company3:
# #     def __init__(self, name, network) -> None:
# #         self.name = name
# #         self.network = network

# #     def show(self):
# #         print("Company name:", self.name)
# #         print("Company Network", self.network)


# # com1 = company1("Microsoft", 200000000)
# # com2 = company2("Facebook", 300000000)
# # com3 = company3("Google", 400000000)

# # com1.show()
# # print("-"*10)
# # com2.show()
# # print("-"*10)
# # com3.show()
# # print("-"*10)

# # for x in (com1, com2, com3):
# #     x.show()
# #     print("-"*10)


# # inheritance polymorphism


# class industry:
#     def __init__(self, Name, age) -> None:
#         self.name = Name
#         self.age = age

#     def show(self):
#         print("This is the Company groups:", self.name)
#         print("This is the age of company:", self.age)


# class company1(industry):
#     def show(self):
#         print("This is the Company 1 :")


# class company2(industry):
#     def show(self):
#         print("This is the Company 2 :")

# def call()


# obj = industry("Microsoft",20)
# obj1 = company1("Mic",20)
# obj2 = company2("Micrcudnudcosoft",20)

# # for x in (obj,obj1,obj2):
# #     print(x.name)
# #     print(x.age)
# #     x.show()


# class animal:
#     def sound(self):
#         pass


# class dog(animal):
#     def sound(self):
#         print("Boooo...")


# class cat(animal):
#     def sound(self):
#         print("Meow...")


# class cow(animal):
#     def sound(self):
#         print("Mooo...")


# def call(animal):
#     animal.sound()

# dog = dog()
# cat = cat()
# cow = cow()

# call(dog)
# call(cat)
# call(cow)


# class diploma:
#     def student(self):
#         pass


# class Computer(diploma):
#     def student(self):
#         super().student()
#         dict = {
#             1: "Samay",
#             2: "Vedant",
#             3: "Shivam"
#         }
#         print(dict)


# class Electrical(diploma):
#     def student(self):
#         super().student()
#         dict = {
#             1: "Shivam",
#             2: "Shirinivas",
#             3: "Kapate"
#         }
#         print(dict)


# class Civil(diploma):
#     def student(self):
#         super().student()
#         dict = {
#             1: "Powade",
#             2: "patil",
#             3: "Awale"
#         }
#         print(dict)


# obj = diploma()
# obj1 = Computer()
# obj2 = Electrical()
# obj3 = Civil()

# for x in (obj,obj1,obj2,obj3):
#     x.student()


# class sample1:

#     def info(self, name, age):
#         self.name = name
#         self.age = age


# class sample2(sample1):

#     def info(self,name,age,year):
#           super().info(name,age)
#           self.year = year
    
#     def show(self):
#          list = [self.name,self.age,self.year]
#          print(list)


# obj = sample2()
# obj.info("Samay",20,"2023")
# obj.show()
        
