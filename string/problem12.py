#write a program to check if a string contains any special charecters in the string
#it smells like it will use loops paired with a set if special charecters  
# so what exactly we gonna do is  , firstly group all special charecters as one set then using for loop and 
# if statements check for special charecters ,if any special charecters is found  then increment th value of c .
# finally check if the c value is not acceptes otherwise print string is accepted.

n="geeks$for$geeks"
n.split()
c=0
s='[%^&&&*()^%$]'
for i in range(len(n)):
    if n[i] in s :
        c+=1
        
if c:
    print("string is not accepted")
else:
    print("string accepted")

#fucking did it
