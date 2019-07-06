# Write a Python program to get the Fibonacci series between 0 to 50
first_num = 0
second_num = 1
print(second_num,end = ",")
for i in range(1,49):
    next_num = first_num+second_num
    if next_num<50:
        print(next_num,end = ",")
        first_num = second_num
        second_num = next_num