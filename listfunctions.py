l = [1,2,3,4,5,6]
print (l)#(1,4,5,2,3,6)
l.sort() #l=l.sort()/l1=l.sort()#none is result in terminal--its not a valid metthod and look closely to this as this is how computer recognizess a change in func
print(l)#(1,2,3,4,5,6)#dont valid to save the chage as that will change the identity just change it and print it
#so 

#sorts the list 
l.sort()

#reverse the list 
l.reverse()

#appends at the end of the list 
l.append(90)
print(l)

#inserts given num at the given index by poping the current num
l.insert(0,5647)
print(l)

#pop(removes) the num from the given index and return its value
l.pop(3)
print(l)

#remove/delete the num from the given index 
l.remove(5)
print(l)