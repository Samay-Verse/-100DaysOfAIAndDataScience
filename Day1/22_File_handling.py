
# try:
#     f = open("C:\\Users\\Samay\\Desktop\\File\B.txt", "r")
#     f.write("The Microsoft company is the best company..")
#     for x in range(2):
#           print(f.read())

# except Exception as ex:
#     print("Please Create the file ")

# else:
#      f.close()
#      print("File Are Close ")


# # # print("File Is Created Sucessfully")


# # File Creating

# # f = open("C:\\Users\\Samay\\Desktop\\File\A.txt", "w")
# # Str = "My Name is samay Santosh powade..."
# # f.write(Str)
# # f0 = open("C:\\Users\\Samay\\Desktop\\File\B.txt","w")
# # f0.write(Str)


# # try:
# #     with open("C:\\Users\\Samay\\Desktop\\File\A.txt") as f1:
# #         with open("C:\\Users\\Samay\\Desktop\\File\B.txt", "w") as f2:
# #             for i in f1:
# #                 f2.write(i)

# # except:
# #     print("File Are Not Found..")

# # else:
# #     f1.close()
# #     f2.close()
# #     print("File Are Close..")


# # try:
# #     with open("C:\\Users\\Samay\\Desktop\\File\A.txt") as f1:
# #         with open("C:\\Users\\Samay\\Desktop\\File\B.txt", "w") as f3:

# #             for i in f1:
# #                 f3.write(i)


# # except:
# #     print("File Are Not Created...!")

# # else:
# #     f1.close()
# #     f3.close()
# #     print("Data Copy..!")


# # import os

# # if os.path.exists("C:\\Users\\Samay\\Desktop\\File\B.txt"):
# #     os.remove("C:\\Users\\Samay\\Desktop\\File\B.txt")
# #     print("File Are Remove..!")
# # else:
# #     print("File Are Not Deleted..!")

# # if os.path.exists("C:\\Users\\Samay\\Desktop\\File\A.txt"):
# #     os.remove("C:\\Users\\Samay\\Desktop\\File\A.txt")
# #     print("File Are Remove..!")
# # else:
# #     print("File Are Not Deleted..!")

# # with open("C:\\Users\\Samay\\Desktop\\File\A.txt","x") as f1:
# #     with open("C:\\Users\\Samay\\Desktop\\File\B.txt","w"):
# #         print("File Are Created...!")
# # try:
# #     with open("c:\\Users\\Samay\\Desktop\\File\D.txt", "x") as f1:
# #         print("File Are Created..!")

# # except Exception as e:
# #     print("Your Created file Are all ready Creared..")
# # else:
# #     print("The Program are sucessfull Run..!")


# # import openpyxl

# # def write_data_to_excel_xlsx(filename, data):
# #     workbook = openpyxl.Workbook()
# #     sheet = workbook.active

# #     for row_idx, row_data in enumerate(data, start=1):
# #         for col_idx, cell_value in enumerate(row_data, start=1):
# #             sheet.cell(row=row_idx, column=col_idx, value=cell_value)

# #     workbook.save(filename)
# #     print(f"Data saved to {filename} successfully.")

# # # Example data
# # input_data = [
# #     ["Name", "Age", "City"],
# #     ["John", 30, "New York"],
# #     ["Alice", 25, "Los Angeles"],
# #     ["Bob", 35, "Chicago"]
# # ]

# # # Call the function with your desired filename
# # write_data_to_excel_xlsx("output_data.xlsx", input_data)
# # print("output_data.xlsx",input_data)


# import pandas as pd
# file_path = "C:\\Users\\Samay\\Desktop\Book1.xlsx"
# data = {
# "Name":"Samay"
# }

# # # df = pd.DataFrame(data)

# # # # file_path = "data.xlsx"
# # # df.to_excel(file_path, index=False)


# # f = open("C:\\Users\\Samay\\Desktop\\File\Sample.txt", "w")
# # f.write(data)


# # f = open("C:\\Users\\Samay\\Desktop\\File\Sample.txt", "r")

# # for x in f:
# #     print(f.read())


# # f = open("C:\\Users\\Samay\\Desktop\\File\Sample.txt","r")

# # print(f.read())


# # with open("C:\\Users\\Samay\\Desktop\\File\Sample.txt") as f1:
# #     with open("C:\\Users\\Samay\\Desktop\\File\Python.txt","w") as f2:

# #          for x in f1:
# #               f2.write(x)

# # print("File Are Copy")


# # if os.path.exists("C:\\Users\\Samay\\Desktop\\File\Sample.txt"):
# #     os.remove("C:\\Users\\Samay\\Desktop\\File\Sa.txt")
# #     print("File are Deleted...")
# # else:
# #     print("The File Are Not created..")
# # os.remove("C:\\Users\\Samay\\Desktop\\File\Py.txt")


# # f = open("C:\\Users\\Samay\\Desktop\\File\Sample.txt","a")
# # f.write("This is samay santosh powade...")
# # f.close()

# # # Open The File

# # f1 = open("C:\\Users\\Samay\\Desktop\\File\Sample.txt","r")
# # print(f1.read())
# # import os
# # os.rmdir("C:\\Users\\Samay\\Desktop\\New folder")

# # print("The Folder Are Deleted")


# f = open("C:\\Users\\Samay\\Desktop\\File\MyFile1.xlsx", "x")
# f.close()
# f1 = open("C:\\Users\\Samay\\Desktop\\File\MyFile2.xlsx", "x")
# f1.close()


# print("The File Are Creatd ")


# with open("C:\\Users\\Samay\\Desktop\\File\A.txt","w") as f1:
#           f1.write("This is samay santosh powade")


