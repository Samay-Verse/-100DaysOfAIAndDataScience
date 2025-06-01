# # # # # list = ['banana','apple','mango','DryFoods']

# # # # # print(list)
# # # # # print(len(list))

# # # # # list = ['THAR',"TOYOTA",'BMW','TATA','Farari']
# # # # # list2 =[1,2,3,4,5,6,7,8,9,10]
# # # # # list3 = [False,True,False]

# # # # # print(type(list))

# # # # # print(type(list2))

# # # # # print(type(list3))

# # # # # list = ['Samay',12,True]
# # # # # print(list)

# # # # # ThisList = list(('Samay',12,True,'Samay',12))

# # # # # print(type(ThisList))


# # # # list =['samay','powade','mango','banana','orange','watermelon','Cake','cat']

# # # # if 'Cake' in list:
# # # #     print('This is present in list')
# # # # else:
# # # #     print("This  is Not present in list")

# # # list = [1,3,4,5,6,7,8,10]
# # # list.insert(7, 'Samay')
# # # print(list)

# # list = ['mango','Banana','orange']
# # list2 = ['Papaya','Lime']
# # list.extend(list2)
# # list.insert(0,'Pineapple')
# # print(list)

# list = ['Samay','Vedant','Shivam']
# list.clear()
# list.append()
# print(list)

# list = ['Samay','Vedant','Shivam']
# [print(x) for x in list]


# list = ['Samay','Vedant','Sandeep','Shivam','Rohit']
# newList = [x for x in list if "a" in x]
# print(newList)
# # for x in list :
# #     if 'a' in x:
# #         newList.append(x)
# # print(newList)


# list = ['Samay','Vedant','Sandeep','Shivam','Rohit']

# newList = [x for x in list if x != 'Sandeep']

# list2 = [x for x in range(10) if x % 2 != 0]

# list3 = [x for x in list]

# list4 = ['Hello' for x in list if x != 'Hello']

# list5 = [x if x != 'Samay' else  'Sachin' for x in list]

# print(list5)

# print(newList)


# list1 = [90,9,8,736,87,83,920,288,22829,98387]
# # list1.sort( reverse = True)
# list1.reverse()

# print(list1)


# list1 = ['Samay', 'Vedant', 'Sandeep', 'Shivam', 'Rohit']

# # list2 = list.copy()
# list2 = list(list1)

# print(list2)

# list1 = ['Samay', 'Vedant', 'Sandeep', 'Shivam', 'Rohit']
# list2 = [1,2,3,4,5]

# for x in list2:
#     list1.append(x)

# print(list1)


# list1 = [2,4,2,77,88,5,66,77,99,90]
# list2 = [34,34,55,556,77,888,87,90]

# list1.extend(list2)
# # list1.sort(reverse=True)
# # print(list1)
# list1.reverse()
# print(list1)

# list1 = ['Samay', 'Vedant', 'Sandeep', 'Shivam', 'Rohit']

# list1.__format__
# print(list1)


# def show(list1):

#     sample = set(list1)
#     result = list(sample)

#     return result


# list = [1,2,3,4,5,6,7,8,9,3,2,1,2,3,4,55,6,3,4,6,78,55,5,5,7,7,7,7]

# obj = show(list)

# print(obj)


def remove_duplicates(input_list):
    # Convert the list to a set to remove duplicates
    unique_elements = set(input_list)
    
    # Convert the set back to a list
    result_list = list(unique_elements)
    
    return result_list

sample_list = [1, 2, 2, 3, 4, 4, 5]
print("Original List:", sample_list)

unique_list = remove_duplicates(sample_list)
print("List with Duplicates Removed:", unique_list)


