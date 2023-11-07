#Swap major and minor diagonals of a square matrix

#Difficulty Level : Basic
Swap major and minor diagonals of a square matrix

Difficulty Level : Basic
Given a square matrix, swap the element of major and minor diagonals.

Major Diagonal Elements of a Matrix : 
The Major Diagonal Elements are the ones that occur from Top Left of Matrix Down To Bottom Right Corner. The Major Diagonal is also known as Main Diagonal or Primary Diagonal.

Minor Diagonal Elements of a Matrix : 
The Minor Diagonal Elements are the ones that occur from Top Right of Matrix Down To Bottom Left Corner. Also known as Secondary Diagonal.

Example : 

Input : 0 1 2
        3 4 5
        6 7 8

Output : 2 1 0
         3 4 5
         8 7 6
Recommended: Please try your approach on {IDE} first, before moving on to the solution.
Approach: The Simple thing one should know is that the indexes of Primary or Major diagonal are same i.e. lets say A is matrix then A[1][1] will be a Major Diagonal element and sum of indexes of Minor Diagonal is equal to size of Matrix. Lets say A is a matrix of size 3 then A[1][2] will be Minor Diagonal element.

Below is the implementation of above approach : 

C++
Java
Python3
# Python3 Program to swap diagonal of a matrix
 
# size of square matrix
N = 3
 
# Function to swap diagonal of matrix
def swapDiagonal(matrix):
     
    for i in range(N):
         
        matrix[i][i], matrix[i][N-i-1] = \
            matrix[i][N-i-1], matrix[i][i]
 
 
# Driver Code
matrix = [[0, 1, 2],
          [3, 4, 5],
          [6, 7, 8]]
 
# swap diagonals of matrix
swapDiagonal(matrix);
 
# Displaying modified matrix
for i in range(N):   
    for j in range(N):       
        print(matrix[i][j], end = ' ')       
    print()
C#
PHP
Javascript
Output


2 1 0 
3 4 5 
8 7 6 
Time Complexity: O(N*N), as we are using nested loops to traverse N*N times.
Auxiliary Space: O(1), as we are not using any extra space.

