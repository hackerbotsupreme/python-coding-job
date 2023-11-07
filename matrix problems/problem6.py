#Find maximum element of each row in a matrix

#Difficulty Level : Basic

#Given a matrix, the task is to find the maximum element of each row.

#Examples: 

#Input :  [1, 2, 3]
         [1, 4, 9]
         [76, 34, 21]

#Output :
#3
#9
#76

Input : [1, 2, 3, 21]
        [12, 1, 65, 9]
        [1, 56, 34, 2]
Output :
21
65
56
Recommended: Please try your approach on {IDE} first, before moving on to the solution.
Approach : Approach is very simple. The idea is to run the loop for no_of_rows. Check each element inside the row and find for the maximum element. Finally, print the element. 

Implementation:

C++
Java
Python
# Python program to find maximum
# element of each row in a matrix
 
# importing numpy
import numpy
 
# Function to get max element
def maxelement(arr):
     
    # get number of rows and columns
    no_of_rows = len(arr)
    no_of_column = len(arr[0])
     
    for i in range(no_of_rows):
         
        # Initialize max1 to 0 at beginning
        # of finding max element of each row
        max1 = 0
        for j in range(no_of_column):
            if arr[i][j] > max1 :
                max1 = arr[i][j]
                 
        # print maximum element of each row
        print(max1)
 
# Driver Code
arr = [[3, 4, 1, 8],
       [1, 4, 9, 11],
       [76, 34, 21, 1],
       [2, 1, 4, 5]]
 
# Calling the function       
maxelement(arr)
C#
PHP
Javascript
Output
8
11
76
5
Complexity Analysis:

Time Complexity: O(n*m) (where, n refers to no. of rows and m refers to no. of columns)
Auxiliary Space: O(n) (where, n refers to no. of rows)
