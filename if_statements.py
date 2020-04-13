is_male = True #is_male is a condition which uses simple boolean variables
is_tall = True
if is_male:
    print("You're a male ")
else:
    print("You're not a male")
print("---------------")
is_male = False
is_tall = True
if is_male:
    print("You're a male ")
else:
    print("You're not a male")
print("---------------")
is_male = False
is_tall = True
if is_male or is_tall:
    print("You're a male or tall or both ")
else:
    print("You're neither a male or tall or both")
print("---------------")
is_male = False
is_tall = True
if is_male and is_tall:
    print("You're a tall male ")
else:
    print("You're neither a male or tall or both")
print("---------------")
is_male = False
is_tall = True
if is_male and is_tall:
    print("You're a male or tall or both ")
elif is_male and not(is_tall):
    print("You're a short male")
elif not(is_male) and is_tall:
    print("you're not a male, but tall")
else:
    print("You're neither a male or tall or both")