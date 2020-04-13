#function is a collection of codes which performs a specific task
#it allows to organize a code in a better way and allows to break the code
def say_hi(): #when def is used it will create a funtion type and all the codes keyed in will be stored under this.
    print("Hello " + input("please enter your name: ")) #this code will not be executed automatically until it is called separetely.

print("Beginning")
say_hi()
print("Ending")
#parameter is a piece of information given to functions that are being created.
def say_hello(name, age): #here name & age is the parameter and you can assign as many parameters you want to
    print("Hello " + name + ", you're " + age + " years old.")

say_hello("Mani", "43")
say_hello("Mohan", "43")

def say_hello1 (name, age):
    print("Hello " + name + ", you're " + str(age) + " years old.") #here we're converting the int (age) to a str

say_hello1("David", 18)