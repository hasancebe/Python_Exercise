#range

for l in  range(3,10):
    print(l)

for n in range(25,100,20):
    print(n)


#enumerate
greeting="hello"
for index,letter in enumerate(greeting):
    print(index ,"-",letter)

#zip
list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]

print(list(zip(list1,list2)))

for item in list(zip(list1,list2)):
    print(item)