#Write a Python program to create the multiplication table (from 1 to 10) of a number
a = int(input("enter number: "))
for i in range(1,11):
    x = a*i
    print(a,"x",i,"=",x)
