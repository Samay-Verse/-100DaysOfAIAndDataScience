# First Program of Function

# def My_Function():
#     print("Hello This is Python Function First Program....")
# My_Function()


# passing paremeter in Function

# def my_function(name, Sirname):
#     print("The name is: ", name, "The Sir Name is: ", Sirname)


# my_function("Samay", "Powade")


# def my_Function(*company):
#     print("The Best Company is: " + company[0])
#     print("The Best Company is: " + company[1])
#     print("The Best Company is: " + company[2])
#     print("The Best Company is: " + company[3])

# my_Function("Microsoft","Google","FaceBook","twitter")

# Keyword Argument

# def my_function(company1,company2,company3):
#     print("The Copany is: " + company1)
#     print("The Copany is: " + company2)
#     print("The Copany is: " + company3)

# my_function(company1="Microsoft",company2="Google",company3="Facebook")


# Arbitrary Keyword Arguments, **kwargs

# def my_function(**key):
#     print("His Name is>>>"+key["fname"])
#     print("His Name is>>>"+key["Lname"])

# my_function(fname = "Samay",Lname = "Powade")

'''This is a program of Default Parameter Value'''

# def my_function(country = "American"):
#     print("I am form This Country:"+country)

# my_function("indian")
# my_function("Pakistan")
# my_function()
# my_function("baglaDes")


# Passing list as a Function Argument

# def myFunction(list1):
#     for x in  list1:
#         print(x)

# list = ['Samay','Shirinivas','Vedant','Shivam']

# myFunction(list)


# Return Value

# def myFunction(x):
#     return x * 5


# print(myFunction(10))
# print(myFunction(100))

# this is a function of recursion

# def myFunction(k):
#     if k > 0:
#         result = k + myFunction(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result

# myFunction(7)

# This is a Factorial of number program

# def factorial(n):
#     if n == 0:
#         print("The End")
#     else:
#         return  n * factorial(n - 1)

# result = factorial(0)
# print(result)

# list = []

# def list_input(info):
#     for x in info:
#          pass

# list_input(list)

# def myfunction():
#     password = 2023
#     input_pass = int(input("Enter the password: "))
#     if input_pass == password:
#         print("The Password is Correct...")
#     else:
#         while input_pass != password:
#            print("Password is incorrect please try again:")
#            input_pass = int(input("Enter the password: "))


# myfunction()


# # lambda funtion
# x = lambda a: a * 10
# print(x(10))


# passing two parameter

# x = lambda a,b:  a * b
# print(x(5,6))

# multiple prameter in lambda function

# x = lambda a,b,c:a + b + c

# print(x(5,5,5))

# Use the lambda Function in function

# def function(n):
#     return lambda a: a * n

# myLambda = function(20)
# myLambda2 = function(30)

# print(myLambda(10))
# print(myLambda2(10))