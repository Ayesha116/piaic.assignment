#patter using nested loop
i = 6
for x in range(1,i):
    for y in range(1,x):
        print(y,end=" ")
    print(" ")
for z in range(i,1,-1):
    for a in range(1,z):
        print(a,end=" ")
    print(" ")