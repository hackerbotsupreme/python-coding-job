#copying the list
#lets define what exactly the copying means it means making a list that is identical to another list

#rule 1;first think about tactic and try to find the fitting methods
#rule 2:second if nothing inmind, then think what mthods are falling into possible patterns

#attempt 1 :
#first thing i want to think about is is there any inbuilt function that can make my job easier
#well, yes that is-copy(list)
l=[1,2,3,4,5,6,7,8]
a=(l.copy())
print(a)
#fucking did it 


#attempt 2 
# secondly what we wnat to do is taking the list as a whole and store/make a new list which will be exacly same 
l=[1,2,3,4,5,6,7,8]
l1=[]
l1=l# what is intereting is every single differnce returns different result here when you write l=l1 that means i am putting value in right to the  value in left 
print(l1)#that is exactly why l=l1 didn't work 

#attempt 4
#so to this point i copied as it is but can we use some methods
#i think we can ---seems like append and slicing can be the options to go with 

# using append#list.append(item)
l=[1,2,3,4,5,6,7,8]
b=[]
for i in l:
    b.append(i)
    
print(b)


#attempt 5
#using slicing#list[start-index:end-index:indexjump]#also remember that the item of end index will not get printed
l=[1,2,3,4,5,6,7,8]
l_1=l[0:5]         #dont think about l[-1] bcz it will become item and we cannot add list and value 
l_2=l[5:7]         #l2=l_1+l_2+l_3
l_3=l[7:]          #TypeError: can only concatenate list (not "int") to list
l2=l_1+l_2+l_3
print(l2)        #concatenation means joining strings/lists together and end-to-end to create a new one.


