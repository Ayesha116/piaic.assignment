#Write a Python program to convert seconds to day, hour, minutes and seconds.
time= float(input("Input time in seconds: "))
days = time // (3600*24)
time = time % (3600*24)
hours =  time // 3600
time = time % 3600
minutes = time // 60
time = time%60
seconds = time
#print("d:h:m:s: %d:%d:%d:%d " % (days,hours,minutes,seconds)
print("%d"%(days),"days","%d"%(hours),"hours,","%d"%(minutes),"minutes,","%d"%(seconds),"seconds")