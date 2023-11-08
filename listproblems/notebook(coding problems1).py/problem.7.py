#reversing a following list  
l=[1,2,3,4,5,6,7]

#rule 1;first think about tactic and try to find the fitting methods
#rule 2:second if nothing inmind, then think what mthods are falling into possible patterns

  

#concept
#list.append(item/value we want to add)
#to reverse the list there is already a inbuilt function 
#which is list.reverse()

#attempt 1 
l=[1,2,3,4,5,6,7]
print(l)
l.reverse()
print(l)
#[1, 2, 3, 4, 5, 6, 7]
#[7, 6, 5, 4, 3, 2, 1]

#attempt 2                                                                      #works
   #l=[1,2,3,4,5,6,7]
   #k=[]
   #s=len(l)
   #for i in range(0,6):
   # k.append(l[s-i])#'int' object has no attribute 'append'
   #print('the current list',l) 
   #print('the reversed list',k)    
#i will review it later 

#attempt 2 : reversing the list using 'for'
#for syntax- for this in this 
#example-for 7 in list :
l=[1,2,3,4,5,6,7]
h=[]
for i in l:
    h.append(i)
h.reverse()
print(l)
print(h)


#attempt 3                                                                      #works
# using insert( index, value we want to insert )here 
# we used the index as lock in /door for entry and then inserted all the list
# and we also used the fact that i/item in a list traverse from left to right 
#and with lockin when we inser list items it also inserted from left to right  
l=[1,2,3,4,5,6,7]
h=[]
for i in l:
    h.insert(0,i)
print(l)
print(h)



#attemmpt 4                                                                      #works
#using slicing tecnique in list 
#syntax-list[start-index:end-index:indexjump]
#here actually we are printing from 0th index all the way to endth index where 

def reverse(list):                                                                             
    new_list=list[::-1]
    return new_list
j=reverse([1,2,3,4,5,6,7])
print('************')
print(j)


c=[1,2,3,4,5,6,7]
d=c[::2]#as here we have written 2 means it have to jump two nnumbers and it wil be like print 1 jump 1and 2 again print 3 jump 3and 4 and so on#ami jekhan theke jota bolechi seta janar por 
#porei --indexjumping+printing --start hobe jekhane jotogulo number jump korte hobe otar starting prothom element thekei hobe 
print(c)
print(d)
#but still how does it works in case of -1?
#exactly for -1, first it will see range of index  user told to print and then for jumping it wil
#see that -1 is given it will tell ok i have to print and jump values from the right direction
#(remember indexing always starts from left ) and jump every first value so for above 
#case print 7 (start item/jump starts/jumping 1 item)then jump to 6 and print 6
# similarly jump to 5 and print 5 and so on.........   