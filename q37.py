#Write a Python program to reverse the digits of a given number and add it to the original, If the sum is not a palindrome repeat this procedure
def digit_palindrome(num):
    rev = int(str(num[::-1]))
    add = str(int(num)+rev)
    add_rev = add[::-1]
    if add_rev == add:
        print(add)
    else:
        return palindrome
a = input("enter num: ")
digit_palindrome(a)
