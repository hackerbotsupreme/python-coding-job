#write a program to find the largest/greatest number

# same as problem 12 
#sorting in ascending order
list=[1,2,3,4,5,6,7,8]
list.sort()
print("largest element in the list is",list[-1])


#sorting in descending order
list=[1,2,7,8,4,6,0,5]
list.sort(reverse=True)#wht -1 is not fot here --must need to know
print("smallest number in the list is ",list[0])



#attempt 3
#using max() function with thr def
def  maxelement(list):
     return max(list)
list=[1,2,7,8,4,6,0,5]
i= maxelement(list)
print("max number of the list is ", i)