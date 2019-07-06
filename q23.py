#Write a Python program to convert temperatures to and from Celsius, Fahrenheit
print("enter 1 to convert celsius in to fahrenhite")
print("enter 2 to convert fahrenhite in to celsius")
choice = int(input("enter choice: "))
if choice == 1:
    a = int(input("enter temp in celsius: "))
    print(a,"centigrades is equal to ",(1.8*a)+32,"fahrenhite")
elif choice ==2:
    b = int(input("enter temp in fahrenhite: "))
    print(b,"fahrenhite is equal to ",(b-32)/1.8,"centigrade")
else:
    print("you entered wrong choice")