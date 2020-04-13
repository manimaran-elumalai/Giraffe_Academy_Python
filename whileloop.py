a = 1
while a <= 50: #a<=50 is the loop condition
    a += 1
    remainder = (a % 3)
    remainder1 = (a % 10)

    if remainder == 0:
        print ("fizz")
    elif remainder1 !=0:
        print (a)
print("done with the loop")