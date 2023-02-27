#encapsulation
def outer(num1):
    print("outer")
    def inner(num1):
        print("inner")
        return num1+1
    num2=inner(num1)
    print(num1,num2)

outer(10)

def factorial(number):
    if not isinstance(number,int):
        raise TypeError("number must be an integer")
    def innerFactorial(number):
        if number<=1:
            return 1
        return number * innerFactorial(number-1)

    return innerFactorial(number)

print(factorial(5))