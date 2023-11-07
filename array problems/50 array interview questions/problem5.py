#Count number of occurrences (or frequency) in a sorted array

#Difficulty Level : Medium
 
#Given a sorted array arr[] and a number x, write a function that counts the occurrences of x in arr[]. Expected time complexity is O(Logn) 

#Examples: 

#  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 2
#  Output: 4 // x (or 2) occurs 4 times in arr[]

#  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 3
#  Output: 1 

#  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 1
#  Output: 2 

#  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 4
#  Output: -1 // 4 doesn't occur in arr[] 
#---------------------------------------------------------------------
#Method 1 (Linear Search) 
#Linearly search for x, count the occurrences of x and return the count. 
# Python3 program to count
# occurrences of an element
 
# Returns number of times x
# occurs in arr[0..n-1]
def countOccurrences(arr, n, x):
    res = 0
    for i in range(n):
        if x == arr[i]:
            res += 1
    return res
  
# Driver code
arr = [1, 2, 2, 2, 2, 3, 4, 7 ,8 ,8]
n = len(arr)
x = 2
print (countOccurrences(arr, n, x))
#Output : 


#4
#Time Complexity: O(n)

#Space Complexity: O(1), as no extra space is used
#------------------------------------------------------------------------------------
Method 2 (Better using Binary Search) 
We first find an occurrence using binary search. Then we match toward left and right sides of the matched the found index.

# Python 3 program to count
# occurrences of an element
 
# A recursive binary search
# function. It returns location
# of x in given array arr[l..r]
# is present, otherwise -1
def binarySearch(arr, l, r, x):
    if (r < l):
        return -1
 
    mid = int( l + (r - l) / 2)
 
    # If the element is present
    # at the middle itself
    if arr[mid] == x:
        return mid
 
    # If element is smaller than
    # mid, then it can only be
    # present in left subarray
    if arr[mid] > x:
        return binarySearch(arr, l,
                            mid - 1, x)
 
    # Else the element
    # can only be present
    # in right subarray
    return binarySearch(arr, mid + 1,
                                r, x)
 
# Returns number of times
# x occurs in arr[0..n-1]
def countOccurrences(arr, n, x):
    ind = binarySearch(arr, 0, n - 1, x)
 
    # If element is not present
    if ind == -1:
        return 0
 
    # Count elements
    # on left side.
    count = 1
    left = ind - 1
    while (left >= 0 and
           arr[left] == x):
        count += 1
        left -= 1
 
    # Count elements on
    # right side.
    right = ind + 1;
    while (right < n and
           arr[right] == x):
        count += 1
        right += 1
 
    return count
 
# Driver code
arr = [ 1, 2, 2, 2, 2,
        3, 4, 7, 8, 8 ]
n = len(arr)
x = 2
print(countOccurrences(arr, n, x))
 
# This code is contributed
# by ChitraNayal
#Output : 



#4
#Time Complexity : O(Log n + count) where count is number of occurrences.

#Space Complexity: O(logn), due to recursive stack space
#--------------------------------------------------------------------

#Complete Interview Preparation - GFG
#Method 3 (Best using Improved Binary Search) 
#1) Use Binary search to get index of the first occurrence of x in arr[]. Let the index of the first occurrence be i. 
#2) Use Binary search to get index of the last occurrence of x in arr[]. Let the index of the last occurrence be j. 
#3) Return (j – i + 1);

# Python3 program to count
# occurrences of an element
 
# if x is present in arr[] then
# returns the count of occurrences
# of x, otherwise returns -1.
def count(arr, x, n):
 
    # get the index of first
    # occurrence of x
    i = first(arr, 0, n-1, x, n)
  
    # If x doesn't exist in
    # arr[] then return -1
    if i == -1:
        return i
     
    # Else get the index of last occurrence
    # of x. Note that we are only looking
    # in the subarray after first occurrence  
    j = last(arr, i, n-1, x, n);    
     
    # return count
    return j-i+1;
 
# if x is present in arr[] then return
# the index of FIRST occurrence of x in
# arr[0..n-1], otherwise returns -1
def first(arr, low, high, x, n):
    if high >= low:
 
        # low + (high - low)/2
        mid = (low + high)//2     
         
        if (mid == 0 or x > arr[mid-1]) and arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return first(arr, (mid + 1), high, x, n)
        else:
            return first(arr, low, (mid -1), x, n)
    return -1;
  
# if x is present in arr[] then return
# the index of LAST occurrence of x
# in arr[0..n-1], otherwise returns -1
def last(arr, low, high, x, n):
    if high >= low:
 
        # low + (high - low)/2
        mid = (low + high)//2;
  
        if(mid == n-1 or x < arr[mid+1]) and arr[mid] == x :
            return mid
        elif x < arr[mid]:
            return last(arr, low, (mid -1), x, n)
        else:
            return last(arr, (mid + 1), high, x, n)    
    return -1
 
# driver program to test above functions
arr = [1, 2, 2, 3, 3, 3, 3]
x = 3  # Element to be counted in arr[]
n = len(arr)
c = count(arr, x, n)
print ("%d occurs %d times "%(x, c))
#Output:  

#3 occurs 4 times
#Time Complexity: O(Logn) 

#Auxiliary Space: O(1), as no extra space is used
#Programming Paradigm: Divide & Conquer
#---------------------------------------------------------------------------



#Using Collections.frequency() method of java

# Python code to implement the approach
 
# Function to count occurrences
def countOccurrences(arr, x) :
 
    count = 0
    n = len(arr)
    for i in range(n) :
        if (arr[i] == x):
            count += 1
             
    return count
    
# Driver Code
if __name__ == "__main__":
         
    arr = [ 1, 2, 2, 2, 2, 3, 4, 7, 8, 8 ]
    x = 2
   
    # displaying the frequency of x in ArrayList
    print(x , "occurs"
                        , countOccurrences(arr, x)
                        , "times")
     
    # This code is contributed by sanjoy_62.
#Output:

#2 occurs 4 times
#Time Complexity: O(n)

#Auxiliary Space: O(1), as no extra space is used
#-----------------------------------------------------------------------------





























