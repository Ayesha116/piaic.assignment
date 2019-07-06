#5.	Write a Python program to calculate number of days between two dates
from datetime import date
print("Enter the first date please: ")
first_date = date(int(input("\t\t\tYear: ")), int(input("\t\t\tmonth: ")), int(input("\t\t\tday: ")))
print("Enter the second date please: ")
last_date = date(int(input("\t\t\tYear: ")), int(input("\t\t\tmonth: ")), int(input("\t\t\tday: ")))
delta = first_date-last_date
print("There are ",delta,"days")