class Person():
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        print("person created")

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
        print("student created")


p1= Person("ali","yilmaz")

s1=Student("veli","can")

