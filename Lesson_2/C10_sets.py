
#set tanımlaması süslü parantez arasında yapılır
#listelerdeki gibi index yapısı yoktur
#elemanları for döngüsü ile yazdırabiliriz
#pop()ile silme güvenli değildir sıralama olmadığı için hangi elemanın silineceğği önceden öngörülemez

fruits={"banana", "cherry","melon","apple"}
print(fruits)
fruits.add("watermelon")
print(fruits)
fruits.update(["apricot","pear"])
print(fruits)
myList=1,2,3,1,2,3,4,5,6
print(myList)
myList=set(myList)
print(myList)
#silme
fruits.remove("apple")
fruits.discard("melon")
print(fruits)