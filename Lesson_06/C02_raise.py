
"""
x=10
if x>5:
    raise  Exception("x 5 den büyük olamaz");


def check_password(psw):
    import re
    if len(psw)<8:
        raise  Exception("parola en az 8 karakter olmalı")
    elif not re.search("[a-z]",psw):
        raise  Exception("parola küçük harf içermeli")
    elif not re.search("[A-Z]",psw):
        raise  Exception("parola büyük harf içermeli")
    elif not re.search("[0-9]",psw):
        raise  Exception("parola rakam içermeli")
    elif not re.search("[_@$]",psw):
        raise  Exception("parola alfanümerik karakter içermeli")
    elif  re.search("\s",psw):
        raise  Exception("parola boşluk içermemeli")

password="123456789a_M"

try:
    check_password(password)
except Exception as ex:
    print(ex)

else:
    print("geçerli parola: else")

finally:
    print("validation tamamlandı")

"""
class Person:
    def __init__(self,name,year):
        if len(name)>10:
            raise  Exception("name alanı fazla karakter içeriyor")
        else:
            self.name=name

p=Person("Aliiiiiiiiiiiiiiiiiiiiiiiii",1989)



