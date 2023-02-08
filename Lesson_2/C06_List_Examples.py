numbers=[1,3,5,7,15]
names=["hasan","ali","ahmet","can","selim"]
names.append("Cenk")#liste sonuna cenk eklemek
print(names)
names.insert(0,"sena")# en başa sema eklemek
print(names)
names.remove("ali")#ali elemanını silmek
#names.pop(1) aynı işlevi görür
print(names)
names.pop()#listenin son elemanını silmek
print(names)
print(names[::-1])#ters çevirme
names[::-1]
print(names)
print(names.index("can"))#index değerini bulma
result="hasan" in names# hasan listenin elemnı mıdır
print(result)
names.sort()#liste elemanlarını alfabetik olarak sıralama
print(names)

str="opel,hyundai"#listeye cevirmek
str=str.split(",")
print(str)
markalar=[]
marka=input("marka listesine eleman ekle")
markalar.append(marka)
print(markalar)