
# name = ('Samay','Vedant','Shivam','Rohit','Shiriniva','Samay')

# print(len(name))

# tuple = ('Samay',("Samay"))

# print(type(tuple))
# print(tuple)


# tuple = ("Samay",12,True,23.89)
# list = ["Samay",12,True,23.89]
# print(type(list))

# print(type(tuple))

'''Tuple as Constructor '''

# thisTuple = tuple(("Samay", "Vedant", "Sahivam", 'Rohit')
#                   )  # This is Constructor as tuplle

# print(thisTuple)

# Range of Tuples

# thisTuple = tuple(("Samay", "Vedant", "Sahivam", 'Rohit','Kirishna','Shubham','Rohan'))

# # print(thisTuple[1])

# for x in thisTuple:
#     if x == 'Vedant':
#         print(x)

# list1 = ["Samay", "Vedant", "Sahivam", 'Rohit','Kirishna','Shubham','Rohan']

# list1[3] = 'Sachin'
# print(list1)

# thisTuple = ("Samay", "Vedant", "Sahivam", 'Rohit','Kirishna','Shubham','Rohan')

# x = list(thisTuple)

# x[1] = "Powade"

# thisTuple = tuple(x)

# print(x)

'''The Change the tuple Items'''

# tuple1 = ('Samay','Santosh','Shivam','Shirinivas','Vedant')

# tempVar = list(tuple1)

# tempVar[2] = "Samay Santosh powade from Nanded"

# tuple1 = tuple(tempVar)

# print(tempVar)


# "The add Element in the Tuple using conver ting of string "

# thistuple = ('Samay','Santosh','Shivam','Shirinivas','Vedant')

# temp = list(thistuple)
# temp.append('Rohit')

# thistuple = tuple(temp)

# print(temp)

# print(thistuple)


# Add Tuple To tuple

# thistuple = ('Samay','Santosh','Shivam','Shirinivas','Vedant')

# temp = ('Orange','Samay','Santosh','Shivam','Shirinivas')

# thistuple = thistuple +  temp
# print(thistuple)

# remove the item form the tuple

# thistuple = ('Samay','Santosh','Shivam','Shirinivas','Vedant')
# temp = list(thistuple)
# # temp.clear()
# thistuple = tuple(temp)
# del thistuple
# print(thistuple)


# unpacking in tuple

# thistuple = ('Samay','Santosh','Shivam','Shirinivas','Vedant')
# (sirName,*std,color) = thistuple
# print(sirName)
# print(std)
# print(color)


# Tuple as a loop in python

# thistuple = ('Samay','Santosh','Shivam','Shirinivas','Vedant')

# # for x in thistuple:
# #     print(x)
# for x in  range(len(thistuple)):
#      print(thistuple[x])

# # using while loop
# i = 0
# while i < len(thistuple):
#     print(thistuple[i])
#     i = i + 1

# thistuple = ()

# temp = list(thistuple)

# for x in range(5):
#     input_ = int(input("Enter the numebr :"))
#     temp.append(input_)

# thistuple = tuple(temp)

# print(thistuple)


# thistuple = ('Samay','Santosh','Shivam','Shirinivas','Vedant')
# tuple = (1,2,3,4,5,6,7,8,9,10)
# print(thistuple.index('Santosh'))


# print(tuple * 2)


# thistuple = ('Samay','Santosh','Shivam','Shirinivas','Vedant')
# x = list(thistuple)
# x.append("Kirishna")
# thistuple = tuple(x)

# print(thistuple)



tuple1 = (2,33,44,55,33,455,22,55,333,888,333,999)

list1 = list(tuple1)
list1.sort()
tuple1 = tuple(list1)

print(tuple1)


maximum = max(tuple1)
minimum = min(tuple1)

print(maximum)
print(minimum)

print(tuple1[0])
print(tuple1[-1])