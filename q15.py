#Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
a = float(input("please enter principle amount: "))
b = float(input("please enter rate of interest in %: "))
c = float(input("enter years of investment: "))
d = a*(1+b)**c
print("After ", c," years your principle amount ", a, "over an interest rate of ",b,"% will be ", d)