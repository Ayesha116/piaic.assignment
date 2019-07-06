#3.	Write a Python function to check whether a number is completely divisible by another number. Accept two integer values form the user
a = int(input("Enter numerator: "))
b = int(input("enter denominator: "))
if a%b==0:
    print("Number ",a,"is completely divisible by number", b)
elif a%b!=0:
    print("Number ",a,"is not completely divisible by number", b)