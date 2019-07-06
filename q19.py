#Write a Python program to convert the distance (in feet) to inches, yards, and miles. 1 feet = 12 inches, 3 feet = 1 yard, 5280 feet = 1 mile
feet = float(input("enter height in feet: "))
print(feet,"feet is equal to",feet*12, "inches ") 
print(feet, "feet is equal to",feet/3, "yards") 
print(feet, "feet is equal to",feet/5280,"miles")  