#Find the Minimum element in a Sorted and Rotated Array

#Difficulty Level : Medium
#--------------------------------------------------------------------------------
#Given a sorted array arr[] (may be distinct or may contain duplicates) of size N that is rotated at some unknown point, the task is to find the minimum element in it. 

#Examples: 

#Input: arr[] = {5, 6, 1, 2, 3, 4}
#Output: 1
#Explanation: 1 is the minimum element present in the array.

#Input: arr[] = {1, 2, 3, 4}
#Output: 1

#Input: arr[] = {2, 1}
#Output: 1
#Find the minimum element in a sorted and rotated array using Linear Search:
#A simple solution is to use linear search to traverse the complete array and find a minimum. 

#Follow the steps mentioned below to implement the idea:



#Declare a variable (say min_ele) to store the minimum value and initialize it with arr[0].
#Traverse the array from the start.
#Update the minimum value (min_ele) if the current element is less than it.
#Return the final value of min_ele as the required answer.
#Below is the implementation of the above approach.

# python3 code  to implement the approach
 
def findMin(arr, N):
     
    min_ele = arr[0];
 
    # Traversing over array to
    # find minimum element
    for i in range(N) :
        if arr[i] < min_ele :
            min_ele = arr[i]
 
    return min_ele;
 
# Driver program
arr = [5, 6, 1, 2, 3, 4]
N = len(arr)
 
print(findMin(arr,N))
 
# This code is contributed by aditya942003patil
#Output
#1
#Time Complexity: O(N)
#Auxiliary Space: O(1)

#The Easy Way using STL:
#
#       The Approach:
#
#        The is verry simple here we have array/vector we use *min_element function in stl and print the minimum element in the vector/array.

#include <iostream>
#include<bits/stdc++.h>
#using namespace std;
 
int main() {
    vector<int>v{5, 6, 1, 2, 3, 4};
    cout<<"The Minimum Element in the vector is: ";
    cout<<*min_element(v.begin(),v.end())<<endl;
    return 0;
}
#Output
#The Minimum Element in the vector is: 1
#Time Complexity: O(N),in worst case.
#Auxiliary Space: O(1)

#Find the minimum element in a sorted and rotated array using Binary Search: 
#This approach is based on the following idea:

#As the array is sorted and rotated, there are two segments that are themselves sorted but their meeting point is the only position where the smallest element is and that is not sorted. 

#So we just need to find the position whose neighbours are greater than it and based on the extreme end values we can decide in which half we should search for that element.

#Follow the steps below to solve the given problem: 

#If we take a closer look at the above examples, we can easily figure out the following pattern:

#The minimum element is the only element whose previous is greater than it. If there is no previous element, then there is no rotation (the first element is minimum). 
#We check this condition for the middle element by comparing it with (mid-1)th and (mid+1)th elements.
#If the minimum element is not at the middle (neither mid nor mid + 1), then: 
#If the middle element is smaller than the last element, then the minimum element lies in the left half
#Else minimum element lies in the right half.
#Follow the below illustration for a better understanding

#Illustration:

#Let the array be arr[]={15, 18, 2, 3, 6, 12}
#low = 0 , high = 5.
#            =>  mid = 2
#            =>  arr[mid]=2 , arr[mid-1] > arr[mid] , hence condition is matched
#            =>  The required index = mid = 2

#So the element is  found at index 2 and arr[2] = 2

#Below is the code implementation of the above approach:

# Python program to find minimum element
# in a sorted and rotated array
 
 
def findMin(arr, low, high):
    # This condition is needed to handle the case when array is not
    # rotated at all
    if high < low:
        return arr[0]
 
    # If there is only one element left
    if high == low:
        return arr[low]
 
    # Find mid
    mid = int((low + high)/2)
 
    # Check if element (mid+1) is minimum element. Consider
    # the cases like [3, 4, 5, 1, 2]
    if mid < high and arr[mid+1] < arr[mid]:
        return arr[mid+1]
 
    # Check if mid itself is minimum element
    if mid > low and arr[mid] < arr[mid - 1]:
        return arr[mid]
 
    # Decide whether we need to go to left half or right half
    if arr[high] > arr[mid]:
        return findMin(arr, low, mid-1)
    return findMin(arr, mid+1, high)
 
 
# Driver program to test above functions
if __name__ == '__main__':
    arr = [5, 6, 1, 2, 3, 4]
    N = len(arr)
    print("The minimum element is " + \
          str(findMin(arr, 0, N-1)))
 
# This code is contributed by Pratik Chhajer
#Output
#The minimum element is 1
#Time Complexity: O(logN), using binary search 
#Auxiliary Space: O(1)
#--------------------------------------------------------------------


