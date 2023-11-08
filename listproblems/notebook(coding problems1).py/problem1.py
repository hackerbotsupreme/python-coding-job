#write  a python program to interchange first and last items in the list
#l=[1,2,3,4,5]--->l=[5,2,3,4,1]                     #scroll down to the end to see solution


#concepts
#key learnings from this question is how list.insert function works 
#list.insert -- l.insert(index,value)--value we want to put-basically we  use this  to put a value 
# to an partincular index so with this a question also arises that is what happens with the value 
#that was previously there well as we said computer first put values to the indexes accorading to where
#we have told him so then he indexes are left to fill and he takes the list as a whole
#and rearrange that accorading to empty indexes. to understand more precisely look through
#the following of this problem explanation # in this problem we will also cover list.remove:
#list.remove  -----l.remove(value)--item  of the list we want to delete--->  
#lisi.pop ---- l.pop(index)----index item will be deleted and the list will gets rearranged 
# deletes/removes the item from the list from where they  first finds them

#explanation ------------------------------------of solving the problem using the concept

# in this problem we told him to put 5 at the 0 index and 1 at the 4 index(as the index 
# count starts fom 0 and left) so he puts it then he sees that the indexes from 1 to 3
# (3 index)are blank so computer will take first (3 items) of the given list/
# before changed/  l=[1,2,3,4,5]  which is 1,2,3 put it to the (1 to 3)index then
# he will take the rest of the items and put it to rest empty index where the extra
# index will be created too.



#attempt 1 
l=[1,2,3,4,5]
print('list before interchanging',l)
l.insert(0,5) 
l.insert(4,1)
l.remove(1)
l.pop()#cant use pop cause its rearranges the inserted value which doesn't work to resolve  #to this point output is---[5, 1, 2, 3, 1, 4, 5]
print(l)                                   # l.remove is not fits our needs -->l.remove(5)
#so this flow is not exactiy solving our problem but


#tip:so tip we can get from attempt 1 is if we somehow 
# interchange and lock in the values with the index/positions then we can find the flow to solve  can go better


#quick revise
#how many list methods are there and what are they?
#6 --pop
#remove
#reverse
#inverse
# append 
# sort

#attempt 2                                                                          #works
#tip 1:so tip we can get from attempt 1 is if we somehow 
# interchange and lock in the values with the index/positions then we can find the flow to solve  can go better
#acoorading to the tip 1 list methods dont have the required command
#so if we need to create command or set of command we can go with def func 
#lets try ----def function


def  swaplist(list):
    size=len(list)
    temp=(size-1)
    list[0]=list[temp]
    return list
l=[1,2,3,4,5]
print(l)
l1=swaplist(l)
print("the list after interchaging the values",l1)                                  


#attempt 3                                                                          #works


#just analyzing the question we can say one thing that is we know the indexes
#and the idea is we just need to swap them so
l=[1,2,3,4,5]
print(l)
l[0],l[-1]=l[-1],l[0]
print(l)


#attempt  4                                                                        #works


#also by analyzing the question we seen that the lists methods dont have the required commands 
#to resolve the question but clearly we can say if there is any func which has
#1.has the function to access the the items.2.allowed to interchange  the items  
#list
#tuple
#set
#dictionary
#strings
#the should be between set and tuple
#set does not allows innterchanging of items
#tuple does but is that have the required methods?
#


# the idea swap is store the first and last elements as a 
#pair in tuple variable and then  swap 
get=list[0],list[-1]
get=list[-1],list[0]
print(l)