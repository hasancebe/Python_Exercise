def sayHello(name="user"):
    print("hello", name)

sayHello("hasan")
sayHello()

def sayHi():
    return "hello"


str=sayHi()
print(str)

def total(n1,n2):
    return n1+n2
print(total(5,6))

def add(*params):
    return sum(params)

print(add(10,20,30))
print(add(5,7))