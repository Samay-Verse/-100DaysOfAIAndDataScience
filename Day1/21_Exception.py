
# try:
#      print(x)
# except:
#      print("The X is not Defined..")
# # print(x)

# list = [1,2,3,4,5,6,7,8,9,10]

# print(list)


# a = 10
# b = 0

# try:
#     c = a / b
# except NameError:
#     print("the Number are not divided into zero.")
# except:
#     print("Some Thing is else..")

# print("this is the exception code..")


# n1 = int(input("Enter the  number 1:"))
# n2 = int(input("Enter the  number 2:"))

# try:
#     n3 = n1/n2
# except Exception as e:
#     print(e)

# print("hello World")

# try:
#     print(x)
# except Exception as E:
#     print(E)

# print("This is A Exception File..")


# n1 = int(input("Enter the  number 1:"))
# n2 = int(input("Enter the  number 2:"))

# try:
#     n3 = n1/n2
#     print(n3)
# except Exception as E:
#     print(E)
# else:
#     print("Program is Exsucuted")

# try:
#     n3 = n1/n2
#     print(n3)
# except Exception as E:
#     print(E)
# finally:
#     print("This is Samay Santosh powade..")


# list = [1,2,3,4,5,6,8]
# print(list)


# Raise Exception

# x = -1

# if x < 0:
#     raise Exception("Sorry,The Number not below Zero...")

# print("This is microsoft company..")


# str = "hello"

# if not type(str) is int:
#     raise StopIteration("Only Integer are allows..")


# User Define Exception


# class myException(Exception):
#     def __init__(self,message):
#         self.message = message

#     def __str__(self) -> str:
#           return f"MyException: {self.message}"

# def ShowException(num):
#      if num < 0:
#           raise myException("The Number is must be in integer not negative..")

# try:
#      user_input = int(input("Enter the number:"))
#      ShowException(user_input)
#      print("All Right...")
# except myException as my:
#      print(my)
# except ValueError:
#      print("Please enter the proper value..")


# class myException(Exception):
#     def __init__(self, message) -> None:
#         self.message = message

#     def __str__(self) -> str:
#         return f"ValueError: {self.message}"


# def showException(num):
#     if type(num) == int:
#         print("Hello...")
#     else:
#         raise myException("This is Not valid..")


# try:
#     user_input = int(input("Enter the Number:"))
#     showException(user_input)
#     print("All Right..")

# except myException as my:
#     print(my)


# class myException(Exception):
#     def __init__(self, message):
#         self.msg = message

#     def __str__(self):
#         return f"Divided by zero: {self.msg}"


# def showException(num1, num2):

#     if num1 > 0 and num2 == 0:
#         raise myException("The Divided by Zero Error")
#     else:
#         print(num1, " ", num2)


# try:
#     n1 = int(input("Enter the number 1:"))
#     n2 = int(input("Enter the number 2:"))
#     showException(n1,n2)

# except myException as show:
#     print(show)
# except Exception as a:
#     print(a)


# dict = {
#     "name": "Samay",
#     "Age": " ",
#     "Password": "Samay@2005"
# }


# def show(num):

#     if num["Age"] == None:
#         del num["Age"]
#     else:
#         print("Welcome")

# obj = dict["Age"] = None
# print(dict["name"])
# print(type(obj))
# show(dict)

# print(dict)


# User Define Exception


# class myException(Exception):
#     def __init__(self, *args: object, message) -> None:
#         super().__init__(*args)
#         self.msg = message

#     def __str__(self) -> str:
#         return f"The Fill Error: {self.msg}"


# # def showException(dictionary):
# #     if dict.items == None:
# #         print(dict)


# try:
#     dict = {
#         1: None,
#         2: "Samay",
#         3: "Santosh",
#         4: " ",
#         5: " ",
#         6: None,
#         7: True,
#         8: "Sandeep",
#         9: "Shivam",
#         10: None,
#         11: None,
#         12: "Samay",
#         13: "Santosh",
#         14: " ",
#         15: None,
#         16: None,
#         17: True,
#         18: "Sandeep",
#         19: "Shivam",
#         20: None
#     }
#     # showException(dict)

# except:
# #     pass


def Delete_None_values_from_Dict(input_dict):
    listDelete = []

    for key, value in input_dict.items():

        if key == 1:
            listDelete.append(value)
        if value == " ":
            listDelete.append(key)

    print(listDelete)


dict = {
    1: None,
    2: "Samay",
    3: "Santosh",
    4: " ",
    5: " ",
    6: None,
    7: None,
    8: "Sandeep",
    9: "Shivam",
    10: None

}

Delete_None_values_from_Dict(dict)