#Find the smallest positive number missing from an unsorted array | Set 1

#Difficulty Level : Hard
#-----------------------------------------------------------------------
#Given an unsorted array arr[] with both positive and negative elements, the task is to find the smallest positive number missing from the array.

#Note: You can modify the original array.

#Examples:

#Input:  arr[] = {2, 3, 7, 6, 8, -1, -10, 15}
#Output: 1


#Input:  arr[] = { 2, 3, -7, 6, 8, 1, -10, 15 }
#Output: 4

#Input: arr[] = {1, 1, 0, -1, -2}
#Output: 2
#-------------------------------------------------------------------------
#Naive Approach:



#A naive method to solve this problem is to search all positive integers, starting from 1 in the given array. 

#Time Complexity: O(N2) because we may have to search at most n+1 numbers in the given array.
#Auxiliary Space: O(1)

#Smallest positive number missing from an unsorted array by Marking Elements:
#The idea is to mark the elements which are present in the array then traverse over the marked array and return the first element which is not marked.

#Follow the steps below to solve the problem:

#Create a list full of 0’s with the size of the max value of the given array. 
#Now, whenever we encounter any positive value in the original array, change the index value of the list to 1. 
#After that simply iterate through the modified list, the first 0 encountered, (index value + 1) should be the answer.
#Below is the implementation of the above approach.

# Python3 Program to find the smallest
# positive missing number
 
 
def solution(A):  # Our original array
 
    m = max(A)  # Storing maximum value
    if m < 1:
 
        # In case all values in our array are negative
        return 1
    if len(A) == 1:
 
        # If it contains only one element
        return 2 if A[0] == 1 else 1
    l = [0] * m
    for i in range(len(A)):
        if A[i] > 0:
            if l[A[i] - 1] != 1:
 
                # Changing the value status at the index of our list
                l[A[i] - 1] = 1
    for i in range(len(l)):
 
        # Encountering first 0, i.e, the element with least value
        if l[i] == 0:
            return i + 1
            # In case all values are filled between 1 and m
    return i + 2
 
 
# Driver Code
if __name__ == '__main__':
    arr = [0, 10, 2, -10, -20]
    print(solution(arr))
#Output
#1
#Time Complexity: O(N), Only two traversals are needed.
#Auxiliary Space: O(N), using the list will require extra space
#-----------------------------------------------------------------------
#Smallest positive number missing from an unsorted Array by using array elements as Index:
#The idea is to use array elements as an index. To mark the presence of an element x, change the value at the index x to negative. But this approach doesn’t work if there are non-positive (-ve and 0) numbers. 

#So segregate positive from negative numbers as the first step and then apply the approach.

#Follow the steps below to solve the problem:

#Segregate positive numbers from others i.e., move all non-positive numbers to the left side.
#Now ignore non-positive elements and consider only the part of the array which contains all positive elements. 
#Traverse the array containing all positive numbers and to mark the presence of an element x, change the sign of value at index x to negative. 
#Traverse the array again and print the first index which has a positive value. 
#Below is the implementation of the above approach.

#v

#Output
#1
#Time Complexity: O(N), Traversing the array of size N.
#Auxiliary Space: O(1)

#Smallest positive number missing from an unsorted array by changing the input Array
#The idea is to mark the elements in the array which are greater than N and less than 1 with 1.

#Follow the steps below to solve the problem:

#The smallest positive integer is 1. First, we will check if 1 is present in the array or not. If it is not present then 1 is the answer.
#If present then, again traverse the array. The largest possible answer is N+1 where N is the size of the array. 
#When traversing the array, if we find any number less than 1 or greater than N, change it to 1. 
#This will not change anything as the answer will always be between 1 to N+1. Now our array has elements from 1 to N.
#Now, for every ith number, increase arr[ (arr[i]-1) ] by N. But this will increase the value more than N. So, we will access the array by arr[(arr[i]-1)%N].
#We will find now which index has a value less than N+1. Then i+1 will be our answer. 
#Below is the implementation of the above approach.

# Python3 program for the above approach
 
# Function for finding the first missing
# positive number
def firstMissingPositive(arr, n):
 
    ptr = 0
 
    # Check if 1 is present in array or not
    for i in range(n):
        if arr[i] == 1:
            ptr = 1
            break
 
    # If 1 is not present
    if ptr == 0:
        return(1)
 
    # Changing values to 1
    for i in range(n):
        if arr[i] <= 0 or arr[i] > n:
            arr[i] = 1
 
    # Updating indices according to values
    for i in range(n):
        arr[(arr[i] - 1) % n] += n
 
    # Finding which index has value less than n
    for i in range(n):
        if arr[i] <= n:
            return(i + 1)
 
    # If array has values from 1 to n
    return(n + 1)
 
# Driver Code
if __name__ == '__main__':
    # Given array
    A = [0, 10, 2, -10, -20]
     
    # Size of the array
    N = len(A)
     
    # Function call
    print(firstMissingPositive(A, N))
 
# This code is contributed by shailjapriya
#Output
#1
#Time Complexity: O(N), Traversing over the array
#Auxiliary Space:  O(1) 

#Smallest positive number missing from an unsorted array by Swapping:
#The idea is to swap the elements which are in the range 1 to N should be placed at their respective indexes.

#Follow the steps below to solve the problem:

#Traverse the array, Ignore the elements which are greater than N and less than 1.
#While traversing, check if a[i] ≠ a[a[i]-1] holds true or not .
#If the above condition is true then swap a[i] and a[a[i] – 1]  and swap until (a[i] ≠ a[a[i] – 1]) condition fails.
#Traverse the array and check whether a[i] ≠ i + 1 then return i + 1.
#If all are equal to its index then return N+1.
#Below is the implementation of the above approach.

# Python program for the above approach
 
 
# Function for finding the first
# missing positive number
def firstMissingPositive(arr, n):
 
    # Loop to traverse the whole array
    for i in range(n):
 
        # Loop to check boundary
        # condition and for swapping
        while (arr[i] >= 1 and arr[i] <= n
               and arr[i] != arr[arr[i] - 1]):
            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[temp - 1] = temp
 
    # Checking any element which
    # is not equal to i + 1
    for i in range(n):
        if (arr[i] != i + 1):
            return i + 1
 
    # Nothing is present return last index
    return n + 1
 
 
# Driver code
if __name__ == '__main__':
    arr = [0, 10, 2, -10, -20]
    n = len(arr)
    ans = firstMissingPositive(arr, n)
    print(ans)
 
# This code is contributed by shivanisinghss2110
#Output
#1
#Time Complexity: O(N), Only two traversals are needed.
#Auxiliary Space: O(1), No extra space is needed
#------------------------------------------------------------------
#Smallest positive number missing from an unsorted array using Sorting:
#The idea is to sort the array and then check for the smallest missing number (start from 1) if it is present then increment it.

#Follow the steps below to solve the problem:

#First sort the array and the smallest positive integer is 1.
#So, take ans=1 and iterate over the array once and check whether arr[i] = ans (Checking for value from 1 up to the missing number).
#By iterating if that condition meets where arr[i] = ans then increment ans by 1 and again check for the same condition until the size of the array.
#After one scan of the array, the missing number is stored in ans variable.
#Now return that ans to the function.
#Below is the implementation of the above approach:

# Python code for the same approach
from functools import cmp_to_key
 
 
def cmp(a, b):
    return (a - b)
 
 
def firstMissingPositive(nums):
 
    nums.sort(key = cmp_to_key(cmp))
    ans = 1
    for i in range(len(nums)):
 
        if(nums[i] == ans):
            ans += 1
 
    return ans
 
 
# driver code
if __name__ == '__main__':
    arr = [0, 10, 2, -10, -20]
    print(firstMissingPositive(arr))
 
# This code is contributed by shinjanpatra
#Output
#1
#Time Complexity: O(N*log(N)), Time required to sort the array
#Auxiliary Space: O(1) 