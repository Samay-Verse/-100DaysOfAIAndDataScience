
# itrators

# def gen(n):
#     for x in range(n):
#         yield x

# obj = gen(10000)

# for x in range(100):
#     print(next(obj))


# def gen(n):
#     for x in range(n):
#         yield x


# num = "Samay"

# itretor = iter(num)
# print(len(itretor))
# print(next(itretor))
# print(next(itretor))
# print(next(itretor))
# print(next(itretor))
# print(next(itretor))

# import sys
# x = 0
# for x in range(1000):
#     print(x)

# print(sys.getsizeof(x))

# def gen(n):
#     for x in range(n):
#         yield x

# obj = gen(10000)

# for x in range(10):
#     print(next(obj))

# print(sys.getsizeof(gen(10000)))
# print(type(obj))

# list = ["Samay",'vedant','Shivam','Kirishna','Shirinivas']

# # print(next(list))

# myiter = iter(list)
# print(type(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# print(sys.getsizeof(myiter))


# Create a iterator using __iter__ method and __next__ method

# class myNumber:

#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         y = self.a
#         self.a += 1
#         return y


# obj = myNumber()

# myiter = iter(obj)

# for i in range(10):
#     print(next(myiter))


# x = 1

# while x <= 10:
#     print(x)
#     x = x + 1
# import sys

# print(sys.getsizeof(x))
# print(sys.getsizeof(myiter))


# class sample:

#     def __iter__(self, name, age):
#         self.name = name
#         self.age = age
#         return self

#     def __next__(self, name, age):
#         self.y = name
#         self.z = age
#         return self.y
#         return self.x

# list1 = ["Samay","Siddhant","Yash","Prtik"]
# list2 = [12,34,23,45]


# obj = sample()
# obj.__iter__(list1,list2)
# myiter  = iter(obj)
# print(next(myiter))


# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#   print(x)

# list = {1,2,3,4,5,6,7,9,10}

# print(len(list))



