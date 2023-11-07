#Count zeros in a row wise and column wise sorted matrix

#Difficulty Level : Easy

#Given a N x N binary matrix (elements in matrix can be either 1 or 0) where each row and column of the matrix is sorted in ascending order, count number of 0s present in it.
#Expected time complexity is O(N).

#Examples: 

#Input: 
[0, 0, 0, 0, 1]
[0, 0, 0, 1, 1]
[0, 1, 1, 1, 1]
[1, 1, 1, 1, 1]
[1, 1, 1, 1, 1]

Output: 8


#Input: 
[0, 0]
[0, 0]

Output: 4


#Input: 
[1, 1, 1, 1]
[1, 1, 1, 1]
[1, 1, 1, 1]
[1, 1, 1, 1]

#Output: 0

#The idea is very simple. We start from the bottom-left corner of the matrix and repeat below steps until we find the top or right edge of the matrix.

#Decrement row index until we find a 0. 
#Add number of 0s in current column i.e. current row index + 1 to the result and move right to next column (Increment col index by 1).
#The above logic will work since the matrix is row-wise and column-wise sorted. The logic will also work for any matrix containing non-negative integers.

#Below is the implementation of above idea :

#C++
#C
#Java
#Python
# Python program to count number
# of 0s in the given row-wise
# and column-wise sorted
# binary matrix.
 
# Function to count number
# of 0s in the given
# row-wise and column-wise
# sorted binary matrix.
def countZeroes(mat):
     
    # start from bottom-left
    # corner of the matrix
    N = 5;
    row = N - 1;
    col = 0;
 
    # stores number of
    # zeroes in the matrix
    count = 0;
 
    while (col < N):
         
        # move up until
        # you find a 0
        while (mat[row][col]):
             
            # if zero is not found
            # in current column, we
            # are done
            if (row < 0):
                return count;
            row = row - 1;
 
        # add 0s present in
        # current column to result
        count = count + (row + 1);
 
        # move right to
        # next column
        col = col + 1;
 
    return count;
     
# Driver Code
mat = [[0, 0, 0, 0, 1],
       [0, 0, 0, 1, 1],
       [0, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]];
 
print( countZeroes(mat));
 
# This code is contributed
# by chandan_jnu

#Output
#8
#Time complexity of above solution is O(n) since the solution follows single path from bottom-left corner to top or right edge of the matrix. 
#Auxiliary space used by the program is O(1). since no extra space has been taken.



#This article is contributed by Aditya Goel. If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.





#Like
#10
#Previous
#Count entries equal to x in a special matrix
#Next
#Sort the matrix row-wise and column-wise
#Related Articles
#1.
#Count Negative Numbers in a Column-Wise and Row-Wise Sorted Matrix
#2.
#Search in a row wise and column wise sorted matrix
#3.
#Largest row-wise and column-wise sorted sub-matrix
#4.
#Maximum sum of any submatrix of a Matrix which is sorted row-wise and column-wise
#5.
#heapq in Python to print all elements in sorted order from row and column wise sorted matrix
#6.
#Print all elements in sorted order from row and column wise sorted matrix
#7.
#Kth smallest element in a row-wise and column-wise sorted 2D array
#8.
#Check if a grid can become row-wise and column-wise sorted after adjacent swaps
#9.
#Sort the matrix row-wise and column-wise
#10.
#C++ Program to Sort the matrix row-wise and column-wise