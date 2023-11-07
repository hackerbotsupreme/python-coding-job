#Given a matrix of ‘O’ and ‘X’, find the largest subsquare surrounded by ‘X’

#Difficulty Level : Hard

#Given a matrix where every element is either ‘O’ or ‘X’, find the largest subsquare surrounded by ‘X’. 
#In the below article, it is assumed that the given matrix is also a square matrix. The code given below can be easily extended for rectangular matrices.

#Examples: 

#Input: mat[N][N] = { {'X', 'O', 'X', 'X', 'X'},
#                     {'X', 'X', 'X', 'X', 'X'},
#                     {'X', 'X', 'O', 'X', 'O'},
#                     {'X', 'X', 'X', 'X', 'X'},
#                     {'X', 'X', 'X', 'O', 'O'},
#                    };
#Output: 3
#The square submatrix starting at (1, 1) is the largest
#submatrix surrounded by 'X'
#
#Input: mat[M][N] = { {'X', 'O', 'X', 'X', 'X', 'X'},
#                     {'X', 'O', 'X', 'X', 'O', 'X'},
#                     {'X', 'X', 'X', 'O', 'O', 'X'},
#                     {'X', 'X', 'X', 'X', 'X', 'X'},
#                     {'X', 'X', 'X', 'O', 'X', 'O'},
#                    };
#Output: 4
#The square submatrix starting at (0, 2) is the largest
#submatrix surrounded by 'X'
#Recommended Problem
#Largest subsquare surrounded by X
#Matrix
#Data Structures
#D-E-Shaw
#Solve Problem
#Submission count: 4.1K
#A Simple Solution is to consider every square submatrix and check whether is has all corner edges filled with ‘X’. The time complexity of this solution is O(N4).
#We can solve this problem in O(N3) time using extra space. The idea is to create two auxiliary arrays hor[N][N] and ver[N][N]. The value stored in hor[i][j] is the number of horizontal continuous ‘X’ characters till mat[i][j] in mat[][]. Similarly, the value stored in ver[i][j] is the number of vertical continuous ‘X’ characters till mat[i][j] in mat[][]. 

#Example:

#mat[6][6] =  X  O  X  X  X  X
#             X  O  X  X  O  X
#             X  X  X  O  O  X
#             O  X  X  X  X  X
#             X  X  X  O  X  O
#             O  O  X  O  O  O

#hor[6][6] = 1  0  1  2  3  4
#            1  0  1  2  0  1
#            1  2  3  0  0  1
#            0  1  2  3  4  5
#            1  2  3  0  1  0
#            0  0  1  0  0  0

#ver[6][6] = 1  0  1  1  1  1
#            2  0  2  2  0  2
#            3  1  3  0  0  3
#            0  2  4  1  1  4
#            1  3  5  0  2  0
#            0  0  6  0  0  0
#Once we have filled values in hor[][] and ver[][], we start from the bottommost-rightmost corner of matrix and move toward the leftmost-topmost in row by row manner. For every visited entry mat[i][j], we compare the values of hor[i][j] and ver[i][j], and pick the smaller of two as we need a square. Let the smaller of two be ‘small’. After picking smaller of two, we check if both ver[][] and hor[][] for left and up edges respectively. If they have entries for the same, then we found a subsquare. Otherwise we try for small-1. 

#Below is implementation of the above idea. 

#C++
#Java
#Python3
# A Python3 program to find the largest
# subsquare surrounded by 'X' in a given
# matrix of 'O' and 'X'
import math as mt
 
# Size of given matrix is N X N
N = 6
 
# A utility function to find minimum
# of two numbers
 
 
def getMin(x, y):
    if x < y:
        return x
    else:
        return y
 
# Returns size of Maximum size
# subsquare matrix surrounded by 'X'
 
 
def findSubSquare(mat):
 
    Max = 0  # Initialize result
 
    # Initialize the left-top value
    # in hor[][] and ver[][]
    hor = [[0 for i in range(N)]
           for i in range(N)]
    ver = [[0 for i in range(N)]
           for i in range(N)]
 
    if mat[0][0] == 'X':
        hor[0][0] = 1
        ver[0][0] = 1
 
    # Fill values in hor[][] and ver[][]
    for i in range(N):
 
        for j in range(N):
 
            if (mat[i][j] == 'O'):
                ver[i][j], hor[i][j] = 0, 0
            else:
                if j == 0:
                    ver[i][j], hor[i][j] = 1, 1
                else:
                    (ver[i][j],
                     hor[i][j]) = (ver[i - 1][j] + 1,
                                   hor[i][j - 1] + 1)
 
    # Start from the rightmost-bottommost corner
    # element and find the largest ssubsquare
    # with the help of hor[][] and ver[][]
    for i in range(N - 1, 0, -1):
 
        for j in range(N - 1, 0, -1):
 
            # Find smaller of values in hor[][] and
            # ver[][]. A Square can only be made by
            # taking smaller value
            small = getMin(hor[i][j], ver[i][j])
 
            # At this point, we are sure that there
            # is a right vertical line and bottom
            # horizontal line of length at least 'small'.
 
            # We found a bigger square if following
            # conditions are met:
            # 1)If side of square is greater than Max.
            # 2)There is a left vertical line
            #   of length >= 'small'
            # 3)There is a top horizontal line
            #   of length >= 'small'
            while (small > Max):
 
                if (ver[i][j - small + 1] >= small and
                        hor[i - small + 1][j] >= small):
 
                    Max = small
 
                small -= 1
 
    return Max
 
 
# Driver Code
mat = [['X', 'O', 'X', 'X', 'X', 'X'],
       ['X', 'O', 'X', 'X', 'O', 'X'],
       ['X', 'X', 'X', 'O', 'O', 'X'],
       ['O', 'X', 'X', 'X', 'X', 'X'],
       ['X', 'X', 'X', 'O', 'X', 'O'],
       ['O', 'O', 'X', 'O', 'O', 'O']]
 
# Function call
print(findSubSquare(mat))
 
# This code is contributed by
# Mohit kumar 29

#Output


#4
#Time complexity: O(N2).
#Auxiliary Space: O(N2)

#Optimized approach:

#A more optimized solution would be to pre-compute the number of contiguous ‘X’ horizontally and vertically, in a matrix of pairs named dp. Now  for every entry of dp we have a pair (int, int) which denotes the maximum contiguous ‘X’ till that point, i.e.

#dp[i][j].first denotes contiguous ‘X’ taken horizontally till that point.
#dp[i][j].second denotes contiguous ‘X’ taken vertically till that point.
#Now, a square can be formed with dp[i][j] as the bottom right corner, having sides atmost of length, min(dp[i][j].first, dp[i][j].second)

#So, we make another matrix maxside, which will denote the maximum square side formed having the bottom right corner as arr[i][j]. We’ll try to get some intuition from the properties of a square, i.e. all the sides of the square are equal.

#Let’s store maximum value that can be obtained, as val = min(dp[i][j].first, dp[i][j].second). From point (i, j), we traverse back horizontally by distance Val, and check if the minimum vertical contiguous ‘X’ till that point is equal to Val.


#Similarly, we traverse back vertically by distance Val and check if the minimum horizontal contiguous ‘X’ till that point is equal to Val? Here we are making use of the fact that all sides of square are equal.

#Input Matrix:

#X  O  X  X  X  X

#X  O  X  X  O  X

#X  X  X  O  O  X

#O  X  X  X  X  X

#X  X  X  O  X  O

#O  O  X  O  O  O

#Value of matrix dp:

#(1,1) (0,0) (1,1) (2,1) (3,1) (4,1)  

#(1,2) (0,0) (1,2) (2,2) (0,0) (1,2)  

#(1,3) (2,1) (3,3) (0,0) (0,0) (1,3)  

#(0,0) (1,2) (2,4) (3,1) (4,1) (5,4)  

#(1,1) (2,3) (3,5) (0,0) (1,2) (0,0)  

#(0,0) (0,0) (1,6) (0,0) (0,0) (0,0) 

#Below is the implementation of the above idea:

#C++
#Java
#Python3
# Python3 program to find  the largest
# subsquare surrounded by 'X' in a given
# matrix of 'O' and 'X'
 
# Size of given matrix is N X N
N = 6
 
def maximumSubSquare(arr):
     
    dp = [[[-1, -1] for i in range(51)]
                    for j in range(51)]
 
    # Initialize maxside with 0
    maxside = [[0 for i in range(51)]
                  for j in range(51)]
                   
    x = 0
    y = 0
     
    # Fill the dp matrix horizontally.
    # for contiguous 'X' increment the
    # value of x, otherwise make it 0
    for i in range(N):
        x = 0
         
        for j in range(N):
            if (arr[i][j] == 'X'):
                x += 1
            else:
                x = 0
                 
            dp[i][j][0] = x
 
    # Fill the dp matrix vertically.
    # For contiguous 'X' increment
    # the value of y, otherwise
    # make it 0
    for i in range(N):
      y = 0
        for j in range(N):
            if (arr[j][i] == 'X'):
                y += 1
            else:
                y = 0
                 
            dp[j][i][1] = y
     
    # Now check , for every value of (i, j) if sub-square
    # is possible,
    # traverse back horizontally by value val, and check if
    # vertical contiguous
    # 'X'enfing at (i , j-val+1) is greater than equal to
    # val.
    # Similarly, check if traversing back vertically, the
    # horizontal contiguous
    # 'X'ending at (i-val+1, j) is greater than equal to
    # val.
    maxval = 0
    val = 0
 
    for i in range(N):
        for j in range(N):
            val = min(dp[i][j][0],
                      dp[i][j][1])
                       
            if (dp[i][j - val + 1][1] >= val and
                dp[i - val + 1][j][0] >= val):
                maxside[i][j] = val
            else:
                maxside[i][j] = 0
 
            # Store the final answer in maxval
            maxval = max(maxval, maxside[i][j])
 
    # Return the final answe.
    return maxval
 
# Driver code
mat = [ [ 'X', 'O', 'X', 'X', 'X', 'X' ],
        [ 'X', 'O', 'X', 'X', 'O', 'X' ],
        [ 'X', 'X', 'X', 'O', 'O', 'X' ],
        [ 'O', 'X', 'X', 'X', 'X', 'X' ],
        [ 'X', 'X', 'X', 'O', 'X', 'O' ],
        [ 'O', 'O', 'X', 'O', 'O', 'O' ] ]
         
# Function call
print(maximumSubSquare(mat))
 
# This code is contributed by avanitrachhadiya2155

#Output
4
#Time complexity: O(N2) 
#Auxiliary space: O(N2)






#Previous
#Flood fill Algorithm - how to implement fill() in paint?
##Next
#Given a matrix of ‘O’ and ‘X’, replace 'O' with 'X' if surrounded by 'X'
##Related Articles
#1.
#Given a matrix of ‘O’ and ‘X’, replace 'O' with 'X' if surrounded by 'X'
#2.
#Generate a Matrix such that given Matrix elements are equal to Bitwise OR of all corresponding row and column elements of generated Matrix
#3.
#Generate matrix from given Sparse Matrix using Linked List and reconstruct the Sparse Matrix
#4.
#Find the original matrix when largest element in a row and a column are given
#5.
#Find smallest and largest element from square matrix diagonals
#6.
#Find the original matrix from the given AND matrix
#7.
#Check if a given matrix can be converted to another given matrix by row and column exchanges
#8.
#Find size of the largest '+' formed by all ones in a binary matrix
#9.
#Find the largest area rectangular sub-matrix whose sum is equal to k
#10.
#Length of largest common subarray in all the rows of given Matrix