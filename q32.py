#Write a Python program to get the least common multiple (LCM) of two positive integers 
def LCM(a,b):
    if a > b:
        lcm = a
    else:
        lcm = b

    while True:
        if (lcm % a == 0) and (lcm % b == 0):
            print("lcm is ",lcm)
            return lcm
        lcm += 1
number1 = int(input("enter number1: "))
number2 = int(input("enter number2: "))
LCM(number1,number2)