class Circle:
    pi=3.14

    def __int__(self, yaricap=1):
        self.yaricap=yaricap

    def cevre(self):
        return 2*self.pi*self.yaricap

    def alan(self):
        return  self.pi*(self.yaricap**2)


c1=Circle()
c1.yaricap=4.5
print("alan",c1.alan())
print("çevre",c1.cevre())