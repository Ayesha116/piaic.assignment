#Write a Python program to compute the greatest common divisor (GCD) of two positive integers. 
a = 0
def GCD(num1,num2):
        gcd = 0
        for i in range(1,num2+1,1):
                if num1%i==0 and num2%i==0:
                        gcd = i
        print(gcd)


numerator = int(input("enter numerator: "))
denominator = int(input("enter denominator: "))
GCD(numerator,denominator)
    