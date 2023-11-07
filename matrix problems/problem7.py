#Shift matrix elements row-wise by k

#Difficulty Level : Easy

Given a square matrix mat[][] and a number k. The task is to shift the first k elements of each row to the right of the matrix.

Examples : 

Input : mat[N][N] = {{1, 2, 3},
                     {4, 5, 6},
                     {7, 8, 9}}
        k = 2
Output :mat[N][N] = {{3, 1, 2}
                     {6, 4, 5}
                     {9, 7, 8}}

Input : mat[N][N] = {{1, 2, 3, 4}
                     {5, 6, 7, 8}
                     {9, 10, 11, 12}
                     {13, 14, 15, 16}}
        k = 2
Output :mat[N][N] = {{3, 4, 1, 2}
                     {7, 8, 5, 6}
                     {11, 12, 9, 10}
                     {15, 16, 13, 14}}
Note: Matrix should be a square matrix 
Recommended: Please try your approach on {IDE} first, before moving on to the solution.
Implementation:

C++
Java
Python3
# Python3 program to shift k
# elements in a matrix.
 
N = 4
# Function to shift first k
# elements of each row of
# matrix.
def shiftMatrixByK(mat, k):
    if (k > N) :
        print ("shifting is"
            " not possible")
        return
     
    j = 0
    while (j < N) :
         
        # Print elements from
        # index k
        for i in range(k, N):
            print ("{} " .
            format(mat[j][i]), end="")
             
        # Print elements before
        # index k
        for i in range(0, k):
            print ("{} " .
            format(mat[j][i]), end="")
             
        print ("")
        j = j + 1
 
# Driver code
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
k = 2
 
# Function call
shiftMatrixByK(mat, k)
 
# This code is contributed by
# Manish Shaw (manishshaw1)
C#
PHP
Javascript
Output
3 4 1 2 
7 8 5 6 
11 12 9 10 
15 16 13 14 
Complexity Analysis:

Time Complexity: O(n2), 
Auxiliary Space: O(1)



