cars=["bmw","opel","honda","toyota","fiat"]
print(cars)
print(len(cars))#eleman sayısı
#listenin son elemanını yazdır
print(cars[len(cars)-1])
print(cars[-1])
#opel'i mazda ile değiştir
cars[1]="mazda"
print(cars)
isthere="bmw" in cars#listede var mı
print(isthere)
#listenin ilk 3 elemanı yazdır
print(cars[0:3])
print(cars[3:])

#listenin son iki elemanı yerine renault ve nissan yapalım
cars[-2:]=["renault","nissan"]
print(cars)
#ekleme
cars=cars + ["tofas","mercedes"]
print(cars)
#silme
del cars[-1]
print(cars)
#tersten yazdır
print(cars[::-1])
print("----------------------------")
student1=["yigit", "bilgi",2010,[70,80,90]]
student2=["sena","yalcın",2011,[80,80,90]]
student3=["ahmet","kiraz",2011,[100,90,80]]
result=f"adı soyadı {student1[0]} {student1[1]} dogumu {student1[2]} not ortalaması {(student1[3][0]+ student1[3][0]+student1[3][0])/3} "
print(result)


