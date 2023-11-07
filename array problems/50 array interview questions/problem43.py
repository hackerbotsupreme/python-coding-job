#Maximum Sum Path in Two Arrays

#Difficulty Level : Medium
#---------------------------------------------------------------------
#Given two sorted arrays, the arrays may have some common elements. Find the sum of the maximum sum path to reach from the beginning of any array to the end of any of the two arrays. We can switch from one array to another array only at common elements. 

#Note: The common elements do not have to be at the same indexes.

#Examples: 

#Input: ar1[] = {2, 3, 7, 10, 12}, ar2[] = {1, 5, 7, 8}
#Output: 35
#Explanation: 35 is sum of 1 + 5 + 7 + 10 + 12.
#Start from the first element of ar2 which is 1, then move to 5, then 7.  From 7 switch to ar1 (as 7 is common) and traverse 10 and 12.


#Input: ar1[] = {10, 12}, ar2 = {5, 7, 9}
#Output: 22
#Explanation: 22 is the sum of 10 and 12. 
#Since there is no common element, take all elements from the array with more sum.

#Input: ar1[] = {2, 3, 7, 10, 12, 15, 30, 34}, ar2[] = {1, 5, 7, 8, 10, 15, 16, 19}
#Output: 122
#Explanation: 122 is sum of 1, 5, 7, 8, 10, 12, 15, 30, 34
#Start from the first element of ar2 which is 1, then move to 5, then 7. From 7 switch to ar1 (as 7 is common), then traverse the remaining ar1.
#---------------------------------------------------------------------

#Maximum Sum Path in Two Arrays using Merge: This approach is based on the following idea:



#The idea is to do something similar to the merge process of merge sort. This involves calculating the sum of elements between all common points of both arrays. Whenever there is a common point, compare the two sums and add the maximum of two to the result.

#Illustration:

#Input: arr1[] = {2, 3, 7, 10, 12}

#           arr2[] = {1, 5, 7, 8}

#          Initialise i = 0, j = 0, sum1 = 0, sum2 = 0, result = 0


 

#Step – 1: arr1[i] > arr2[j] 
#sum2 = sum2 + arr2[j] = 0 + 1 = 1
#j = j + 1 = 1


 

#Step – 2: arr1[i] < arr2[j] 
#sum1 = sum1 + arr1[i] = 0 + 2 = 2
#i = i + 1 = 1


 

#Step – 3: arr1[i] < arr2[j] 
#sum1 = sum1 + arr1[i] = 2 + 3 = 5
#i = i + 1 = 2


 

#Step – 4: arr1[i] > arr2[j] 
#sum2 = sum2 + arr2[j] = 1 + 5 = 6
#j = j + 1 = 2


 

#Step – 5: arr1[i] == arr2[j] 
#result = result + maximum(sum1, sum2) + arr1[i] = 0 + max(5, 6) + 7 = 13
#sum1 = 0, sum2 = 0
#i = i + 1 = 3
#j = j + 1 = 3


 

#Step – 6: arr1[i] > arr2[j] 
#sum2 = sum2 + arr2[j] = 0 + 8 = 8
#j = j + 1 = 4


 

#Step – 7: sum1 = sum1 + arr1[i] = 0 + 10 = 10
#i = i + 1 = 4


 

#Step – 8: sum1 = sum1 + arr1[i] = 10 + 12 = 22
#i = i + 1 = 5


 

#Step – 9: result = result + max(sum1, sum2) = 13 + max(10, 22) = 35 


 

#Hence, maximum sum path is 35.

#Follow the steps below to solve the given problem:

#Initialize variables, result, sum1, sum2. Initialize result as 0. Also initialize two variables sum1 and sum2 as 0. Here sum1 and sum2 are used to store sum of element in ar1[] and ar2[] respectively. These sums are between two common points.
#Now run a loop to traverse elements of both arrays. While traversing compare current elements of array 1 and array 2 in the following order.
#If current element of array 1 is smaller than current element of array 2, then update sum1, else if current element of array 2 is smaller, then update sum2.
#If the current element of array 1 and array 2are same, then take the maximum of sum1 and sum2 and add it to the result. Also add the common element to the result.
#This step can be compared to the merging of two sorted arrays, If the smallest element of the two current array indices is processed then it is guaranteed that if there is any common element it will be processed together. So the sum of elements between two common elements can be processed.
#Below is the implementation of the above code: 


# Python program to find maximum sum path
  
# This function returns the sum of elements on maximum path from
# beginning to end
  
  
def maxPathSum(ar1, ar2, m, n):
  
    # initialize indexes for ar1[] and ar2[]
    i, j = 0, 0
  
    # Initialize result and current sum through ar1[] and ar2[]
    result, sum1, sum2 = 0, 0, 0
  
    # Below 3 loops are similar to merge in merge sort
    while (i < m and j < n):
  
        # Add elements of ar1[] to sum1
        if ar1[i] < ar2[j]:
            sum1 += ar1[i]
            i += 1
  
        # Add elements of ar2[] to sum2
        elif ar1[i] > ar2[j]:
            sum2 += ar2[j]
            j += 1
  
        else:   # we reached a common point
  
            # Take the maximum of two sums and add to result
            result += max(sum1, sum2) + ar1[i]
            # update sum1 and sum2 to be considered fresh for next elements
            sum1 = 0
            sum2 = 0
            # update i and j to move to next element in each array
            i += 1
            j += 1
  
    # Add remaining elements of ar1[]
    while i < m:
        sum1 += ar1[i]
        i += 1
    # Add remaining elements of b[]
    while j < n:
        sum2 += ar2[j]
        j += 1
  
    # Add maximum of two sums of remaining elements
    result += max(sum1, sum2)
  
    return result
  
  
# Driver code
ar1 = [2, 3, 7, 10, 12, 15, 30, 34]
ar2 = [1, 5, 7, 8, 10, 15, 16, 19]
m = len(ar1)
n = len(ar2)
  
# Function call
print("Maximum sum path is", maxPathSum(ar1, ar2, m, n))
  
# This code is contributed by __Devesh Agrawal__
###########################3Output
#Maximum sum path is 122
#-----------------------------------------------------------
