#Sort an array of 0s, 1s and 2s | Dutch National Flag problem

#Difficulty Level : Medium
#Given an array A[] consisting of only 0s, 1s, and 2s. The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last.

#This problem is also the same as the famous “Dutch National Flag problem”. The problem was proposed by Edsger Dijkstra. The problem is as follows:

#Given N balls of colour red, white or blue arranged in a line in random order. You have to arrange all the balls such that the balls with the same colours are adjacent with the order of the balls, with the order of the colours being red, white and blue (i.e., all red coloured balls come first then the white coloured balls and then the blue coloured balls). 

#Examples:


#Input: {0, 1, 2, 0, 1, 2}
#Output: {0, 0, 1, 1, 2, 2}

#Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
#Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}
#--------------------------------------------------------------
#Sort an array of 0s, 1s, and 2s using the Pointer Approach: 
#This approach is based on the following idea:

#The problem is similar to “Segregate 0s and 1s in an array”.
#The problem was posed with three colors, here `0′, `1′ and `2′. The array is divided into four sections: 
#arr[1] to arr[low – 1]
#arr[low] to arr[mid – 1]
#arr[mid] to arr[high – 1]
#arr[high] to arr[n]
#If the ith element is 0 then swap the element to the low range.
#Similarly, if the element is 1 then keep it as it is.
#If the element is 2 then swap it with an element in high range.
#Illustration:

#arr[] = {0, 1, 2, 0, 1, 2}

#lo = 0, mid = 0, hi = 5


 

#Step – 1: arr[mid] == 0

#swap(arr[lo], arr[mid])
#lo = lo + 1 = 1
#mid = mid + 1 = 1
#arr[] = {0, 1, 2, 0, 1, 2}

 

#Step – 2: arr[mid] == 1


#mid = mid + 1 = 2
#arr[] = {0, 1, 2, 0, 1, 2}

 

#Step – 3: arr[mid] == 2

#swap(arr[mid], arr[hi])
#hi = hi – 1 = 4
#arr[] = {0, 1, 2, 0, 1, 2}

 

#Step – 4: arr[mid] == 2

#swap(arr[mid], arr[hi])
#hi = hi – 1 = 3
#arr[] = {0, 1, 1, 0, 2, 2}

 

#Step – 5: arr[mid] == 1

#mid = mid + 1 = 3
#arr[] = {0, 1, 1, 0, 2, 2}

 

#Step – 6: arr[mid] == 0

#swap(arr[lo], arr[mid])
#lo = lo + 1 = 2
#mid = mid + 1 = 4
#arr[] = {0, 0, 1, 1, 2, 2}

 

#Hence, arr[] = {0, 0, 1, 1, 2, 2}

#Follow the steps below to solve the given problem:

#Keep three indices low = 1, mid = 1, and high = N and there are four ranges, 1 to low (the range containing 0), low to mid (the range containing 1), mid to high (the range containing unknown elements) and high to N (the range containing 2).
#Traverse the array from start to end and mid is less than high. (Loop counter is i)
#If the element is 0 then swap the element with the element at index low and update low = low + 1 and mid = mid + 1
#If the element is 1 then update mid = mid + 1
#If the element is 2 then swap the element with the element at index high and update high = high – 1 and update i = i – 1. As the swapped element is not processed
#Print the array.
 
#Complete Interview Preparation - GFG 

# Python program to sort an array with
# 0, 1 and 2 in a single pass
 
# Function to sort array
 
 
def sort012(a, arr_size):
    lo = 0
    hi = arr_size - 1
    mid = 0
    # Iterate till all the elements
    # are sorted
    while mid <= hi:
        # If the element is 0
        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]
            lo = lo + 1
            mid = mid + 1
        # If the element is 1
        elif a[mid] == 1:
            mid = mid + 1
        # If the element is 2
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi = hi - 1
    return a
 
# Function to print array
 
 
def printArray(a):
    for k in a:
        print(k, end=' ')
 
 
# Driver Program
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr_size = len(arr)
arr = sort012(arr, arr_size)
printArray(arr)
 
# Contributed by Harshit Agrawal
#Output
#0 0 0 0 0 1 1 1 1 1 2 2 
#Time Complexity: O(n), Only one traversal of the array is needed.
#Space Complexity: O(1), No extra space is required.
#----------------------------------------------------------------------
#Sort an array of 0s, 1s, and 2s using Counting Approach: 
#This approach is based on the following idea:

#Count the number of 0s, 1s, and 2s in the given array. Then store all the 0s at the beginning followed by all the 1s and then all the 2s.

#Illustration:

#arr[] = {0, 1, 2, 0, 1, 2}

#cnt0 = 0, cnt1 = 0, cnt2 = 0

#At i = 0: arr[0] == 0

#cnt0 = cnt0 + 1 = 1
#At i = 1: arr[1] == 1

#cnt1 = cnt1 + 1 = 1
#At i = 2: arr[2] == 2

#cnt2 = cnt2 + 1 = 1
#At i = 3: arr[3] == 0

#cnt0 = cnt0 + 1 = 2
#At i = 4: arr[4] == 1

#cnt1 = cnt1 + 1 = 2
#At i = 5: arr[5] == 2

#cnt2 = cnt2 + 1 = 2
#Replace cnt0 number of elements with 0 in arr

#arr[] = {0, 0, 2, 0, 1, 2}
#Replace cnt1 number of elements with 1 in arr

#arr[] = {0, 0, 1, 1, 1, 2}
#Replace cnt2 number of elements with 2 in arr

#arr[] = {0, 0, 1, 1, 2, 2}
#3Hence, arr[] = {0, 0, 1, 1, 2, 2}

#Follow the steps below to solve the given problem:  

#Keep three counters c0 to count 0s, c1 to count 1s, and c2 to count 2s
#Traverse through the array and increase the count of c0 if the element is 0, increase the count of c1 if the element is 1 and increase the count of c2 if the element is 2
#Now again traverse the array and replace the first c0 elements with 0, the next c1 elements with 1, and the next c2 elements with 2.
#Below is the implementation of the above idea : 

# Python implementation of the approach
 
# Utility function to print contents of an array
 
 
def printArr(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
 
 
# Function to sort the array of 0s, 1s and 2s
def sortArr(arr, n):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
 
    # Count the number of 0s, 1s and 2s in the array
    for i in range(n):
        if arr[i] == 0:
            cnt0 += 1
 
        elif arr[i] == 1:
            cnt1 += 1
 
        elif arr[i] == 2:
            cnt2 += 1
 
    # Update the array
    i = 0
 
    # Store all the 0s in the beginning
    while (cnt0 > 0):
        arr[i] = 0
        i += 1
        cnt0 -= 1
 
    # Then all the 1s
    while (cnt1 > 0):
        arr[i] = 1
        i += 1
        cnt1 -= 1
 
    # Finally all the 2s
while (cnt2 > 0):
        arr[i] = 2
        i += 1
        cnt2 -= 1
 
    # Print the sorted array
    printArr(arr, n)
 
 
# Driver code
 
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
n = len(arr)
 
sortArr(arr, n)
 
# This code is contributed by shubhamsingh10
#Output
#0 0 0 0 0 1 1 1 1 1 2 2 
#Time Complexity: O(n), Only nonnested traversals of the array are needed.

#Space Complexity: O(1)




























