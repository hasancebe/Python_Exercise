def usalma(number):


    def inner(power):
        return number**power
    return inner

powerValue=usalma(2)
print(powerValue(3))
