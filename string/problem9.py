#remove all duplicates from the string
#



#first thing is first is there any in built functions that can make our lives easy
#well yes in that case  it is set()-- as we already know set is a unique set of collction and suplicates doesnot exist for set
#


#attempt 1
k = "geeksforgeeks"
k2=[]
for ele in k:
    if ele not in k2:
        k2.append(ele)
for i in range(0, len(k2)):
    print(k2[i],end=" ")
    
    
#attempt 2
string="geeksforgeeks"
p=""
for char in string:
    if char not in p:
        p=p+char 
print(p)
k=list("geeksforgeeks")

#attempt 3

def removeDuplicate(str,n):
    s=set()
    for i in str:
        s.add(i)
        for i in s:
            st=st+i
        return st
    
str='geeksforgeeks'
n=len(str)
print(removeDuplicate(list(str),n))

#attempt 4
def removeDuplicate(sr):
    s=set()
    s=" ".join(s)
    print("without order:",s)
    t=" "
    for i in str:
        if (i in t):
            pass
        else:
            t=t+i
        print("withorder:",t)
str="geeksforgeeks"
removeDuplicate(str)

#fucking did it