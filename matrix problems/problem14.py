#Swap major and minor diagonals of a square matrix

#Difficulty Level : Basic

#Given a square matrix, swap the element of major and minor diagonals.

#Major Diagonal Elements of a Matrix : 
#The Major Diagonal Elements are the ones that occur from Top Left of Matrix Down To Bottom Right Corner. The Major Diagonal is also known as Main Diagonal or Primary Diagonal.

#Minor Diagonal Elements of a Matrix : 
#The Minor Diagonal Elements are the ones that occur from Top Right of Matrix Down To Bottom Left Corner. Also known as Secondary Diagonal.


#Example : 

#Input : 0 1 2
#        3 4 5
#        6 7 8

#Output : 2 1 0
#         3 4 5
#         8 7 6
#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#Approach: The Simple thing one should know is that the indexes of Primary or Major diagonal are same i.e. lets say A is matrix then A[1][1] will be a Major Diagonal element and sum of indexes of Minor Diagonal is equal to size of Matrix. Lets say A is a matrix of size 3 then A[1][2] will be Minor Diagonal element.

#Below is the implementation of above approach : 

#C++
#Java
#Python3
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
#C#
#PHP
#Javascript
#Output


#2 1 0 
#3 4 5 
#8 7 6 
#Time Complexity: O(N*N), as we are using nested loops to traverse N*N times.
#Auxiliary Space: O(1), as we are not using any extra space.





#Like
#10
#Previous
#Program to print Lower triangular and Upper triangular matrix of an array
#Next
##Squares of Matrix Diagonal Elements
#Related Articles
#1.
#Find trace of matrix formed by adding Row-major and Column-major order of same matrix
#2.
#Calculation of address of element of 1-D, 2-D, and 3-D using row-major and column-major order
#3.
#Performance analysis of Row major and Column major order of iterating arrays in C
#4.
#Number of positions with Same address in row major and column major order
#5.
#Find smallest and largest element from square matrix diagonals
#6.
#Sum of both diagonals of a spiral odd-order square matrix
#7.
#Row-wise common elements in two diagonals of a square matrix
#8.
#Finding the converging element of the diagonals in a square matrix
#9.
#Sum of all parts of a square Matrix divided by its diagonals
#10.
#Find the product of sum of two diagonals of a square Matrix