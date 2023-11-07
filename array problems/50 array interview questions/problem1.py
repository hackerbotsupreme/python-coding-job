#Find a peak element which is not smaller than its neighbours
#Difficulty Level : Medium


#Given an array arr[] of integers. Find a peak element i.e. an element that is not smaller than its neighbors. 

#Note: For corner elements, we need to consider only one neighbor. 

#Example:

#Input: array[]= {5, 10, 20, 15}
#Output: 20
#Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20.

#Input: array[] = {10, 20, 15, 2, 23, 90, 67}
#Output: 20 or 90
#Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20, similarly 90 has neighbors 23 and 67.

#The following corner cases give a better idea about the problem. 

#If the input array is sorted in a strictly increasing order, the last element is always a peak element. For example, 50 is peak element in {10, 20, 30, 40, 50}.
##If the input array is sorted in a strictly decreasing order, the first element is always a peak element. 100 is the peak element in {100, 80, 60, 50, 20}.
#If all elements of the input array are the same, every element is a peak element.
#####################________________________________



#It is clear from the above examples that there is always a peak element in the input array.



#Recommended Problem
#Bitonic Point
#Arrays
#Searching
#+2 more
#Flipkart
#Amazon
#+1 more
#Solve Problem
#Submission count: 83.6K
#Naive Approach: Below is the idea to solve the problem

#The array can be traversed and the element whose neighbors are less than that element can be returned.

#Follow the below steps to Implement the idea: 

#If the first element is greater than the second or the last element is greater than the second last, print the respective element and terminate the program.
#Else traverse the array from the second index to the second last index i.e. 1 to N – 1  
#If for an element array[i] is greater than both its neighbors, i.e., array[i] > =array[i-1]  and array[i] > =array[i+1] , then print that element and terminate.
#Below is the implementation of above idea.

# A Python3 program to find a peak element


# A Python3 program to find a peak element
 
# Find the peak element in the array
def findPeak(arr, n) :
 
    # first or last element is peak element
    if (n == 1) :
      return 0
    if (arr[0] >= arr[1]) :
        return 0
    if (arr[n - 1] >= arr[n - 2]) :
        return n - 1
  
    # check for every other element
    for i in range(1, n - 1) :
  
        # check if the neighbors are smaller
        if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]) :
            return i
             
# Driver code.
arr = [ 1, 3, 20, 4, 1, 0 ]
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))
 
# This code is contributed by divyeshrabadiya07
#Output
#Index of a peak point is 2
#Time complexity: O(n), One traversal is needed so the time complexity is O(n)

#Auxiliary Space: O(1), No extra space is needed, so space complexity is constant

#--------------------------------------------------------------------

#Find a peak element using recursive Binary Search
#Below is the idea to solve the problem.

#Using Binary Search, check if the middle element is the peak element or not. If the middle element is not the peak element, then check if the element on the right side is greater than the middle element then there is always a peak element on the right side. If the element on the left side is greater than the middle element then there is always a peak element on the left side. 

#Complete Interview Preparation - GFG

#Follow the steps below to implement the idea:

#Create two variables, l and r, initialize l = 0 and r = n-1
#Recursively perform the below steps till l <= r, i.e. lowerbound is less than the upperbound
#Check if the mid value or index mid = low + (high - low) / 2,  is the peak element or not, if yes then print the element and terminate.
#Else if the element on the left side of the middle element is greater then check for peak element on the left side, i.e. update r = mid – 1
#Else if the element on the right side of the middle element is greater then check for peak element on the right side, i.e. update l = mid + 1
#Below is the implementation of the above approach

# A python3 program to find a peak
#  element using divide and conquer
 
# A binary search based function
# that returns index of a peak element
 
 
def findPeakUtil(arr, low, high, n):
 
    # Find index of middle element
    # low + (high - low) / 2
    mid = low + (high - low)/2
    mid = int(mid)
 
    # Compare middle element with its
    # neighbours (if neighbours exist)
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
        (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid
 
 
    # If middle element is not peak and
    # its left neighbour is greater
    # than it, then left half must
    # have a peak element
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakUtil(arr, low, (mid - 1), n)
 
    # If middle element is not peak and
    # its right neighbour is greater
    # than it, then right half must
    # have a peak element
    else:
        return findPeakUtil(arr, (mid + 1), high, n)
 
 
# A wrapper over recursive
# function findPeakUtil()
def findPeak(arr, n):
 
    return findPeakUtil(arr, 0, n - 1, n)
 
 
# Driver code
arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))
     
# This code is contributed by
# Smitha Dinesh Semwal
#Output
#Index of a peak point is 2
#Time Complexity: O(log N), Where N is the number of elements in the input array. 
#Auxiliary Space: O(log N), As recursive call is there, hence implicit stack is used.



#-------------------------------------------------------------------------


Find a peak element using iterative Binary search
Below is the idea to solve the problem.

Using Binary Search, check if the middle element is the peak element or not. If the middle element the peak element terminate the while loop and print middle element, then check if the element on the right side is greater than the middle element then there is always a peak element on the right side. If the element on the left side is greater than the middle element then there is always a peak element on the left side. 

Follow the steps below to implement the idea:

Create two variables, l and r, initialize l = 0 and r = n-1
Run a while loop till l <= r, lowerbound is less than the upperbound
Check if the mid value or index mid = low + (high - low) / 2,  is the peak element or not, if yes then print the element and terminate.
Else if the element on the left side of the middle element is greater then check for peak element on the left side, i.e. update r = mid – 1
Else if the element on the right side of the middle element is greater then check for peak element on the right side, i.e. update l = mid + 1
The below-given code is the iterative version of the above explained and demonstrated recursive based divide and conquer technique.

# A Python program to find a peak element
# using divide and conquer
 
# A binary search based function
# that returns index of a peak element
def findPeak(arr, n):
   
    l = 0
    r = n-1
     
    while(l <= r):
 
        # finding mid by binary right shifting.
        mid = (l + r) >> 1
 
        # first case if mid is the answer
        if((mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid])):
            break
 
        # move the right pointer
        if(mid > 0 and arr[mid - 1] > arr[mid]):
            r = mid - 1
 
        # move the left pointer
        else:
            l = mid + 1
 
    return mid
 
 
# Driver Code
arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
print(f"Index of a peak point is {findPeak(arr, n)}")
 
# This code is contributed by Rajdeep Mallick (rajdeep999)
#Output
#Index of a peak point is 2
#Time Complexity: O(log N), Where n is the number of elements in the input array. In each step our search becomes half. So it can be compared to Binary search, So the time complexity is O(log N)
#Auxiliary Space: O(1), No extra space is required, so the space complexity is constant.

#-------------------------------------------
#Exercise: 
#Consider the following modified definition of peak element. An array element is a peak if it is greater than its neighbors. Note that an array may not contain a peak element with this modified definition.

#References: 
#http://courses.csail.mit.edu/6.006/spring11/lectures/lec02.pdf 
#http://www.youtube.com/watch?v=HtSuA80QTyo
 

#Asked in: Amazon
#Related Problem: 
#Find local minima in an array































































