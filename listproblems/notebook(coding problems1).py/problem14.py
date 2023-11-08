#dind the second largest number in the list 

#first if there is any in-built function that fits our needs 
# well yes we can use  max() function and we can use sorting in both ways
# in descending and ascending order 

#attempt 1
#sort in ascending option:low to high
list=[1,2,7,8,4,6,0,5]
list.sort()
list.remove(max(list))#or list.remove(list[1])
print("the second largest numberis",list[-1])


#and similarly
#attempt 2
#sorting in decending order :high to low
list=[1,2,7,8,4,6,0,5]
list.sort(reverse=True)#wht -1 is not fot here --must need to know
list.remove(max(list))
print("thr second largest number in the list is ",list[0])
 

#attempt 3 
#kick out the second largest 
#we will use max() function to find the largest  then kick out that
list=[1,2,7,8,4,6,0,5]
newlist=set(list)
newlist.remove(max(newlist))
print("the second largest numberis",max(newlist))


#attempt 4
#a new mthod: we will sort an dprint
list=[1,2,7,8,4,6,0,5]
print("second  largest element",sorted(list)[-2])
# super cool




