def max_number(Num1, Num2, Num3):
    if Num1 >= Num2 and Num1 >= Num3:#>= is a comparison operators and max_number is the function being created.
        return Num1
    elif Num2 >= Num3:
        return Num2
    else:
        return Num3
print(max_number(213,53,217))
print("------------------------")
def max_number1(Num1, Num2, Num3):
    if Num1 <= Num2 and Num1 <= Num3:#<= is a comparison operators and max_number1 is the function being created.
        return Num1
    elif Num2 <= Num3:
        return Num2
    else:
        return Num3
print(max_number1(213,53,217))