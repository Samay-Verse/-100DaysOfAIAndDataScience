
# f1.close()


# print("The File Are Creatd ")


try:
    with open("C:\\Users\\Samay\\Desktop\\File\Sampele1.txt") as f1:
        with open("C:\\Users\\Samay\\Desktop\\File\Sampele2.txt","w") as f2:
            
            for x in f1:
                f2.write(x)
        


except:
    print("File Are Not found...")
