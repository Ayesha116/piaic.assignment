#Write a Python program to convert all units of time into seconds
year = int(input("enter time in years: "))*365*24*60*60
days = int(input("enter time in days: "))*24*60*60
hours = int(input("enter time in hours: "))*60*60
minutes = int(input("enter time in minutes: "))*60
seconds = year+days+hours+minutes
print(seconds,"seconds")
