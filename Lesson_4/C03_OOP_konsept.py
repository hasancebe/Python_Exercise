# class tanımlama

class Person:
    #class attribute
    address="no information"
    #consructor(yapıcı method)
    def __init__(self,name, year):
        self.name=name
        self.year=year
        print("init metodu çalışştı")

    #methods
    def intr(self):
        print("hello I am "+ self.name)

    def calculateAge(self):
        return 2023-self.year

#object
p1=Person("hasan",1988)
p2=Person("ahmet",2000)
p1.name="veli"
print(p1.name,p1.year,p1.address)
print(p2)
print(type(p1))
p1.intr()
p2.intr()
print(p1.calculateAge())
print(p2.calculateAge())