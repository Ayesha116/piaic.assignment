#Write a program to convert binary number to Decimal number

def binary_to_decimal(number):
    decimalNum = 0
    temp = str(number)      
    index = 0              
    for i in reversed(temp):
        decimalNum = decimalNum + (int(i) * (2 ** index))
        index += 1
    print("decimal number is",decimalNum)
a = int(input("enter binary number: "))
binary_to_decimal(a)


