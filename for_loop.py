#For loop is a special type of loop allows to loop over different collections of items - arrays strings.
print("--------")
for letter in "Giraffe Academy": #for every letter in the Giraffe Academy
    print (letter)

print("---------")

print("--------")
friends = ["David", "Rahul", "Richardson"]
for friend in friends:
    print(friend)

print("---------")
friends = ["David", "Rahul", "Richardson"]
for index in range(10):
    print(index)

print("---------")
friends = ["David", "Rahul", "Richardson"]
for index in range(len(friends)):
    print(index)

print("---------")
friends = ["David", "Rahul", "Richardson"]
for index in range(len(friends)):
    print(friends[index])
print("-----------")
for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not First")
