#Move all negative numbers to beginning and positive to end with constant extra space

#Difficulty Level : Easy
#--------------------------------------------------------------------
#An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.

#Examples : 

#Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
#Output: -12 -13 -5 -7 -3 -6 11 6 5

#Note: Order of elements is not important here.
#-------------------------------------------------------
#Naive approach: The idea is to sort the array of elements, this will make sure that all the negative elements will come before all the positive elements.
#Below is the implementation of the above approach:

# Python code for the same approach
def move(arr):
  arr.sort()
 
# driver code
arr = [ -1, 2, -3, 4, 5, 6, -7, 8, 9 ]
move(arr)
for e in arr:
    print(e , end = " ")
 
# This code is contributed by shinjanpatra
#Output
#-7 -3 -1 2 4 5 6 8 9 
#Time Complexity: O(n*log(n)), Where n is the length of the given array.
#Auxiliary Space: O(n)
#-------------------------------------------------------
#Efficient Approach 1:
#The idea is to simply apply the partition process of quicksort. 

# A Python 3 program to put
# all negative numbers before
# positive numbers
 
def rearrange(arr, n ) :
 
    # Please refer partition() in
    # below post
    # https://www.geeksforgeeks.org / quick-sort / j = 0
    j = 0
    for i in range(0, n) :
        if (arr[i] < 0) :
            temp = arr[i]
            arr[i] = arr[j]
            arr[j]= temp
            j = j + 1
    print(arr)
 
# Driver code
arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
rearrange(arr, n)
 
 
# This code is contributed by Nikita Tiwari.
#Output
#-1 -3 -7 4 5 6 2 8 9 
#Time complexity: O(N) 
#Auxiliary Space: O(1)

#------------------------------------------------------------------
Two Pointer Approach: The idea is to solve this problem with constant space and linear time is by using a two-pointer or two-variable approach where we simply take two variables like left and right which hold the 0 and N-1 indexes. Just need to check that :

Check If the left and right pointer elements are negative then simply increment the left pointer.
Otherwise, if the left element is positive and the right element is negative then simply swap the elements, and simultaneously increment and decrement the left and right pointers.
Else if the left element is positive and the right element is also positive then simply decrement the right pointer.
Repeat the above 3 steps until the left pointer ≤ right pointer.
Below is the implementation of the above approach:

# Python3 program of the
# above approach
 
# Function to shift all the
# the negative elements to
# the left of the array
def shiftall(arr,left,right):
   
  # Loop to iterate while the
  # left pointer is less than
  # the right pointer
  while left<=right:
     
    # Condition to check if the left
    # and right pointer negative
    if arr[left] < 0 and arr[right] < 0:
      left+=1
       
    # Condition to check if the left
    # pointer element is positive and
    # the right pointer element is
    # negative
    else if arr[left]>0 and arr[right]<0:
      arr[left], arr[right] = \
              arr[right],arr[left]
      left+=1
      right-=1
       
    # Condition to check if the left
    # pointer is positive and right
    # pointer as well
    else if arr[left]>0 and arr[right]>0:
      right-=1
    else:
      left+=1
      right-=1
       
# Function to print the array
def display(arr):
  for i in range(len(arr)):
    print(arr[i], end=" ")
  print()
 
# Driver Code
if __name__ == "__main__":
  arr=[-12, 11, -13, -5, \
       6, -7, 5, -3, 11]
  n=len(arr)
  shiftall(arr,0,n-1)
  display(arr)
 
# Sumit Singh
#Output
#-12 -3 -13 -5 -7 6 5 11 11 
#This is an in-place rearranging algorithm for arranging the positive and negative numbers where the order of elements is not maintained.
#Time Complexity: O(N)
#Auxiliary Space: O(1)
#-------------------------------------------------------------------
#The problem becomes difficult if we need to maintain the order of elements. Please refer to Rearrange positive and negative numbers with constant extra space for details.

#This article is contributed by Apoorva. If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeek’s main page and help other Geeks.

#Approach 3:
#Here, we will use the famous Dutch National Flag Algorithm for two “colors”. The first color will be for all negative integers and the second color will be for all positive integers. We will divide the array into three partitions with the help of two pointers, low and high. 

#ar[1…low-1] negative integers
ar[low…high] unknown
ar[high+1…N] positive integers
Now, we explore the array with the help of low pointer, shrinking the unknown partition, and moving elements to their correct partition in the process. We do this until we have explored all the elements, and size of the unknown partition shrinks to zero.

Below is the implementation of the above approach:

# Python code for the approach
 
# Using Dutch National Flag Algorithm.
def reArrange(arr, n):
    low,high = 0, n - 1
    while(low<high):
        if(arr[low] < 0):
            low += 1
        elif(arr[high] > 0):
            high -= 1
        else:
            arr[low],arr[high] = arr[high],arr[low]
 
def displayArray(arr, n):
 
    for i in range(n):
        print(arr[i],end = " ")
   
    print('')
 
# driver code
# Data
arr = [1, 2,  -4, -5, 2, -7, 3, 2, -6, -8, -9, 3, 2,  1]
n = len(arr)
reArrange(arr,n)
displayArray(arr,n)
 
# This code is contributed by shinjanpatra
Output
-9 -8 -4 -5 -6 -7 3 2 2 2 1 3 2 1 
Time complexity: O(N) 
Auxiliary Space: O(1)