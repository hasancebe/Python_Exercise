#soru:kullanıcıdan alınan iki tamsayıdan xyz toplamını çıkaralım
x,y,z=5,16,19
numbers=1,2,3,4,5,6
number1=input("1.numarayı giriniz")
number2=input("2.numarayı giriniz")
number3=int(number1)*int(number2)
result=number3-(x+y+z)
print(result)

#soru y nin x kalansız bölüm sonucu kaçtır
print(y//x)
#soru:xyz toplamının mod3'ü nedir
print((x+y+z)%3)
#y nin x'inci kuvveti
print(y**x)
#x,*y,z=numbers işlemine göre z nin küpü kaçtır
x,*y,z=numbers
print(y)
print(z)
print(z**3)
#bu işlemde y değerleri toplamı kaçtır
toplam=y[0]+y[1]+y[2]+y[3]
print(toplam)


