students={
    "120":{
        "name":"Ali,",
        "surname":"yilmaz",
        "tel":123456
    },
    "126":{
        "name":"veli",
        "surname":"can",
        "tel":789456
    }
}
students1={}
no=input("enter no")
name=input("enter name")
surname=input("enter surname")
phone=input("enter phone number")
'''
students1[no]={
    "name":name,
    "surname":surname,
    "tel":phone

}
'''
students1.update({
    no:{
        "name":name,
        "surname":surname,
        "tel":phone
    }
})
print(students1)
print("*"*50)
