# list ---[] and tuples---{}
a=[1,2,3,4,5,7]#list # look at the format its just like strings and also uses []
print(a[0])#indexing goes like --obviously from the left---012345,  #so we can also print any of the elements like-- print(a[0])
a[1]=20#[1,20,3,4,5,7]#we cant change items for strings but we can change the items in case of lists
print(a)

#print the list using print()
print(a)

#access using index using a[0],a[1],a[2]
print(a[2])

#change the value of list using 
a[0]=57

#we can also create a list with different types of values
c=[45,"harry",6.9,True]
print(c)

#like strings we can also slice the lists
number=(1,2,3,4,3.5)#counting starts from left, the end-index is  not getting printed 
print(number[0:3])# and  to access the last item we will use negative-indices here too
print(number[-1])#and similarly we can print the series of items to end-tems like
print(number[-3:])#(3,4,3.5)#this
print(number[-3:-1])#(3,4)# -1(3.5) will not be printed as its end-index 

