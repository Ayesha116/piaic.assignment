#Write a Python program to count the number occurrence of a specific character in a string
word = input("enter string: ").lower()
specific_characters = 0
for i in word:
    if i == "=" or i == "'" or i == ";" or i == ":" or i == "|" or i == "!" or i =="," or i == "*" or i == "^" or i == "$" or i == "%" or i == "#" or i == "@" or i == "<" or i == ">" or i == ".": 
        specific_characters = specific_characters+1
print("specific charcters = ",specific_characters)