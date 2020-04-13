#list is a struture in python which can store list of information and allows us to keep organised and tack them lot easier. 
#You'll normally put related value into the list and use it throughout the particular programming cycle.
friends = ["Christy", "Rahul", "Mohan", "Jyothi", "Kavin"] #friends in this is a list name and Christy, Rahul and others are elements with Index Value of 0 - 4.
friends[1] = "David Richardson" #lists elements are mutable
print(friends)
print(friends[4])
print(friends[1:])
print(friends[:4]) #Will print all the elements from the beginning upto 4 but not 4
print(friends[:-1])
friends[4] = "Kavin Kishore"
print(friends)