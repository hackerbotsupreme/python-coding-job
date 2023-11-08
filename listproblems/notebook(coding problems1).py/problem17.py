#write a python program to count positive and negative numbers  in a list.

#first things first is there is anything in built that can make our job easy 
#sum() method + list comprehension
#list comprehension - reurn value for (variable in iterator)(condition )
#x for (x in range(10))- when x mets this condition only that x will return
# it is telling like you will return x for  every x mets condition  as true 
l=[-1,2,-3,45,6,-7,-8,9]
x=sum( num for num in l if num>=0 )
print("the positive numberss in the list:",x)
print ("the negative  numbers in the list is  :",len(l)-x)