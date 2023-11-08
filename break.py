# first example of break statement 
for i in range(10):
    print(i)
    if i==5:
        break#o to 5 will be printed 
else:
    print("this will get printed when the loop exhausts")#when you use break before else then the else statement will not get executed because whether the loop neither gets exhausted even end before reaching to else
#second example of break statement
for i in range (0,80):
    print(i)
    if i==3:
        break#0 to 3 will get printed