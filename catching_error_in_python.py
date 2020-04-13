# try and except our program

try:
    number = int(input("Please Enter a Number: "))
    print(number)
except:
    print("Invalid Number")

print("____________")
try:
    value = 10/0
    number = int(input("Please Enter a Number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by Zero")
except ValueError:
    print("Invalid Number")

print("____________")
try:
    value = 10/0
    number = int(input("Please Enter a Number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Number")