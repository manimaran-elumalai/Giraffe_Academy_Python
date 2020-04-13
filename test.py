coordinates = (1,2,3)
a,b,c = coordinates # this is called unpacking
print(a*(b**c))
print((c**c))
print(c+a+b)
#### Dictionaries - use to store the key value pairs
customer = { # cureley braces are used to define the dictionary
    "name" : "John Smith", #name is the key and John Smith is the value
    "age" : 40,#key has to be always unique
    "Phone" : 23776966,
    "is_verified" : True
}
print(customer["name"])
print(customer.get("name"))
print(customer.get("D.O.B", "14th Aug 1977"))
customer["is_married"] = True
print(customer["is_married"])