numbers=[1,3,5,7,9,12,19]
#listeyi while ile yazdırın
count=0
while(count<len(numbers)):
    print(numbers[count])
    count+=1

#başlangıç ve bitişş değerlerini kullanıcıdan alarak aradaki tek sayıları yazdır
sayi1=int(input("başlangıç sayıyısını giriniz: "))
sayi2=int(input("bitiş sayıyısını giriniz: "))
numbers1=[1,3,5,7,9,12,19,21,35]
count1=0
while(count1<len(numbers1)):
    if(numbers1[count1]>sayi1 and numbers1[count1]<sayi2):
        if(numbers1[count1]%2==1):
            print(numbers1[count1])
    count1+=1

#1000 den geriye sayıları yazdır
sayi3=100
while(sayi3>0):
    print(sayi3)
    sayi3-=1

#kullanıcıdan alacağınız 5 sayıyı sıralı şekilde yazdırın
sayilar=[]
i=1
while i<=5:
    n1=int(input(f"{i}. sayyıyı giriniz:"))
    i+=1
    sayilar.append(n1)
sayilar.sort()
print(sayilar)