#python program to check whether the string is syymetrical or palindrome .
#ok lets analyze the question so syymetrical means  , a string is said to be syymetrical if both the halves
# of the string are the same and a string is said to be a paindrome string if one half of the string is the 
# reverse of the other half or if a string appears same when read forward or backward.

#first we gonna think  is
#attempt 1
#1.find reverse of the string
#2.chechk if the reverse and original are same or not.
def ispalindrome(s):
    return s==s[::-1]
s="malayalam"
ans=ispalindrome(s)
if ans :
    print("yes")
else:
    print("no")

#attempt2                                                                                               #works
#using extend() and reverse() methods
def ispalindrome(s):
    x=list(s)
    y=[]
    y.extend(x)
    x.reverse()
    if (x==y):
        return True
    else:
        return False 
s="malayalam"
ans=ispalindrome(s)
if ans:
    print("yes")
else:
    print("no")
# yes is the ans 
# fucking did it


#attempt 3                                                                                            #works
x="malayalam"
w=" "
for i in x:
    w=i+w
if (x==w):
    print("yes")
else:
    print("no")