#python program to print even length strings/words.

#this question is ver very goodd lesson to learn string-split methhod.
#string-split method
#string.split(seperator,maxsplit) and not only that split method also turns the whole string into a list and turn elements into items
#but how will these  gonna help me find even length strings
n="this is a python language"
s=n.split(" ")
for i in s:
    if len(i)%2==0:#watch the behaviour closely here  , here i means items like is whole an item, this whole is an item 
      print(i)
    else:
        pass
    
# kind of main issue here is length  finding   
#using split(), for, len()
def printwords(s):
    s=s.split(' ')
for word in s:
    if len(word)%2==0:
        print(word)
s="i am musker"
print(printwords(s))

#main issue in length finding
#using list comparison()
n='geeksforgeeks'
s=n.split(" ")
print([x for x in s if len(x)%2==0])

#fuckimg did it 

        
