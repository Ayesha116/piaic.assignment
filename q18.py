#	Write a Python program to calculate the hypotenuse of a right angled triangle
import math
base = int(input("enter base in cm: "))
perp = int(input("enter perrpendicular in cm: "))
hypo = math.sqrt(base**2+perp**2)
print("hypoteneous of triangle is ",hypo, "cm")