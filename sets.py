a={1,2,3,4,5}
print(type(a))
print (a)#{1,2,3,4,5}
a={1,2,3,4,5,1}
print(a)#{1,2,3,4,5} so that proves set is a collection of non repititive/unique items

#identifying an empty set 
b={}
print(type(b))#<class 'dict'>#b={}this syntex will create empty dictionary  --- so why  
#the empty set can be created using the ----b=set(b)-------
b=set()
print(type(b))#<class 'set'> mission sucessful


#important rules of set
#you can not change the item of the set once its created but you can add items to the set 
#sets are unindexed and unordered .
#sets can not contain duplicate items  . 
#you can not chage the items of the set but you can add and remove items.
#if the item is not present in the set which you are tryong to remove then it will throw keyerror

#how to add items in the set 
b=set()
b.add(4)
b.add(7)
print(b)
b.remove(4)
print(b)
#{4, 7}
#so can we add dictiionaries , lists ?
b.add((4,5,8))
#print(b)#{(4, 5, 8), 4, 7} so we can add   tuples(unique)  to set bcz its cant be changed 
b.add([1,2])
print(b)#TypeError: unhashable type: 'list'(not unique)#so we canot add  lists to set bcz lists can change
b.add({
   4:5
})
#print(b)#TypeError: unhashable type: 'dict'(not unique)# so we can not ad  dict to a set bcz dict can change

