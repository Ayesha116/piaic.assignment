#Write a Python program to convert an integer to Binary, Octal and Hexadecimal numbers
def decimaltobinary(num):
    if num>1:
        decimaltobinary(num//2)
    print(num%2,end="")
def decimaltooctal(num):
    if num>7:
        decimaltooctal(num//8)
    print(num%8,end = "")
def decimaltohexadecimal(num):
    if num>16:
        decimaltohexadecimal(num//16)
    print(num%16,end="")
a = int(input("enter number: "))
decimaltobinary(a)
print("\n ")
decimaltooctal(a)
print("\n ")
decimaltohexadecimal(a)