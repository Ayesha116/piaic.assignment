#Input a text and count the occurrences of vowels and consonant 
word = input("enter word: ").lower()
vowel = 0
consonant = 0
for i in word:
    if i=="a"or i =="e" or i == "o" or i == "u" or i == "i":
        vowel = vowel+1
    elif i =="b" or i =="c" or i =="d" or i =="f" or i =="g" or i =="h" or i =="j" or i =="k" or i =="l" or i =="m" or i =="n" or i =="p" or i =="q" or i =="r" or i =="s" or i =="t" or i =="v" or i =="w" or i =="x" or i =="y" or i =="z":
        consonant = consonant+1
print("vowels= ", vowel)
print("consonants= ",consonant)