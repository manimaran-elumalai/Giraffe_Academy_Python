message = input("< ")
words = message.split(" ") # this split function will split the words into separate item whenever it sees the space
print(words)
emojis = {
    ":-)" : " 😀",
    ":-(" : " 😟"
}
output = " "
for word in words:
    output += emojis.get(word, word) + " "
print(output)