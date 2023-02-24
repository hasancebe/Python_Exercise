def faktoriel(x):
    x=int(x)

    if x<0:
        raise ValueError("negatif değer girildi")
    result=1

    for i in range(1,x+1):
        result*=i

    return result

for x in [5,4,-5,"10c"]:
    try:
        y=faktoriel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)


