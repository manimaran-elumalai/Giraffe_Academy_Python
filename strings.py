#Strings (is a common data type) basically a plain text and always comes within quotation mark
print("Mani's Learning") 
print("Mani's\nLearning") #will print learning on the 2nd line bcos of \n
print("Mani's\"Learning")
print("Mani's\Learning")

#Creating a Variable and assigning the string value to it
phrase1 = "Mani's Learning"
print(phrase1)
print(phrase1 + " is cool") # Concatenation - Taking a String Value and appending it with another string
print(phrase1.lower()) #lower is a function which will convert the string into lower case (functions are nothing but block of codes)
print(phrase1.upper())
print(phrase1.isupper()) #This functions checks if the String value assigned to phrase one is upper and it will return False as output
print(phrase1.upper().isupper()) #This will return the output as True
print(len(phrase1)) #will return the length of the string
print(phrase1[0]) #this will return the individual characters in the string
print(phrase1.index("M")) #this will return the index value of the characters checked / where the character started if it is multiple same character
print(phrase1.replace("Mani's", "Rahul's")) #Replaces the entire string or a specific character within the string
