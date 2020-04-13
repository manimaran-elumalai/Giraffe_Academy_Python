friends = ["Christy", "Rahul", "Mohan", "Jyothi", "Kavin"]
lucky_numbers = ["2", "4", "6", "8"]
friends1 = friends.copy()
print(friends1)
friends.extend(lucky_numbers) #extend(extend is a list function) the elements of the other lists to the friends list
print(friends)
friends.insert(4, "David") #add a new element to the specified index position
print(friends)
friends.append("Manimaran") #add the new string to the existing list at the last index position
print(friends)
friends.sort()
print(friends)
friends.remove("Manimaran")
print(friends)
print(friends.index("Rahul")) #to find if the element is part of the list or not - if yes, it'll return the index position, else an error.
print(friends.count("Kavin")) #to count how many times the element is there in the list
print(friends)
friends.pop(2)
print(friends)
friends.clear()
print(friends)
lucky_numbers.reverse()
print(lucky_numbers)
