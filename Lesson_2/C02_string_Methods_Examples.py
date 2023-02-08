
#baştaki sondaki boşlukları silme
message=" Hello World "
print(message)
message=message.strip()
print(message)
#sadece sadikturan yazısı kalacak şekilde silme
message1="www.sadikturan.com"
message1=message1.lstrip("www.")
message1=message1.rstrip(".com")
print(message1)
message1="www.sadikturan.com"
message1=message1.strip("w.com")
print(message1)

#tüm karakterleri küçük
message="Hello World"
message=message.lower()
print(message)

# kaç adet "a" var
message1="sadikturanakalacakheryerama"
index=message1.count("a")
print(index)

#"website  www ile başlıyor mu com ile bitiyormu
message1="www.sadikturan.com"
iswww=message1.startswith("www")
iscom=message1.endswith(".com")
print(iscom,iswww)
#website içinde com var mı
message1="www.sadikturan.com"
iscom=message1.find("com")
print(iscom)#bulunduğğu index numarasını yazar
iscom=message1.find("com",0,10)
print(iscom)#bulamayınca -1 yazar

#cümledeki herşey alfabatik mi
message1="www.sadikturan.com"
isalfa=message1.isalpha()
print(isalfa)
isnume=message1.isdigit()
print(isnume)
