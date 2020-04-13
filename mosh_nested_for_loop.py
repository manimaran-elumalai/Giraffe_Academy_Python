tables = [6,7,8,9,10]
for x in tables:
    for y in range(1,10):
        print(str(x) + " x " + str(y) + " = " + str(x*y))
    print("\n*****************\n")

### BELOW CODE PRINTS x based on the items in numbers variable
numbers = [2,2,2,5,6]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)
print("\n*****************\n")



tables = [2,3,4,5,6]
for x in tables:
    for y in range(1,11):
        print(str(x) + " x " + str(y) + " = " + str(x*y))
    print("\n******\n")

### Finding the max number
numbers = [3,1,10,15,24,18]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
