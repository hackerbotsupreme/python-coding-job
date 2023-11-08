#pyhon program rofind smallest number in the list 


#concept:the keylessons of this question is how sort function works 

#first thingg is first is there any inbuilt function that can make our life easy
#well, yes there is  four methods.1. sort in ascending ordeer
#sort in descending  order
#3.usinf min() function
#$.using max() function 


#ok so
#attempt 1
#sort in ascending option:low to high
list=[1,2,7,8,4,6,0,5]
list.sort()
print("smallest number in the list is ",list[0])

#and similarly
#attempt 2
#sorting in decending order :high to low
list=[1,2,7,8,4,6,0,5]
list.sort(reverse=True)#wht -1 is not fot here --must need to know
print("smallest number in the list is ",list[-1])

#attempt 4
#using min() function  with the def
def  minelement(list):
     return min(list)
list=[1,2,7,8,4,6,0,5]
i= minelement(list)
print("minimum number of the list is ", i)

#attempt 5
#using max() function with thr def
def  maxelement(list):
     return max(list)
list=[1,2,7,8,4,6,0,5]
i= maxelement(list)
print("max number of the list is ", i)

#ok  others are being worth leess bcz if the methods nees
# to use min , max then what is in doing one more method


