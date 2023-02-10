sayi=int(input("sayi giriniz"))
if sayi==1:
    print("1 sayisi asal değildir")
asalmi=True
for i in range(2,sayi):
    if(sayi%i==0):
    #    print("sayi asal değildir")
        asalmi=False
        break
if asalmi:
    print("asaldir")
else:
    print("asal değildir")