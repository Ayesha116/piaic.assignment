#Write a program to convert Octal number to Decimal number
def octaltodecimal(number):
    Decimalnum = 0
    a = str(number)
    power = 0

    for i in reversed(a):
        j = int(i)
        Decimalnum = Decimalnum+ j*(8**power)
        power+=1
    print("after converting octal to decimal: ", Decimalnum)


user_input = int(input("enter number in octal: "))
octaltodecimal(user_input)