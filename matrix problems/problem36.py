#A Boolean Matrix Question

#Difficulty Level : Medium
#Given a boolean matrix mat[M][N] of size M X N, modify it such that if a matrix cell mat[i][j] is 1 (or true) then make all the cells of ith row and jth column as 1. 

#Examples:

#Input: {{1, 0},
#           {0, 0}}
#Output: {{1, 1}
#              {1, 0}}
#Input: {{0, 0, 0},
#            {0, 0, 1}}
#Output: {{0, 0, 1},
#               {1, 1, 1}}

#Input: {{1, 0, 0, 1},
#           {0, 0, 1, 0},
#          {0, 0, 0, 0}}
#Output: {{1, 1, 1, 1},
#               {1, 1, 1, 1},
 #             {1, 0, 1, 1}}

#Recommended Problem
#Boolean Matrix
#Arrays
#Matrix
#+1 more
#Microsoft
#Solve Problem
#Submission count: 63.1K
#Follow the steps below to solve the problem

#Create two temporary arrays row[M] and col[N]. Initialize all values of row[] and col[] as 0. 
#Traverse the input matrix mat[M][N]. If you see an entry mat[i][j] as true, then mark row[i] and col[j] as true. 
#Traverse the input matrix mat[M][N] again. For each entry mat[i][j], check the values of row[i] and col[j]. If any of the two values (row[i] or col[j]) is true, then mark mat[i][j] as true.
#Below is the implementation of the above approach:


# Python3 Code For A Boolean Matrix Question
R = 3
C = 4
 
 
def modifyMatrix(mat):
    row = [0] * R
    col = [0] * C
 
    # Initialize all values of row[] as 0
    for i in range(0, R):
        row[i] = 0
 
    # Initialize all values of col[] as 0
    for i in range(0, C):
        col[i] = 0
 
    # Store the rows and columns to be marked
    # as 1 in row[] and col[] arrays respectively
    for i in range(0, R):
 
        for j in range(0, C):
            if (mat[i][j] == 1):
                row[i] = 1
                col[j] = 1
 
    # Modify the input matrix mat[] using the
    # above constructed row[] and col[] arrays
    for i in range(0, R):
 
        for j in range(0, C):
            if (row[i] == 1 or col[j] == 1):
                mat[i][j] = 1
 
# A utility function to print a 2D matrix
 
 
def printMatrix(mat):
    for i in range(0, R):
 
        for j in range(0, C):
            print(mat[i][j], end=" ")
        print()
 
 
# Driver Code
mat = [[1, 0, 0, 1],
       [0, 0, 1, 0],
       [0, 0, 0, 0]]
 
print("Input Matrix")
printMatrix(mat)
 
modifyMatrix(mat)
 
print("Matrix after modification")
printMatrix(mat)
 
# This code is contributed by Nikita Tiwari.

#Output


#Input Matrix 
#1001
#0010
#0000
#Matrix after modification 
#1111
#1111
#1011
#Time Complexity: O(M*N), Traversing over the matrix two times.
#Auxiliary Space: O(M + N), Taking two arrays one of size M and another of size N.

#Thanks to Dixit Sethi for suggesting this method. 

#A Boolean Matrix Question using O(1) Space:
#This method is a space-optimized version of above method. This method uses the first row and first column of the input matrix in place of the auxiliary arrays row[] and col[] of above method. First take care of the first row and column and store the info about these two in two flag variables rowFlag and colFlag. Once we have this info, we can use the first row and first column as auxiliary arrays and apply method 1 for submatrix (matrix excluding first row and first column) of size (M-1)*(N-1).

#Follow the steps to solve the problem:

#Scan the first row and set a variable rowFlag to indicate whether we need to set all 1s in the first row or not. 
#Scan the first column and set a variable colFlag to indicate whether we need to set all 1s in the first column or not. 
#Use the first row and first column as the auxiliary arrays row[] and col[] respectively, consider the matrix as a submatrix starting from the second row and second column, and apply above method.
#Finally, using rowFlag and colFlag, update the first row and first column if needed.
#Below is the implementation of above approach:


# Python3 Code For A Boolean Matrix Question
def modifyMatrix(mat):
 
    # variables to check if there are any 1
    # in first row and column
    row_flag = False
    col_flag = False
 
    # updating the first row and col
    # if 1 is encountered
    for i in range(0, len(mat)):
 
        for j in range(0, len(mat)):
            if (i == 0 and mat[i][j] == 1):
                row_flag = True
 
            if (j == 0 and mat[i][j] == 1):
                col_flag = True
 
            if (mat[i][j] == 1):
                mat[0][j] = 1
                mat[i][0] = 1
 
    # Modify the input matrix mat[] using the
    # first row and first column of Matrix mat
    for i in range(1, len(mat)):
 
        for j in range(1, len(mat) + 1):
            if (mat[0][j] == 1 or mat[i][0] == 1):
                mat[i][j] = 1
 
    # modify first row if there was any 1
    if (row_flag == True):
        for i in range(0, len(mat)):
            mat[0][i] = 1
 
    # modify first col if there was any 1
    if (col_flag == True):
        for i in range(0, len(mat)):
            mat[i][0] = 1
 
# A utility function to print a 2D matrix
 
 
def printMatrix(mat):
 
    for i in range(0, len(mat)):
        for j in range(0, len(mat) + 1):
            print(mat[i][j], end="")
 
        print()
 
 
# Driver Code
mat = [[1, 0, 0, 1],
       [0, 0, 1, 0],
       [0, 0, 0, 0]]
 
print("Input Matrix :")
printMatrix(mat)
 
modifyMatrix(mat)
 
print("Matrix After Modification :")
printMatrix(mat)
 
# This code is contributed by Nikita tiwari.

#Output
#Input Matrix :
#1 0 0 1 
#0 0 1 0 
#0 0 0 0 
#Matrix After Modification :
#1 1 1 1 
#1 1 1 1 
#1 0 1 1 
#Time Complexity: O(M*N), Traversing over the matrix two times.
#Auxiliary Space: O(1)

# Thanks to Sidh for suggesting this method. 





#Like
#69
#Previous
#Print a given matrix in spiral form
#Next
#Print unique rows in a given Binary matrix
#Related Articles
#1.
#Python | Print unique rows in a given boolean matrix using Set with tuples
#2.
#Find regions with most common region size in a given boolean matrix
#3.
#Find size of the largest region in Boolean Matrix
#4.
#Given a Boolean Matrix, find k such that all elements in k'th row are 0 and k'th column are 1.
#5.
#Generate a Matrix such that given Matrix elements are equal to Bitwise OR of all corresponding row and column elements of generated Matrix
#6.
#Generate matrix from given Sparse Matrix using Linked List and reconstruct the Sparse Matrix
#7.
#Boolean Parenthesization Problem | DP-37
#8.
#Maximize sum of N X N upper left sub-matrix from given 2N X 2N matrix
#9.
#Circular Matrix (Construct a matrix with numbers 1 to m*n in spiral way)
#10.
#Find trace of matrix formed by adding Row-major and Column-major order of same matrix