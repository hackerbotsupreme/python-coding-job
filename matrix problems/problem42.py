#Print maximum sum square sub-matrix of given size

#Difficulty Level : Hard
#Given an N x N matrix, find a k x k submatrix where k <= N and k >= 1, such that sum of all the elements in submatrix is maximum. The input matrix can contain zero, positive and negative numbers.

#For example consider below matrix, if k = 3, then output should print the sub-matrix enclosed in blue. 

#rectangle

#We strongly recommend you to minimize your browser and try this yourself first.


#A Simple Solution is to consider all possible sub-squares of size k x k in our input matrix and find the one which has maximum sum. Time complexity of above solution is O(N2k2).
#We can solve this problem in O(N2) time. This problem is mainly an extension of this problem of printing all sums. The idea is to preprocess the given square matrix. In the preprocessing step, calculate sum of all vertical strips of size k x 1 in a temporary square matrix stripSum[][]. Once we have sum of all vertical strips, we can calculate sum of first sub-square in a row as sum of first k strips in that row, and for remaining sub-squares, we can calculate sum in O(1) time by removing the leftmost strip of previous subsquare and adding the rightmost strip of new square. 

#Below is the implementation of above idea.

#C++
#C
#Java
#Python3
# An efficient Python3 program to find maximum sum
# sub-square matrix
 
# Size of given matrix
N = 5
 
# A O(n^2) function to the maximum sum sub-
# squares of size k x k in a given square
# matrix of size n x n
def printMaxSumSub(mat, k):
 
    # k must be smaller than or equal to n
    if (k > N):
        return;
 
    # 1: PREPROCESSING
    # To store sums of all strips of size k x 1
    stripSum = [[0 for j in range(N)] for i in range(N)];
 
    # Go column by column
    for j in range(N):
         
        # Calculate sum of first k x 1 rectangle
        # in this column
        sum = 0;
        for i in range(k):
            sum += mat[i][j];
        stripSum[0][j] = sum;
 
        # Calculate sum of remaining rectangles
        for i in range(1,N-k+1):
            sum += (mat[i+k-1][j] - mat[i-1][j]);
            stripSum[i][j] = sum;
 
    # max_sum stores maximum sum and its
    # position in matrix
    max_sum = -1000000000
    i_ind = 0
    j_ind = 0
 
    # 2: CALCULATE SUM of Sub-Squares using stripSum[][]
    for i in range(N-k+1):
         
        # Calculate and print sum of first subsquare
        # in this row
        sum = 0;
        for j in range(k):
            sum += stripSum[i][j];
 
        # Update max_sum and position of result
        if (sum > max_sum):
            max_sum = sum;
            i_ind = i
            j_ind = 0
 
 
        # Calculate sum of remaining squares in
        # current row by removing the leftmost
        # strip of previous sub-square and adding
        # a new strip
        for j in range(1,N-k+1):
            sum += (stripSum[i][j+k-1] - stripSum[i][j-1]);
 
            # Update max_sum and position of result
            if (sum > max_sum):
                max_sum = sum;
                i_ind = i
                j_ind = j
 
    # Print the result matrix
    for i in range(k):
        for j in range(k):
            print(mat[i+i_ind][j+j_ind], end = ' ')
        print()
 
# Driver program to test above function
mat = [[1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 8, 6, 7, 3],
        [4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5],
    ];
k = 3;
print("Maximum sum 3 x 3 matrix is");
printMaxSumSub(mat, k);
 
# This code is contributed by rutvik_56.

#Output


#Maximum sum 3 x 3 matrix is
#8 6 7 
#4 4 4 
#5 5 5 
#Time complexity: O(N2).
#Auxiliary Space: O(N2).

#Related Articles: 
#Given an n x n square matrix, find sum of all sub-squares of size k x k 
#Maximum sum rectangle in a 2D matrix

#This article is contributed by Aarti_Rathi and Aditya Goel. If you like GeeksforGeeks and would like to contribute, you can also write an article and mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks. 

#Recommended
#Solve DSA problems on GfG Practice.

#Solve Problems




#Like
#20
#Next
#Given an n x n square matrix, find sum of all sub-squares of size k x k
#Related Articles
#1.
##Find Maximum Length Of A Square Submatrix Having Sum Of Elements At-Most K
#2.
##Submatrix of given size with maximum 1's
#3.
#Largest possible square submatrix with maximum AND value
#4.
#Minimum area such that all submatrix of the size have same maximum value
#5.
#Check if a matrix contains a square submatrix with 0 as boundary element
#6.
#Maximum size of square such that all submatrices of that size have sum less than K
#7.
#Minimum operations to convert Binary Matrix A to B by flipping submatrix of size K
#8.
#Maximum sum of any submatrix of a Matrix which is sorted row-wise and column-wise
#9.
#Maximum sum submatrix
#10.
#Minimum sum submatrix in a given 2D array
#Article Contributed By :
#https://media.geeksforgeeks.org/auth/avatar.png
#GeeksforGeeks
#Vote for difficulty
#Current difficulty : Hard
#Easy
#Normal
#Medium
#Hard
#Expert
#Improved By :
#Vivekkumar Singh
#princi singh
#rrrtnx
#rutvik_56
#simmytarika5
##adityakumar129
#codewithmini
#hardikkoriintern
#Article Tags :
#Matrix
#Practice Tags :
#Matrix
#Improve Article
#Report Iss