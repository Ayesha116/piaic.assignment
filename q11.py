#Write a Python program to test whether a passed letter is a vowel or not
alpha = input("enter any character: ")
letter = alpha.lower()
if letter=="a" or letter=="e" or letter=="i" or letter=="u" or letter=="o":
    print("character is vowel")
else:
    print("characters is consonant")