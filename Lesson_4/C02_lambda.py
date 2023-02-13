def square(num):
    return num **2

numbers=[1,3,5,7]

result=list(map(square,numbers))
print(result)

#veya for döngüsüile yapılabilir

for item in map(square,numbers):
    print(item)


#veya lambda fonksiyonu kullanılabilir
result=list(map(lambda num: num ** 2,numbers))
print(result)