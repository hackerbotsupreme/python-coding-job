t=(1,2,3,4,5,6,7)#look at the syntax tuples contains -----()
print(t[0]) # we can  print items in tuples  

#cannot update the values of a tuple #once a tuple is defined it can not be changed
t[0]=20
print(t)#'tuple' object does not support item assignment means we can not change items in tuple 

#empty tuple 
t=()

#tuple with one element needs a comma 
t=(1,)#syntax of a single element tuple

#tuple with more than one element 
t=(1,2,3,4,5,1,2,1)

#count of an item 
print(t.count(1))

#finding an index of a item
print(t.index(1))

