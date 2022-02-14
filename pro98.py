def swapFileData():
    file1=input("input the name of the first file")
    file2=input("input the name for the second file")
    f=open(file1,"r")
    data_a=f.read()
    f2=open(file2,"r")
    data_b=f2.read()
    f=open(file1,"w")
    f.write(data_b)
    f2=open(file2,"w")
    f2.write(data_a)

swapFileData()    
    

