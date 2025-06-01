
# # info = {
# #     "Name":'Samay',
# #     "Age":18,
# #     "Class":"CO4I",
# #     "Name":'Samay Powade',
# #     'Adult':False

# # }

# # print(type(info))
# # print(info["Name"])
# # print(len(info))
# # print(info)


# # thisDict = dict(name = "Samay",age = 18,Std = 'CO4I')
# # print(thisDict)

# # CompanyDict = {

# #     "CompanyName":"Microsoft",
# #     "AverageSalary":100000,
# #     "Location":"Pune",
# #     "WorkTime":"Per day 5 to 6 hour",
# #     "Work":"DataScience",
# #     "Position":"Bigneer"
# # }

# # x = CompanyDict["Location"]
# # y = CompanyDict.get("WorkTime")
# # z = CompanyDict.keys()
# # a = CompanyDict.values()
# # print(CompanyDict)
# # print(x)
# # print(y)
# # print(z)
# # print(a)

# # CompanyDict["CompanyName"] = "Facebook"
# # CompanyDict["Location"] = "Nanded"
# # print(CompanyDict)

# # CompanyDict["StartingDate"] = "11/11/2005"

# # print(CompanyDict)

# # print(CompanyDict.keys())

# # print(CompanyDict.items())

# # CompanyDict["Work"] = "Developer"

# # print(CompanyDict)


# # CompanyDict = {

# #     "CompanyName":"Microsoft",
# #     "AverageSalary":100000,
# #     "Location":"Pune",
# #     "WorkTime":"Per day 5 to 6 hour",
# #     "Work":"DataScience",
# #     "Position":"Bigneer"
# # }

# # if "Locatio" in CompanyDict:
# #     print("This Key Are Present in the Companny Dictionary.")
# # else:
# #     print("Thiskey are not present in the list.")


# # thisDict = {
# #     "Name":"Samay",
# #     "Age":18,
# #     "Place":"Nanded",
# #     "Collage":"GT & MC"
# # }

# # thisDict.update({"Age":20})

# # print(thisDict)

# # thisDict.update({"FatherName":"Santosh"})
# # print(thisDict)
# # print(thisDict)
# # thisDict.pop("Collage")
# # thisDict.popitem()
# # thisDict.popitem()
# # thisDict.popitem()
# # thisDict.popitem()
# # del thisDict["Place"]
# # del thisDict
# # thisDict.clear()
# # print(thisDict)


# # info = {
# #     "Name":"Samay",
# #     "Std":"CO4I",
# #     "FatherName":"Santosh",
# #     "MotherName":"Vandena"
# # }

# # # info2 = info.copy()
# # # print(info2)
# # # [print(x) for x in info2]
# # myDictionary = dict(info)
# # print(myDictionary)
# # # for x , y in info.items():
# # #     print(x,y)

# TheGroupOfSamTecIndurstry = {

#     "DataScience": {
#         "hostName": "Samay Powade",
#         "CompanyStartingDate": "11/11/2005",
#         "NetWorking": "2000000 Month"
#     },

#     "DevelopMentSofter": {
#         "hostName": "Samay Powade",
#         "CompanyStartingDate": "11/12/2005",
#         "NetWorking": "3000000 Month"
#     },
#     "FullStackDeveloper": {
#         "hostName": "Samay Powade",
#         "CompanyStartingDate": "11/01/2005",
#         "NetWorking": "4000000 Month"
#     },
#     "The Metal": {
#         "hostName": "Samay Powade",
#         "CompanyStartingDate": "11/02/2005",
#         "NetWorking": "5000000 Month"
#     }
# }

# x = TheGroupOfSamTecIndurstry["DataScience"]["hostName"]
# print(x)

# # print(TheGroupOfSamTecIndurstry)
# # print("\n")
# # print(TheGroupOfSamTecIndurstry["DevelopMentSofter"])
# # print("\n")
# # print(TheGroupOfSamTecIndurstry.get("The Metal"))
# # print("\n")
# # print(TheGroupOfSamTecIndurstry.items())

# # for x in TheGroupOfSamTecIndurstry.values():
# #     print(x)


# mobileDict = {
#     "Product": "Mobile",
#     "ProductItems": 200,
#     "Mobile Company": "ONE Pluse/1+"
# }
# laptopDict = {
#     "Product": "Laptop",
#     "ProductItems": 300,
#     "Laptop Company": "Lenovo"
# }
# TVDict = {
#     "Product": "TV",
#     "ProductItems": 400,
#     "TV Company": "Sony"
# }
# AcDict = {
#     "Product": "AC",
#     "ProductItems": 500,
#     "AC Company": "SONY"
# }
# Headphone = {
#     "Product": "HeadPhone",
#     "ProductItems": 600,
#     "Headphone Company": "Boat"
# }

# ChetanaServices = {
#     "mobileDict" :mobileDict,
#     "laptopDict" :laptopDict,
#     "TVDict":TVDict,
#     "AcDict":AcDict,
#     "Headphone":Headphone
# }

# # print(ChetanaServices.pop("mobileDict"))
# # del ChetanaServices["AcDict"]
# # print(ChetanaServices)

# # for x in  ChetanaServices.items():
# #     print(ChetanaServices)

# person = {
#     "Name":"Samay",
#     "Age":18,
#     "City":"Nanded"
# }

# print(person)


# School = {
#      1:"Samay",
#      2:"Vedant",
#      3:"Sandeep",
#      4:"Rohit"
# }

# print(School)

# Predefined dictionary of student names
# student_dict = {
#     1: "Alice",
#     2: "Bob",
#     3: "Charlie",
#     4: "David",
#     5: "Eve"
# }

# # Printing the dictionary of student names
# for keys, value in student_dict.items():
#     print(f"Student ID: {keys}, Name: {value}")

# student = {
#     "Samay":90,
#     "Rohit":78,
#     "Vedant":88,
#     "Shivam":60,
#     "Shirinivas":70,
# }

# for key,values in student.items():
#     print(f"The Student name :{key}, Marks:{values}")
# total_Marks = sum(student.values())
# Average = total_Marks/5
# print(Average)

# student = {
#      "Siddhant":89,
#      "Sntosh":77,
#      "Sandeep":67,
#      "Vedant":78
# }

# for key,value in student.items():
#     print(f"The Name Of Student:{key},The Marks:{value}")
# totalSum = sum(student.values())
# print(totalSum)

# StudentDict = {}
# Student_number = int(input("Enter the Number of student: "))

# for x in range(Student_number):
#     name = input("Enter the Student Name:")
#     marks = int(input("Enter the Marks"))
#     StudentDict[name] = marks

# print("The Student Record is: ")

# for name,marks in StudentDict.items():
#     print("Name",name)
#     print("Marks:",marks)
# total_sum = sum(StudentDict.values())
# total_average = total_sum/Student_number
# print(total_average)


"Sample Nested Dictionary"
# student = {
#     "Samay": {
#         "Java Programming": 61,
#         "Software Engineering": 45,
#         "Microprocessor": 35,
#         "Data Communication": 48
#     },
#     "Vedant": {
#         "Java Programming": 56,
#         "Software Engineering": 47,
#         "Microprocessor": 55,
#         "Data Communication": 65
#     },
#     "Shivam": {
#         "Java Programming": 67,
#         "Software Engineering": 55,
#         "Microprocessor": 75,
#         "Data Communication": 68
#     }

# }

# total_sum1 = sum(student["Samay"].values())
# length = len(student["Samay"])
# total_avg = total_sum1 / length
# print(total_avg)


# totalsum1 = sum(student["Samay"].values())
# totalsum2 = sum(student["Shivam"].values())
# totalsum3 = sum(student["Vedant"].values())
# print(totalsum1)
# print(totalsum2)
# print(totalsum3)

# for key,value in student["Samay"].items():
#     print(f"{key},{value}")

# info = student["Samay"]
# print(info)

"Program to Input number in Directory"

# myList = ["Samay",'Shivam',"Vedant"]
# myDict = {}

# for temp in myList:
#     marks = float(input("Enter the Marks of {}:".format(temp)))
#     myDict[temp] = marks
#     print(temp)

# print("The Student Reors is: ")
# for name,marks in myDict.items():
#     print("Name: ",name)
#     print("marks: ",marks)
#     print("-"*10)

samay = 'samay'
myDict = {
    samay:['Samay','Powade','Santosh'],
    "Shivam":(1,2,3,4,5,6,7,8,9,10),
    "Vedant":{'Patil','CO5I','Nanded'}
}
print(myDict["Vedant"])


# COStaf = ['Samay', 'Vedant', 'Shivam', 'Shardha']
# EEStaf = ['Piyush', 'Rohit', 'Siddhant', 'Maya']

# MyDict = {
#     'CO':
#     {

#     },
#     'EE':
#     {

#     }
# }
# # For input Staf  present in Dictionary
# for x in range(1):
#     presentStafCO = int(input("Enter the Present Staf of CO in Collage: "))
#     MyDict['CO']["StafCO"] = presentStafCO

# for y in range(1):
#     presentStafEE = int(input("Enter the Present Staf of EE in Collage: "))
#     MyDict['EE']["StafEE"] = presentStafEE

# for temp1 in COStaf:
#     Salary = input("Enter the Average Salary of Staf {}".format(temp1))
#     MyDict['CO'][temp1] = Salary

# for temp2 in EEStaf:
#     Salary2 = input("Enter the Average Salary of Staf {}".format(temp2))
#     MyDict['EE'][temp2] = Salary2

# print(MyDict['CO'])
# print(MyDict['EE'])

# mylist = [
#     {"Samay": 61, "age": 18, "Class": "CO4I"},
#     {"Shivam": 61, "age": 20, "Class": "CO4I"},
#     {"Vedant": 61, "age": 17, "Class": "CO4I"}
# ]

# # print(mylist)
# # print(type(mylist))
# # print(type(mylist[0]))
# mylist[0]["Class"] = "CO5I"
# mylist[1]["Class"] = "CO5I"
# mylist[2]["Class"] = "CO5I"
# print(mylist[0].values())
# print(mylist[1].values())
# print(mylist[2].values())

# mylist = [
#     {}
# ]
# Limit = int(input("Enter the Limit of Student: "))

# for x in range(Limit):
#     name = input("Enter the Name of student: ")
#     marks = int(input("Enter the Marks out of 100: "))
#     mylist[0][name] = marks


# print("The Record is: ")

# for name,value in mylist[0].items():
#     print("Name",name)
#     print("value",value)
#     print("-"*10)


library = [
    {"Title":"The Gold","Author":"The Sancons.."},
    {"Title":"The Man in Forest","Author":"The Samay.."},
    {"Title":"The Golden City","Author":"The Vedant.."}
]

print(library[0].get("Title"))
print(library[1].get("Title"))
print(library[2].get("Title"))


# customreInfo = {
#     "Samay": 1234,
#     "Siddhant": 2345,
#     "Vedant": 3333,
#     "Shivam": 4545
# }


# print(len(customreInfo))
# name = input("Enter the Name:")
# pass1 = int(input("Enter the Password:"))

# customreInfo[name] = pass1
# print(customreInfo)


# dishList = {
#     "Papdi Chaat": 50,
#     "Samosa": 20,
#     "Naan": 120,
#     "Paratha": 50,
#     "Masala Dosa": 100,
#     "Masala Chai": 50,
#     "Butter Chicken": 130,
#     "Chicken Tikka": 160,
#     "Gajar Ka Halwa": 200,
#     "MEALS": 200,
#     "Chana masala": 300,
#     "Crisp papadum": 40,
#     "Lamb vindaloo": 400,
#     "Kofta": 150,
#     "Korma": 190,
#     "Biryani": 90,
#     "Kebab": 180
# }


# user_input = input("Enter the name:") 

# if user_input == dishList:
#     print(user_input)
# else:
#     print("This is not valid.")




def check_name_in_dictionary():
    # Declare a dictionary
    my_dictionary = {
        "Alice": 25,
        "Bob": 30,
        "Charlie": 22,
        "David": 28,
        "Eva": 20
    }

    # Take user input for the name
    user_input = input("Enter a name: ")

    # Check if the user input name is present in the dictionary
    if user_input in my_dictionary:
        print(f"{user_input} is present in the dictionary. Age: {my_dictionary[user_input]}")
    else:
        print(f"{user_input} is not present in the dictionary.")

# Call the function to check the user input name
check_name_in_dictionary()
