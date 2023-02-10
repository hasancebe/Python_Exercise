numbers=[1,3,5,7,9,12,19,21]

#3 ün katı olan sayıları yazdır
for n in numbers:
    if(n%3==0):
        print(n)
print("*"*50)
#listedeki tek sayilar
for teksayi in numbers:
    if(teksayi%2!=0):
        print(teksayi)
print("*"*50)
#sayıların toplamı kaçtır
toplam=0
for tn in numbers:
    toplam=toplam+tn
print(toplam)
print("*"*50)

cities=["istanbul","ankara","izmir","antalya"]
for city in cities:
    if(len(city)>5):
        print(city)
print("*"*50)

products=[
          {"name":"samsung s6", "price":3000},
          {"name":"samsung s7","price":4000},
          {"name":"samsung s8","price":9000}
]
totalprice=0
for urun in products:
    intprice=int(urun["price"])
    totalprice+=intprice
print(totalprice)
print("*"*50)
for urun in products:
    intprice=int(urun["price"])
    if(intprice<5000):
        print(urun["name"])