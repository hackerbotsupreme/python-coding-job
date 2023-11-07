#Find number of transformation to make two Matrix Equal

#Difficulty Level : Hard


#Given two matrices A and B of order n*m. The task is to find the required number of transformation steps so that both matrices became equal, print -1 if it is not possible. 

#Transformation step is as: 

#Select any one matrix out of two matrices. 
# Choose either row/column of the selected matrix. 
# Increment every element of select row/column by 1. 
#Examples : 

#Input : 
#A[2][2]: 1 1
#         1 1
#B[2][2]: 1 2
#         3 4
#Output : 3
##Explanation :
#1 1   ->   1 2   ->   1 2   ->   1 2
#1 1   ->   1 2   ->   2 3   ->   3 4

#Input :
#A[2][2]: 1 1
#         1 0
#B[2][2]: 1 2
#         3 4
#Output : -1
#Explanation : No transformation will make A and B equal.
#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#The key steps behind the solution of this problem are:

#Incrementing any row of A[][] is same as decrementing the same row of B[][]. So, we can have the solution after having the transformation on only one matrix either incrementing or decrementing. 
#So make A[i][j] = A[i][j] - B[i][j].
#For example,
#If given matrices are,
#A[2][2] : 1 1  
#          1 1
#B[2][2] : 1 2
#          3 4
#After subtraction, A[][] becomes,
#A[2][2] : 0 -1
#         -2 -3 
#For every transformation either 1st row/ 1st column element necessarily got changed, same is true for other i-th row/column.
#If ( A[i][j] – A[i][0] – A[0][j] + A[0][0] != 0) then no solution exists.
#Elements of 1st row and 1st column only leads to result.
 
#// Update matrix A[][]
#// so that only A[][]
#// has to be transformed
#for (i = 0; i < n; i++)
#    for (j = 0; j < m; j++)
#        A[i][j] -= B[i][j];

#// Check necessary condition
#// For condition for 
#// existence of full transformation
#for (i = 1; i < n; i++)
#    for (j = 1; j < m; j++)
#        if (A[i][j] - A[i][0] - A[0][j] + A[0][0] != 0)
#            return -1;

#// If transformation is possible
#// calculate total transformation
#result = 0;
#for (i = 0; i < n; i++)
#    result += abs(A[i][0])
#for (j = 0; j < m; j++)
#    result += abs(A[0][j] - A[0][0]);
#return abs(result);
#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#Implementation:


# Python3 program to find number of
# countOpsation to make two matrix
# equals
def countOps(A, B, m, n):
 
    # Update matrix A[][] so that only
    # A[][] has to be countOpsed
    for i in range(n):
        for j in range(m):
            A[i][j] -= B[i][j];
 
    # Check necessary condition for
    # condition for existence of full
    # countOpsation
    for i in range(1, n):
        for j in range(1, n):
            if (A[i][j] - A[i][0] -
                A[0][j] + A[0][0] != 0):
                return -1;
 
    # If countOpsation is possible
    # calculate total countOpsation
    result = 0;
 
    for i in range(n):
        result += abs(A[i][0]);
 
    for j in range(m):
        result += abs(A[0][j] - A[0][0]);
 
    return (result);
 
# Driver code
if __name__ == '__main__':
    A = [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]];
 
    B = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]];
          
    print(countOps(A, B, 3, 3));
 
# This code is contributed by Rajput-Ji

#Output
#12
#Time Complexity: O (n*m)
#Auxiliary Space: O(1)

#This article is contributed by Aarti_Rathi and Shivam Pradhan (anuj_charm). If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks. 





#Like
##6
#Previous
##Form coils in a matrix
#Next
#Printing all solutions in N-Queen Problem
#Related Articles
#1.
#Generate a Matrix such that given Matrix elements are equal to Bitwise OR of all corresponding row and column elements of generated Matrix
#2.
#Number of ways to select equal sized subarrays from two arrays having atleast K equal pairs of elements
#3.
#Minimum operations of given type to make all elements of a matrix equal
#4.
#Filling diagonal to make the sum of every row, column and diagonal equal of 3x3 matrix
#5.
#Minimize flips required to make all shortest paths from top-left to bottom-right of a binary matrix equal to S
#6.
#Check if it is possible to make the given matrix increasing matrix or not
#7.
#Generate a matrix having each element equal to the sum of specified submatrices of a given matrix
#8.
#Generate matrix from given Sparse Matrix using Linked List and reconstruct the Sparse Matrix
#9.
#Replace specified matrix elements such that no two adjacent elements are equal
#10.
#Count right angled triangles in a matrix havi