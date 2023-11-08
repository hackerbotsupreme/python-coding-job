#print the folloeing pattern
# *
# **
# ***
#*****
#lets do it for  n=3
#n=3
#for i in range(3):
#    print(" " *(n-i-1))#
#    print("*" *(2*i+1))#*****
#    print(" " *(n-i-1))#
n=3
for i in range(3):
    print(" " *(n-i-1),end="")#
    print("*" *(2*i+1),end="")#*   *** *****
    print(" " *(n-i-1),end="")#
