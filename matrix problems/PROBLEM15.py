#Mirror of matrix across diagonal

#Difficulty Level : Easy

#Given a 2-D array of order N x N, print a matrix that is the mirror of the given tree across the diagonal. We need to print the result in a way: swap the values of the triangle above the diagonal with the values of the triangle below it like a mirror image swap. Print the 2-D array obtained in a matrix layout.

#Examples:  

#Input : int mat[][] = {{1 2 4 }
#                       {5 9 0}
#                       { 3 1 7}}
#Output :  1 5 3 
#          2 9 1
#          4 0 7

#Input : mat[][] = {{1  2  3  4 }
#                   {5  6  7  8 }
#                   {9  10 11 12}
#                   {13 14 15 16} }
##Output : 1 5 9 13 
#         2 6 10 14  
#         3 7 11 15 
#         4 8 12 16 
#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#A simple solution to this problem involves extra space. We traverse all right diagonal (right-to-left) one by one. During the traversal of the diagonal, first, we push all the elements into the stack and then we traverse it again and replace every element of the diagonal with the stack element. 

#Below is the implementation of the above idea. 

#C++
#Java
#Python3
# Simple Python3 program to find mirror of
# matrix across diagonal.
MAX = 100
 
def imageSwap(mat, n):
     
    # for diagonal which start from at
    # first row of matrix
    row = 0
     
    # traverse all top right diagonal
    for j in range(n):
         
        # here we use stack for reversing
        # the element of diagonal
        s = []
        i = row
        k = j
        while (i < n and k >= 0):
            s.append(mat[i][k])
            i += 1
            k -= 1
             
        # push all element back to matrix
        # in reverse order
        i = row
        k = j
        while (i < n and k >= 0):
            mat[i][k] = s[-1]
            k -= 1
            i += 1
            s.pop()
             
    # do the same process for all the
    # diagonal which start from last
    # column
    column = n - 1
    for j in range(1, n):
         
        # here we use stack for reversing
        # the elements of diagonal
        s = []
        i = j
        k = column
        while (i < n and k >= 0):
            s.append(mat[i][k])
            i += 1
            k -= 1
             
        # push all element back to matrix
        # in reverse order
        i = j
        k = column
        while (i < n and k >= 0):
            mat[i][k] = s[-1]
            i += 1
            k -= 1
            s.pop()
 
# Utility function to print a matrix
def printMatrix(mat, n):
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=" ")
        print()
         
# Driver code
mat = [[1, 2, 3, 4],[5, 6, 7, 8],
        [9, 10, 11, 12],[13, 14, 15, 16]]
n = 4
imageSwap(mat, n)
printMatrix(mat, n)
 
# This code is contributed by shubhamsingh10
#C#
#Javascript
#Output: 

#1 5 9 13 
#2 6 10 14 
#3 7 11 15 
#4 8 12 16
#Time complexity : O(n2)
#Auxiliary Space: O(n), as stack is used

#An efficient solution to this problem is that if we observe an output matrix, then we notice that we just have to swap (mat[i][j] to mat[j][i]). 
#Below is the implementation of the above idea. 



#Implementation:

#C++
#Java
#Python3
# Efficient Python3 program to find mirror of
# matrix across diagonal.
from builtins import range
MAX = 100;
 
def imageSwap(mat, n):
 
    # traverse a matrix and swap
    # mat[i][j] with mat[j][i]
    for i in range(n):
        for j in range(i + 1):
            t = mat[i][j];
            mat[i][j] = mat[j][i]
            mat[j][i] = t
 
# Utility function to print a matrix
def printMatrix(mat, n):
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=" ");
        print();
 
# Driver code
if __name__ == '__main__':
    mat = [1, 2, 3, 4], \
        [5, 6, 7, 8], \
        [9, 10, 11, 12], \
        [13, 14, 15, 16];
    n = 4;
    imageSwap(mat, n);
    printMatrix(mat, n);
 
# This code is contributed by Rajput-Ji
#C#
#PHP
#Javascript
#Output: 

#1 5 9 13 
#2 6 10 14 
#3 7 11 15 
#4 8 12 16 
#Time complexity : O(n2)
#Auxiliary Space: O(1)





#Like
#2
#Next
#Rotate a matrix by 90 degree in clockwise direction without using any extra space
#Related Articles
#1.
#C++ Program for Mirror of matrix across diagonal
#2.
#Java Program for Mirror of matrix across diagonal
#3.
#Python Program for Mirror of matrix across diagonal
#4.
#Javascript Program for Mirror of matrix across diagonal
#5.
#Program to swap upper diagonal elements with lower diagonal elements of matrix.
#6.
#Filling diagonal to make the sum of every row, column and diagonal equal of 3x3 matrix
#7.
#Maximum sum of elements in a diagonal parallel to the main diagonal of a given Matrix
#8.
#Program to check diagonal matrix and scalar matrix
#9.
#Program to convert given Matrix to a Diagonal Matrix
#10.
#Construct a square Matrix whose parity of diagonal sum is same as size of matrix