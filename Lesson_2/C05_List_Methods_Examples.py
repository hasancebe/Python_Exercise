numbers=[1,3,5,7,15]
names=["hasan","ali""ahmet","can","selim"]
print(min(numbers))
print(max(names))
print(numbers[1:4])
names[1]="hüseyin"
print(names)
numbers.append(19)
print(numbers)
numbers.insert(2,78)
print(numbers)
names.insert(-1,"abdullah")
print(names)
names.pop()
print(names)
names.pop(0)
print(names)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.count(5))#5 kaç tane var
#numbers.clear()
#print(numbers)
print(numbers.copy())

