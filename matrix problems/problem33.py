#Minimum flip required to make Binary Matrix symmetric

#Difficulty Level : Basic
#Given a Binary Matrix of size N X N, consisting of 1s and 0s. The task is to find the minimum flips required to make the matrix symmetric along main diagonal.
#Examples : 
 

#Input : mat[][] = { { 0, 0, 1 },
#                    { 1, 1, 1 },
#                    { 1, 0, 0 } };
#Output : 2
#Value of mat[1][0] is not equal to mat[0][1].
#Value of mat[2][1] is not equal to mat[1][2].
#So, two flip are required.

#Input : mat[][] = { { 1, 1, 1, 1, 0 },
#                    { 0, 1, 0, 1, 1 },
#                    { 1, 0, 0, 0, 1 },
#                    { 0, 1, 0, 1, 0 },
#                    { 0, 1, 0, 0, 1 } };                  
#Output : 3
 

#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#Method 1 (Simple): 
#The idea is to find the transpose of the matrix and find minimum number of flip required to make transpose and original matrix equal. To find minimum flip, find the number of position where original matrix and transpose matrix are not same, say x. So, our answer will be x/2.
#Below is the implementation of this approach: 
 

#C++
#Java
#Python3
# Python3 code to find minimum flip
# required to make Binary Matrix
# symmetric along main diagonal
N = 3
 
# Return the minimum flip required
# to make Binary Matrix symmetric
# along main diagonal.
def minimumflip(mat, n):
     
    transpose =[[0] * n] * n
     
    # finding the transpose of the matrix
    for i in range(n):
        for j in range(n):
            transpose[i][j] = mat[j][i]
     
    # Finding the number of position
    # where element are not same.
    flip = 0
    for i in range(n):
        for j in range(n):
            if transpose[i][j] != mat[i][j]:
                flip += 1
     
    return int(flip / 2)
     
# Driver Program
n = 3
mat =[[ 0, 0, 1],
      [ 1, 1, 1],
      [ 1, 0, 0]]
print( minimumflip(mat, n))
 
# This code is contributed by "Sharad_Bhardwaj".
#C#
#PHP
#Javascript
#Output : 
 

#2
#Time Complexity: O(N2)

#Auxiliary Space: O(N2)

#Method 2: (Efficient Approach) 
#The idea is to find minimum flip required to make upper triangle of matrix equals to lower triangle of the matrix. To do so, we run two nested loop, outer loop from i = 0 to n i.e for each row of the matrix and the inner loop from j = 0 to i, and check whether mat[i][j] is equal to mat[j][i]. Count of number of instance where they are not equal will be the minimum flip required to make matrix symmetric along main diagonal.
#Below is the implementation of this approach: 
 




# Python3 code to find minimum flip
# required to make Binary Matrix
# symmetric along main diagonal
N = 3
 
# Return the minimum flip required
# to make Binary Matrix symmetric
# along main diagonal.
def minimumflip( mat , n ):
 
    # Comparing elements across diagonal
    flip = 0
    for i in range(n):
        for j in range(i):
            if mat[i][j] != mat[j][i] :
                flip += 1
     
    return flip
 
# Driver Program
n = 3
mat =[[ 0, 0, 1],
      [ 1, 1, 1],
      [ 1, 0, 0]]
print( minimumflip(mat, n))
 
# This code is contributed by "Sharad_Bhardwaj".

#Output : 
 

#2
#Time Complexity: O(N2)

#Auxiliary Space: O(1), since no extra space has been taken.
 





#Like
#3
#Previous
#Check if all rows of a matrix are circular rotations of each other
#Next
#Sum of middle row and column in Matrix
#Related Articles
#1.
#A square matrix as sum of symmetric and skew-symmetric matrices
#2.
#Convert given Matrix into a Symmetric Matrix by replacing elements at (i, j) and (j, i) with their mean
#3.
#Horizontally Flip a Binary Matrix
#4.
#Minimum row or column swaps required to make every pair of adjacent cell of a Binary Matrix distinct
#5.
#C Program To Check whether Matrix is Skew Symmetric or not
#6.
#Program to check if a matrix is symmetric
#7.
#Find a Symmetric matrix of order N that contain integers from 0 to N-1 and main diagonal should contain only 0's
#8.
#C++ Program to check if a matrix is symmetric
#9.
#Java Program to check if a matrix is symmetric
#310.
#Python Program to check if a matrix is symmetric