#Find size of the largest ‘+’ formed by all ones in a binary matrix

#Difficulty Level : Hard
#Last Updated : 04 Jul, 2022
#Read
#Discuss
#Courses
#Practice
#Video
#Given a N X N binary matrix, find the size of the largest ‘+’ formed by all 1s.

#Example: 



#For above matrix, largest ‘+’ would be formed by highlighted part of size 17.

#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#The idea is to maintain four auxiliary matrices left[][], right[][], top[][], bottom[][] to store consecutive 1’s in every direction. For each cell (i, j) in the input matrix, we store below information in these four matrices –

#left(i, j) stores maximum number of
#consecutive 1's to the left of cell (i, j) 
#including cell (i, j).

#right(i, j) stores maximum number of
#consecutive 1's to the right of cell (i, j) 
#including cell (i, j).

#top(i, j) stores maximum number of
#consecutive 1's at top of cell (i, j) 
#including cell (i, j).

#bottom(i, j) stores maximum number of
#consecutive 1's at bottom of cell (i, j) 
#including cell (i, j).
#After computing value for each cell of above matrices, the largest + would be formed by a cell of input matrix that has maximum value by considering minimum of (left(i, j), right(i, j), top(i, j), bottom(i, j) )

#We can use Dynamic Programming to compute the total amount of consecutive 1’s in every direction. 



#if mat(i, j) == 1
#    left(i, j) = left(i, j - 1) + 1
#else left(i, j) = 0

#if mat(i, j) == 1
#    top(i, j) = top(i - 1, j) + 1;
#else
#    top(i, j) = 0;

#if mat(i, j) == 1
#    bottom(i, j) = bottom(i + 1, j) + 1;
#else
#    bottom(i, j) = 0;    

#if mat(i, j) == 1
#    right(i, j) = right(i, j + 1) + 1;
#else
#    right(i, j) = 0;
#Below is the implementation of above idea :


# Python 3 program to find the size
# of the largest '+' formed by all
# 1's in given binary matrix
 
# size of binary square matrix
N = 10
 
# Function to find the size of the
# largest '+' formed by all 1's in
# given binary matrix
def findLargestPlus(mat):
 
    # left[j][j], right[i][j], top[i][j] and
    # bottom[i][j] store maximum number of
    # consecutive 1's present to the left,
    # right, top and bottom of mat[i][j] including
    # cell(i, j) respectively
    left = [[0 for x in range(N)]
               for y in range(N)]
    right = [[0 for x in range(N)]
                for y in range(N)]
    top = [[0 for x in range(N)]
              for y in range(N)]
    bottom = [[0 for x in range(N)]
                 for y in range(N)]
 
    # initialize above four matrix
    for i in range(N):
         
        # initialize first row of top
        top[0][i] = mat[0][i]
 
        # initialize last row of bottom
        bottom[N - 1][i] = mat[N - 1][i]
 
        # initialize first column of left
        left[i][0] = mat[i][0]
 
        # initialize last column of right
        right[i][N - 1] = mat[i][N - 1]
 
    # fill all cells of above four matrix
    for i in range(N):
        for j in range(1, N):
             
            # calculate left matrix (filled
            # left to right)
            if (mat[i][j] == 1):
                left[i][j] = left[i][j - 1] + 1
            else:
                left[i][j] = 0
 
            # calculate top matrix
            if (mat[j][i] == 1):
                top[j][i] = top[j - 1][i] + 1
            else:
                top[j][i] = 0
 
            # calculate new value of j to calculate
            # value of bottom(i, j) and right(i, j)
            j = N - 1 - j
 
            # calculate bottom matrix
            if (mat[j][i] == 1):
                bottom[j][i] = bottom[j + 1][i] + 1
            else:
                bottom[j][i] = 0
 
            # calculate right matrix
            if (mat[i][j] == 1):
                right[i][j] = right[i][j + 1] + 1
            else:
                right[i][j] = 0
 
            # revert back to old j
            j = N - 1 - j
 
    # n stores length of longest '+'
    # found so far
    n = 0
 
    # compute longest +
    for i in range(N):
        for j in range(N):
             
            # find minimum of left(i, j),
            # right(i, j), top(i, j), bottom(i, j)
            l = min(min(top[i][j], bottom[i][j]),
                    min(left[i][j], right[i][j]))
 
            # largest + would be formed by
            # a cell that has maximum value
            if(l > n):
                n = l
 
    # 4 directions of length n - 1 and 1
    # for middle cell
    if (n):
        return 4 * (n - 1) + 1
 
    # matrix contains all 0's
    return 0
 
# Driver Code
if __name__=="__main__":
     
    # Binary Matrix of size N
    mat = [ [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
            [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
            [ 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
            [ 0, 0, 0, 0, 1, 0, 0, 1, 0, 0 ],
            [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 0 ],
            [ 1, 0, 0, 0, 1, 0, 0, 1, 0, 1 ],
            [ 1, 0, 1, 1, 1, 1, 0, 0, 1, 1 ],
            [ 1, 1, 0, 0, 1, 0, 1, 0, 0, 1 ],
            [ 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ]]
 
    print(findLargestPlus(mat))
 
# This code is contributed by ChitraNayal

#Output
#17
#Time complexity of above solution is O(n2).
#Auxiliary space used by the program is O(n2).

#This article is contributed by Aditya Goel. If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.







#Return previous element in an expanding matrix
#Related Articles
#1.
#Check if all rows of a Binary Matrix have all ones placed adjacently or not
#2.
#Maximum number of ones in a N*N matrix with given constraints
#3.
#Find trace of matrix formed by adding Row-major and Column-major order of same matrix
#4.
#Find perimeter of shapes formed with 1s in binary matrix
#5.
#Maximum size rectangle binary sub-matrix with all 1s
#6.
#Check whether row or column swaps produce maximum size binary sub-matrix with all 1s
#7.
#Maximum size rectangle binary sub-matrix with all 1s | Set 2
#8.
#Minimum swaps needed to convert given Binary Matrix A to Binary Matrix B
#9.
#Generate a Matrix such that given Matrix elements are equal to Bitwise OR of all corresponding row and column elements of generated Matrix
#10.
#Given an n x n square matrix, find sum of all sub-squares of size k x k
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
##Improved By :
#KRV
#ukasp
#Sach_Code
#avanitrachhadiya2155
#kothavvsaakash
#hardikkoriintern
#Article Tags :
#Matrix
#Practice Tags :
#Matrix