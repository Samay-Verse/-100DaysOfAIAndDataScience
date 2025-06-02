
# # tuple1 = (12,13,14,15,16)

# # list1 = list(tuple1)

# # list1.insert(1,1000)
# # tuple1 = tuple(list1)

# # print(tuple1)

# # set = {12,23,34,54,67,0}

# # set.add(19)

# # print(set)

# # dist = {
    
# #     'Name':['Samay','Aastha','Kiwi'],
# #     'Class':(1,2,3,4,4,5,6,7,8,9)
# # }

# # for x,y in dist.items():
# #     print(x,y)
# # # print(dist)

# # n = 7

# # factorial  = 1

# # for x in range(1, n + 1):
# #     factorial *= x

# # print(factorial)


# # def facto(n):
# #     if n == 1:
# #         return 1
# #     else:
        
# #         return n * facto(n - 1 )

# # obj = facto(7)

# # if obj == 1:
# #     print(obj)
# # else:
#     # print(obj)
    
    
# num = int(input('Enter the number:'))

# # if num % 2 == 0:
# #     print('Even')
# # else:
# #     print('odd')

# def isprime(n):
#     if n < 2:
#         return False
#     for x in range(2,int(n ** 0.5)+1):
#         if n % x == 0:
#             return False
#     return True

# obj = isprime(num)

# if obj == False:
#     print('Given number is not prime ')
# else:
#     print('Given number is prime')


# class sample:
#     def __init__(self, a,b):
#       self.a = a
#       self.b = b
    
#     def __str__(self):
#        return f'{self.a}, {self.b}'
   


# obj = sample(10,20)

# print(obj)




# inheritance 

# class sample1:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
        
#     def __str__(self):
#         return f"{self.a}, {self.b},{self.c}"
    
#     def func(self):
#         n = 1
#         while(n<= 10):
#             print(n)
#             n = n + 1
            
    

# class sample2(sample1):
#     def __init__(self, a, b,c):
#         super().__init__(a, b)
#         self.c = c
        
#     def __str__(self):
#         return super().__str__()


# # obj = sample1(10,20)

# obj2 = sample2(10,20,30)

# print(obj2)

# obj2.func()



# file Handling

# f = open('C:\\Data Science\\sample.txt','r+')
# # f.write('Welcome to india my name is samay santosh powade')
# print(f.readline())

import os

os.remove('C:\\Data Science\\sample.txt')
