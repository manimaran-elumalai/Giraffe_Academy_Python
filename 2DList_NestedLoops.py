4#Creating list within list
number_grid = [
    [1,2,3],#Row 1 List
    [4,5,6],#Row 2 List
    [7,8,9],#Row 3 List
    [0]#Row 4 List
]
print(number_grid[0] [0])
print("-----------------")
number_grid = [
    [1,2,3],#Row 1 List
    [4,5,6],#Row 2 List
    [7,8,9],#Row 3 List
    [0]#Row 4 List
]
print(number_grid[1] [2]) #prints the 2nd row and 3rd column element

#Using Nested FOR LOOP
print("2D List/Array with nested for loop")
number_grid = [
    [1,2,3],#Row 1 List
    [4,5,6],#Row 2 List
    [7,8,9],#Row 3 List
    [0]#Row 4 List
]
for row in number_grid:
    print(row)


print("-------------")
number_grid = [
    [1,2,3],#Row 1 List
    [4,5,6],#Row 2 List
    [7,8,9],#Row 3 List
    [0]#Row 4 List
]
for row in number_grid:
    for col in row:
        print(col)