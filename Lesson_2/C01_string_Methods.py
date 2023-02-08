message="My name is hasan cebe"
message=message.upper()
print(message)
message=message.lower()
print(message)
message=message.title()
print(message)
message=message.capitalize()
print(message)
message="  My name is hasan cebe"
message=message.strip()
print(message)
message=message.split()
print(message)
message="My name is hasan cebe"
message=message.split("a")
print(message)
print("---------------------------------------------")
message="My name is hasan cebe"
message=message.split()
print(message)
message=" ".join(message)
print(message)

message="My name is hasan cebe"
message=message.split()
print(message)
message="**".join(message)
print(message)
print("-------------------------------")

message="My name is hasan cebe"
print(message)
index=message.find("name")
print(index)
isFound=message.startswith("M")
isFound1=message.startswith("f")
print(isFound)
print(isFound1)

print("-----------------------------")
message="My name is hasan cebe"
print(message)
message=message.replace("name","isim")
print(message)
message=message.replace("s","ğ")
print(message )
message=message.center(100)
print(message)
