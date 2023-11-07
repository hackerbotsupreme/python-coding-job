#pythonprogram to find missing and additional values of two lists 
#what can be the possible for this problem this smells like it wants difference btween two sets

#attempt 1
#we are gonna use difference function of the sets 
#set1/list1.differencelist2/set2
#this problem is great to learn the the working of difference in set 
list=[1,2,3,4,5,6]
list=[4,5,6,7,8]
print("missing values in the second list :",(set(list(1).difference(list(2)))))
print("additional value in the second list :",(set(list(2)).difference(list(1))))




# Python program to find the missing
# and additional elements

# examples of lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

# prints the missing and additional elements in list2
print("Missing values in second list:", (set(list1).difference(list2)))
print("Additional values in second list:", (set(list2).difference(list1)))

# prints the missing and additional elements in list1
print("Missing values in first list:", (set(list2).difference(list1)))
print("Additional values in first list:", (set(list1).difference(list2)))
