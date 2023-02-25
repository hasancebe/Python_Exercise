file=open("newfile.txt","w",encoding="utf-8")
print(file)
file.write("hasan cebe ")
file1=open("newfile.txt","a",encoding="utf-8")
file1.write("tuğba cebe")
#file3=open("newfile1","x")
file4=open("newfile.txt","r")
print(file4)
"""
file5=open("newfile1","r",encoding="utf-8")
for i in file5:
    print(i,end="")
"""
# veya read metodu ile yazdırabiliriz
file5=open("newfile1","r",encoding="utf-8")
#content=file5.read()
#content=file5.read(2)
#print(content)
#content=file5.read(12)
#content=file5.readline()
#print(content)
liste=file5.readlines()#dosyadaki veriyi liste elemanı olarak alırız
print(liste)

file.close()

file1.close()

file4.close()
file5.close()

#file1=open("C:/Users/hasan/OneDrive/Desktop/newfile.txt","w")
