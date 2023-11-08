#write a program to sap/inteerchange two elements in a list
                                                  #scroll down to the end to see solution


#rule

#rule 1;first think about tactic and try to find the fitting methods
#rule 2:second if nothing inmind, then think what mthods are falling into possible patterns


#concepts

#first thing first is there any list method that can help  me out 
#what we need , swap the elements/or we can say plug elements from one index and put it to another
#plug-- pop, put in the position--insert  so
#yes we can go with list methods


#Attempt 1
def SwapList(list ,pos1, pos2):
    a=list.pop(pos1)
    b=list.pop(pos2-1)
    list.insert(pos2-1,a)# i really need to find why the second index number is needing to be substracted by one
    list.insert(pos1,b)
    return list
    

x=SwapList([1,2,3,4,5],0,1)
print("the list after interchanging  items",x)
f=SwapList([1,2,3,4,5,8,9,7],2,6)
print("the list after interchanging  items",f)


#quick revise\
#list.pop(index)--- pops the item present in that index and stores it at the same time 
#list.insert(index,vlaue yhat we want to put on that index)


#attempt 2                                                              #more reliable#works
#lets store and exchange the items
def swappositions(list,pos1, pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
w=[1,2,3,4,5,8,9,7,0]
e=swappositions(w,2,6)
print(e)



#attemppt 3
def swapfunctions(list,b,c):
    get=list[b],list[c]
    give=list[c],list[b]
    get=list[c],list[b]
    give=list[b],list[c]
    return list
w=[1,2,3,4,5,8,9,7,0]
e=swappositions(w,2,6)
print(e)


    






    
    
    
    







  