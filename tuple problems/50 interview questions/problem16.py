#Python heapq to find K’th smallest element in a 2D array

#Difficulty Level : Basic
#Last Updated : 28 Jul, 2022
#Read
#Discuss
#Courses
#Practice
##Video
#Given an n x n matrix and integer k. Find the k’th smallest element in the given 2D array. Examples:

#Input : mat = [[10, 25, 20, 40],
#               [15, 45, 35, 30],
#               [24, 29, 37, 48],
#               [32, 33, 39, 50]]
#        k =  7 
#Output : 7th smallest element is 30
#We will use similar approach like K’th Smallest/Largest Element in Unsorted Array to solve this problem.

#Create an empty min heap using heapq in python.
#Now assign first row (list) in result variable and convert result list into min heap using heapify method.
#Now traverse remaining row elements and push them into created min heap.
#Now get k’th smallest element using nsmallest(k, iterable) method of heapq module.
#Implementation:

#Python3
# Function to find K'th smallest element in
# a 2D array in Python
import heapq
 
def kthSmallest(input):
 
    # assign first row to result variable
    # and convert it into min heap
    result = input[0]
    heapq.heapify(result)
 
    # now traverse remaining rows and push
    # elements in min heap
    for row in input[1:]:
        for ele in row:
            heapq.heappush(result,ele)
 
    # get list of first k smallest element because
    # nsmallest(k,list) method returns first k
    # smallest element now print last element of
    # that list
    kSmallest = heapq.nsmallest(k,result)
    print (k,"th smallest element is ",kSmallest[-1])
 
# Driver program
if __name__ == "__main__":
    input = [[10, 25, 20, 40],
        [15, 45, 35, 30],
        [24, 29, 37, 48],
        [32, 33, 39, 50]]
    k = 7
    kthSmallest(input)
#Output
#7 th smallest element is  30