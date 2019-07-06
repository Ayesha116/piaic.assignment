#Write a Python program that accepts a string and calculate the number of digits and letters Sample Data : Python 3.2, Expected Output : Letters 6, Digits 2
word = input("enter word: ").lower()
alphabet = 0
number = 0
for i in word:
    if i=="a"or i =="e" or i == "o" or i == "u" or i == "i" or  i =="b" or i =="c" or i =="d" or i =="f" or i =="g" or i =="h" or i =="j" or i =="k" or i =="l" or i =="m" or i =="n" or i =="p" or i =="q" or i =="r" or i =="s" or i =="t" or i =="v" or i =="w" or i =="x" or i =="y" or i =="z":
        alphabet = alphabet+1
    elif i == "1" or i == "2" or i == "3" or i =="4" or i =="5" or i == "6" or i =="7" or i =="8" or i == "9" or i =="0":
        number = number +1
print("letters =",alphabet)
print("digits = ",number)