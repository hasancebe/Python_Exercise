def my_decorator(func):
    def wrapper():
        print("fonksiyondan önce ki işlemler")
        func()
        print("fonksiyondan sonra ki işlemler")
    return wrapper
def sayHello():
    print("Hello")

def sayGreeting():
    print("Greeting")

sayHello=my_decorator(sayHello())
sayHello()