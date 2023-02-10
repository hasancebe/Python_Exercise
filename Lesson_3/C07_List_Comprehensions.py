numbers=[x for  x in range(10)]
print(numbers)

numbers1=[]
for x in range(10):
    numbers1.append(x)
print(numbers1)

numbers3=[x*x for x in range(10) if x%3==0]

print(numbers3)

str="hello"
myList=[letter for letter in str]
print(myList)

results=[a if a%2==0 else 'tek' for a in range(1,10)]
print(results)

numbers4=[(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers4)