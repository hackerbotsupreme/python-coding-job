#Longest alternating subsequence

#Difficulty Level : Medium
#------------------------------------------------------

#A sequence {X1, X2, .. Xn} is an alternating sequence if its elements satisfy one of the following relations : 

#  X1 < X2 > X3 < X4 > X5 < …. xn or 
#  X1 > X2 < X3 > X4 < X5 > …. xn

#Examples:

#Input: arr[] = {1, 5, 4}
#Output: 3
#Explanation: The whole arrays is of the form  x1 < x2 > x3 


#Input: arr[] = {10, 22, 9, 33, 49, 50, 31, 60}
#Output: 6
#Explanation: The subsequences {10, 22, 9, 33, 31, 60} or
#{10, 22, 9, 49, 31, 60} or {10, 22, 9, 50, 31, 60}
#are longest subsequence of length 6
#-----------------------------------------------------------
#Note: This problem is an extension of the longest increasing subsequence problem, but requires more thinking for finding optimal substructure property in this

#Longest alternating subsequence using dynamic programming:
#To solve the problem follow the below idea:



#We will solve this problem by dynamic Programming method, as it has optimal substructure and overlapping subproblems

#Follow the below steps to solve the problem:

#Let A is given an array of length N 
#We define a 2D array las[n][2] such that las[i][0] contains the longest alternating subsequence ending at index i and the last element is greater than its previous element 
#las[i][1] contains the longest alternating subsequence ending at index i and the last element is smaller than its previous element, then we have the following recurrence relation between them,  
#las[i][0] = Length of the longest alternating subsequence 
#                  ending at index i and last element is greater
#                  than its previous element

#las[i][1] = Length of the longest alternating subsequence 
#                  ending at index i and last element is smaller
#                  than its previous element

#Recursive Formulation:

#   las[i][0] = max (las[i][0], las[j][1] + 1); 
#                  for all j < i and A[j] < A[i] 

#   las[i][1] = max (las[i][1], las[j][0] + 1); 
#                 for all j < i and A[j] > A[i]

#The first recurrence relation is based on the fact that, If we are at position i and this element has to be bigger than its previous element then for this sequence (upto i) to be bigger we will try to choose an element j ( < i) such that A[j] < A[i] i.e. A[j] can become A[i]’s previous element and las[j][1] + 1 is bigger than las[i][0] then we will update las[i][0]. 
#Remember we have chosen las[j][1] + 1 not las[j][0] + 1 to satisfy the alternate property because in las[j][0] the last element is bigger than its previous one and A[i] is greater than A[j] which will break the alternating property if we update. So above fact derives the first recurrence relation, a similar argument can be made for the second recurrence relation also. 
#Below is the implementation of the above approach:


# Python3 program to find longest
# alternating subsequence in an array
 
# Function to return max of two numbers
 
 
def Max(a, b):
 
    if a > b:
        return a
    else:
        return b
 
# Function to return longest alternating
# subsequence length
 
 
def zzis(arr, n):
    """las[i][0] = Length of the longest
        alternating subsequence ending at
        index i and last element is greater
        than its previous element
    las[i][1] = Length of the longest
        alternating subsequence ending
        at index i and last element is
        smaller than its previous element"""
    las = [[0 for i in range(2)]
           for j in range(n)]
 
    # Initialize all values from 1
    for i in range(n):
        las[i][0], las[i][1] = 1, 1
 
    # Initialize result
    res = 1
 
    # Compute values in bottom up manner
    for i in range(1, n):
 
        # Consider all elements as
        # previous of arr[i]
        for j in range(0, i):
 
            # If arr[i] is greater, then
            # check with las[j][1]
            if (arr[j] < arr[i] and
                    las[i][0] < las[j][1] + 1):
                las[i][0] = las[j][1] + 1
 
            # If arr[i] is smaller, then
            # check with las[j][0]
            if(arr[j] > arr[i] and
               las[i][1] < las[j][0] + 1):
                las[i][1] = las[j][0] + 1
 
        # Pick maximum of both values at index i
        if (res < max(las[i][0], las[i][1])):
            res = max(las[i][0], las[i][1])
 
    return res
 
 
# Driver Code
arr = [10, 22, 9, 33, 49, 50, 31, 60]
n = len(arr)
 
print("Length of Longest alternating subsequence is",
      zzis(arr, n))
 
# This code is contributed by divyesh072019
#Output
#Length of Longest alternating subsequence is 6
#Time Complexity: O(N2) 
#Auxiliary Space: O(N), since N extra space has been taken

#Efficient Approach: To solve the problem follow the below idea: 

#In the above approach, at any moment we are keeping track of two values (The length of the longest alternating subsequence ending at index i, and the last element is smaller than or greater than the previous element), for every element on the array. To optimize space, we only need to store two variables for element at any index i

#inc = Length of longest alternative subsequence so far with current value being greater than it’s previous value.
#dec = Length of longest alternative subsequence so far with current value being smaller than it’s previous value.
#The tricky part of this approach is to update these two values. 

#“inc” should be increased, if and only if the last element in the alternative sequence was smaller than it’s previous element.
#“dec” should be increased, if and only if the last element in the alternative sequence was greater than it’s previous element.

#Follow the below steps to solve the problem:

#Declare two integers inc and dec equal to one
#Run a loop for i [1, N-1]
#If arr[i] is greater than the previous element then set inc equal to dec + 1
#Else if arr[i] is smaller than the previous element then set dec equal to inc + 1
#Return maximum of inc and dec
#Below is the implementation of the above approach:


# Python3 program for above approach
def LAS(arr, n):
 
    # "inc" and "dec" initialized as 1
    # as single element is still LAS
    inc = 1
    dec = 1
 
    # Iterate from second element
    for i in range(1, n):
 
        if (arr[i] > arr[i-1]):
 
            # "inc" changes if "dec"
            # changes
            inc = dec + 1
        elif (arr[i] < arr[i-1]):
 
            # "dec" changes if "inc"
            # changes
            dec = inc + 1
 
    # Return the maximum length
    return max(inc, dec)
 
 
# Driver Code
if __name__ == "__main__":
    arr = [10, 22, 9, 33, 49, 50, 31, 60]
    n = len(arr)
 
    # Function Call
    print(LAS(arr, n))
#Output:

#6
#Time Complexity: O(N) 
#Auxiliary Space: O(1)