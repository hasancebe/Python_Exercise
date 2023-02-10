import random
i=random.randint(0,100)
haksayisi=int(input("kaç denemede bulmak istesiniz? "))
puan=100
#print(i)
boolEslesme=True
count=0
eksilecekPuan=100/haksayisi
while (boolEslesme):
    if(haksayisi>0):
        j=int(input("sayı giriniz"))
        if(i==j):
            print("tebrikler", count,"denemede sayıyı buldunuz puanınız", puan)
            boolEslesme=False
        elif(i<j):
            print("daha küçük sayı giriniz")
            puan=puan-eksilecekPuan
        else:
            print("daha büyük sayı giriniz")
            puan=puan-eksilecekPuan
        haksayisi-=1
        count+=1
    else:
        boolEslesme=False
        print("hakkınız kalmadı. sayı ",i , "olmalıydı" )