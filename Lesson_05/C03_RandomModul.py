import  random
result=dir(random)
#print(result)
result=random.random()
result=random.random()*100
result=int(random.uniform(10,100))
result=random.randint(20,35)
print(result)
names=["ali","yagmur","ahmet"]
#result=names[random.randint(0,len(names)-1)]
result=random.choice(names)
greeting="hello there"
result=random.choice(greeting)
liste=list(range(10))
random.shuffle(liste)
result=liste
result=random.sample(liste,2)

print(result)