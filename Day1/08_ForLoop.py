''' This is a  First For Loop Program'''

# list = ["Samay","Vedant","Shivam","Kirishna","Rohit"]
# list2 = [1,2,3,4,5,6,7,8,9,10]
# list3 = [True,False,True]

# for x in list:
#     print(x)
# print("\t")
# for x in list2:
#     print(x)
# for x in list3:
#     print(x)
'''Simple For loop program'''
# for x in 'banana':
#     print(x)

"This is Sample Break Program"

# list = ["Samay","Vedant","Sandeep","Rohit","Shivam"]

# for x in list:
#     if x == "Sandeep":
#         break
#     print(x)

'''This is continue Statement program'''

# list = ['Samay','Vedant','Sandeep','Rohit']

# for x in list:
#     if x == 'Sandeep':
#         continue
#     print(x)


# for x in range(3,30,3):
#     print(x)


# for x in range(6):
#     if x == 3:
#         break
#     print(x)

# else:
#     print("Finaly Finished..")

# Nested Loop

# list1 = []
# list2 = []

# for x in list1:
#     for y in list2:
#         print(x,y)

# This is Program of Input String
# list = []

# for  x in  range(5):

#     number = int(input("Enter the number :"))
#     list.append(number)

# # total_sum = sum(list)
# # print(total_sum)
# sum = 0
# for num in list:
#     sum = sum + num
# print(sum)
# print(list)
'''This is the program of input string and print the length of string '''

'''
list = []
list2 = []
for x in range(4):
    str = input("Enter the any string :")
    list.append(str)
    length = len(str)
    list2.append(length)
print(list)
print(list2)
'''

'This is a even and odd number program'

# list = [1,2,3,4,5,6,7]

 # for x in list:
 #     if  x % 2 != 0:
 #         print(x)

'''This is a Odd Even Number program to using user input and add input element in list and remove the even number from list '''

# list1 = []

# for x in range(10):
#     number = int(input("Enter the Number :"))
#     list1.append(number)
# print("List Before Remove Even number:",list1)
# for x in list1:
#     if x % 2 == 0:
#        number = x
#        list1.remove(number)
          
# print("List After Remove Even number :",list1)

# list1 = []
# list2 = []
# list3 = []
# print("The List 1:")
# for x in range(5):
#     number = int(input("Enter the First list Number :"))
#     list1.append(number)
# print("The List 2")
# for x in range(5):
#     number = int(input("Enter the second list Number :"))
#     list2.append(number)

# # list3 = list1.extend(list2)
# list3 = list1 + list2 

# list3.sort()

# print(list3)
# print(list1)

# list = ['Samay','Vedant','Shivam']

# for i in range(len(list)):
#     print(list[i])


# list = ['Samay','Vedant','Shivam']
# [print(x) for x in list]


# list = ['Samay','Vedant','Sandeep','Shivam','Rohit']
# newList = [x for x in list if "a" in x]
# print(newList)
# # for x in list :
# #     if 'a' in x:
# #         newList.append(x)
# # print(newList)


list = ['Samay','Vedant','Sandeep','Shivam','Rohit']

newList = [x for x in list if x != 'Sandeep']

list2 = [x for x in range(10) if x % 2 != 0]

list3 = [x for x in list]

list4 = ['Hello' for x in list if x != 'Hello']

list5 = [x if x != 'Samay' else  'Sachin' for x in list]

print(list5)

print(newList)


