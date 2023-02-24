liste=["1","2","5a","10b","abc","10","50"]
#Question: print only include number value
def checkNumber(liste):

    i=0
    while i<=len(liste)-1:
        import re
        if not re.search("[a-z]",liste[i]):
            print(liste[i])
        i+=1


checkNumber(liste)

def check_number1(liste):


        for x in liste:
            try:
                result=int(x)
                print(result)
            except ValueError:
                continue
print("*"*50)
check_number1(liste)