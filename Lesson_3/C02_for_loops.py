numbers=[1,2,3,4]
for  number in numbers:
    print("hello")
    names=["hasan","husyin","ahmet"]
    for name in names:
        print(f"my name is {name}")

        name="abdullah"
        for n in name:
            print(n)

    tuple=([1,13],[2,3],[49,5])
    for t in tuple:
        print(t)

    d={"k1":1,"k2":2,"k3":3}
    for dic in d.items():#set küme elemanlarının hepsini yazdırma
        print(dic)

        for dic in d.keys():#set kümesindeki key değerleri yazdırma
            print(dic)

        for dic in d.values():#set kümesindeki value degerleri yazdırılır
            print(dic)

            