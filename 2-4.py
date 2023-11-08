#write a program to accept marks of 6 students and display them in a sorted manner 
m1=input("enter marks 1:")
m2=input("enter marks 2:")
m3=input("enter marks 3:")
m4=input("enter marks 4:")
m5=input("enter marks 5:")
m6=input("enter marks 6:")
markslist=[m1,m2,m3,m4,m5,m6]
markslist.sort()
print(markslist)
