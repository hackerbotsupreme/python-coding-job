#Print a given matrix in spiral form

#Difficulty Level : Medium
#------------------------------------------------------------------------

#Examples: 

#Input:  {{1,    2,   3,   4},
#              {5,    6,   7,   8},
#             {9,   10,  11,  12},
#            {13,  14,  15,  16 }}
#Output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 
#Explanation: The output is matrix in spiral format. 


#Input: { {1,   2,   3,   4,  5,   6},
#           {7,   8,   9,  10,  11,  12},
#          {13,  14,  15, 16,  17,  18}}

#Output: 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
#Explanation: The output is matrix in spiral format.
#-----------------------------------------------------------------------
#Print a given matrix in spiral form using the simulation approach:
#To solve the problem follow the below idea:

#Draw the path that the spiral makes. We know that the path should turn clockwise whenever it would go out of bounds or into a cell that was previously visited



#Follow the given steps to solve the problem:

#Let the array have R rows and C columns
#seen[r] denotes that the cell on the r-th row and c-th column was previously visited. Our current position is (r, c), facing direction di, and we want to visit R x C total cells.
#As we move through the matrix, our candidate’s next position is (cr, cc). 
#If the candidate is in the bounds of the matrix and unseen, then it becomes our next position; otherwise, our next position is the one after performing a clockwise turn
#Below is the implementation of the above approach:

# python3 program for the above approach
  
  
def spiralOrder(matrix):
    ans = []
  
    if (len(matrix) == 0):
        return ans
  
    m = len(matrix)
    n = len(matrix[0])
    seen = [[0 for i in range(n)] for j in range(m)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    x = 0
    y = 0
    di = 0
  
    # Iterate from 0 to R * C - 1
    for i in range(m * n):
        ans.append(matrix[x][y])
        seen[x][y] = True
        cr = x + dr[di]
        cc = y + dc[di]
  
        if (0 <= cr and cr < m and 0 <= cc and cc < n and not(seen[cr][cc])):
            x = cr
            y = cc
        else:
            di = (di + 1) % 4
            x += dr[di]
            y += dc[di]
    return ans
  
  
# Driver code
if __name__ == "__main__":
    a = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
  
    # Function call
    for x in spiralOrder(a):
        print(x, end=" ")
    print()
#Output
#1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 
#Time Complexity: O(N), where N is the total number of elements in the input matrix. We add every element in the matrix to our fi
#---------------------------------------------------------------------------------
#Print a given matrix in spiral form by dividing the matrix into cycles:
#To solve the problem follow the below idea:

#The problem can be solved by dividing the matrix into loops or squares or boundaries. It can be seen that the elements of the outer loop are printed first in a clockwise manner then the elements of the inner loop are printed. So printing the elements of a loop can be solved using four loops that print all the elements. Every ‘for’ loop defines a single-direction movement along with the matrix. The first for loop represents the movement from left to right, whereas the second crawl represents the movement from top to bottom, the third represents the movement from the right to left, and the fourth represents the movement from bottom to up

#Follow the given steps to solve the problem:

#Create and initialize variables k – starting row index, m – ending row index, l – starting column index, n – ending column index
#Run a loop until all the squares of loops are printed.
#In each outer loop traversal print the elements of a square in a clockwise manner.
#Print the top row, i.e. Print the elements of the kth row from column index l to n, and increase the count of k.
#Print the right column, i.e. Print the last column or n-1th column from row index k to m and decrease the count of n.
#Print the bottom row, i.e. if k < m, then print the elements of the m-1th row from column n-1 to l and decrease the count of m
#Print the left column, i.e. if l < n, then print the elements of lth column from m-1th row to k and increase the count of l.
#Below is the implementation of the above approach: 

# Python3 program to print
# given matrix in spiral form
  
  
def spiralPrint(m, n, a):
    k = 0
    l = 0
  
    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''
  
    while (k < m and l < n):
  
        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            print(a[k][i], end=" ")
  
        k += 1
  
        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            print(a[i][n - 1], end=" ")
  
        n -= 1
  
        # Print the last row from
        # the remaining rows
        if (k < m):
  
            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end=" ")
  
            m -= 1
  
        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=" ")
  
            l += 1
  
  
# Driver Code
a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
  
R = 4
C = 4
  
# Function Call
spiralPrint(R, C, a)
  
# This code is contributed by Nikita Tiwari.
#Output
#1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 
#Time Complexity: O(M*N). To traverse the matrix O(M*M) time is required.
#Auxiliary Space: O(1). No extra space is required.
#--------------------------------------------------------------

#Print a given matrix in a spiral using recursion:
#To solve the problem follow the below idea:

#The above problem can be solved by printing the boundary of the Matrix recursively. In each recursive call, we decrease the dimensions of the matrix. The idea of printing the boundary or loops is the same

#Follow the given steps to solve the problem:

#create a recursive function that takes a matrix and some variables (k – starting row index, m – ending row index, l – starting column index, n – ending column index) as parameters
#Check the base cases (starting index is less than or equal to the ending index) and print the boundary elements in a clockwise manner
#Print the top row, i.e. Print the elements of the kth row from column index l to n, and increase the count of k
#Print the right column, i.e. Print the last column or n-1th column from row index k to m and decrease the count of n
#Print the bottom row, i.e. if k > m, then print the elements of m-1th row from column n-1 to l and decrease the count of m
#Print the left column, i.e. if l < n, then print the elements of the lth column from m-1th row to k and increase the count of l
#Call the function recursively with the values of starting and ending indices of rows and columns
#Below is the implementation of the above approach: 

# Python3 program for the above approach
  
# Function for printing matrix in spiral
# form i, j: Start index of matrix, row
# and column respectively m, n: End index
# of matrix row and column respectively
  
  
def printdata(arr, i, j, m, n):
  
    # If i or j lies outside the matrix
    if (i >= m or j >= n):
        return
  
    # Print First Row
    for p in range(i, n):
        print(arr[i][p], end=" ")
  
    # Print Last Column
    for p in range(i + 1, m):
        print(arr[p][n - 1], end=" ")
  
    # Print Last Row, if Last and
    # First Row are not same
    if ((m - 1) != i):
        for p in range(n - 2, j - 1, -1):
            print(arr[m - 1][p], end=" ")
  
    # Print First Column, if Last and
    # First Column are not same
    if ((n - 1) != j):
        for p in range(m - 2, i, -1):
            print(arr[p][j], end=" ")
  
    printdata(arr, i + 1, j + 1, m - 1, n - 1)
  
  
# Driver code
if __name__ == "__main__":
    R = 4
    C = 4
    arr = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]
  
    # Function Call
    printdata(arr, 0, 0, R, C)
  
# This code is contributed by avsadityavardhan
#`Output
#1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 
#Time Complexity: O(M*N). To traverse the matrix O(m*n) time is required.
#Auxiliary Space: O(1). No extra space is required.

#Print a given matrix in spiral using DFS:
#To solve the problem follow the below idea:

#Another recursive approach is to consider DFS movement within the matrix (right->down->left->up->right->..->end). We do this by modifying the matrix itself such that when DFS algorithm visits each matrix cell it’s changed to a value which cannot be contained within the matrix. The DFS algorithm is terminated when it visits a cell such that all of its surrounding cells are already visited. The direction of the DFS search is controlled by a variable. 

#Follow the given steps to solve the problem:

#create a DFS function that takes matrix, cell indices, and direction
#checks are cell indices pointing to a valid cell (that is, not visited and in bounds)? if not, skip this cell
#print cell value
#mark matrix cell pointed by indicates as visited by changing it to a value not supported in the matrix
#check are surrounding cells valid? if not stop the algorithm, else continue
#if the direction is given right then check, if the cell to the right is valid. if so, DFS to the right cell given the steps above, else, change the direction to down and DFS downwards given the steps above
#else, if the direction given is down then check, if the cell to the down is valid. if so, DFS to the cell below given the steps above, else, change the direction to left and DFS leftwards given the steps above
#else, if the direction given is left then check, if the cell to the left is valid. if so, DFS to the left cell given the steps above, else, change the direction to up and DFS upwards given the steps above
#else, if the direction given is up then check, if the cell to the up is valid. if so, DFS to the upper cell given the steps above, else, change the direction to right and DFS rightwards given the steps above
#Below is an implementation of the above approach: 

# Python3 program for the above approach
  
R = 4
C = 4
  
  
def isInBounds(i, j):
    global R
    global C
    if (i < 0 or i >= R or j < 0 or j >= C):
        return False
    return True
  
# Check if the position is blocked
  
  
def isBlocked(matrix, i, j):
    if (not isInBounds(i, j)):
        return True
    if (matrix[i][j] == -1):
        return True
  
    return False
  
# DFS code to traverse spirally
  
  
def spirallyDFSTravserse(matrix, i, j, Dir, res):
    if (isBlocked(matrix, i, j)):
        return
  
    allBlocked = True
    for k in range(-1, 2, 2):
        allBlocked = allBlocked and isBlocked(
            matrix, k + i, j) and isBlocked(matrix, i, j + k)
  
    res.append(matrix[i][j])
    matrix[i][j] = -1
    if (allBlocked):
        return
  
    # dir: 0 - right, 1 - down, 2 - left, 3 - up
    nxt_i = i
    nxt_j = j
    nxt_dir = Dir
    if (Dir == 0):
        if (not isBlocked(matrix, i, j + 1)):
            nxt_j += 1
        else:
            nxt_dir = 1
            nxt_i += 1
  
    elif(Dir == 1):
        if (not isBlocked(matrix, i + 1, j)):
            nxt_i += 1
        else:
            nxt_dir = 2
            nxt_j -= 1
  
    elif(Dir == 2):
        if (not isBlocked(matrix, i, j - 1)):
            nxt_j -= 1
        else:
            nxt_dir = 3
            nxt_i -= 1
  
    elif(Dir == 3):
        if (not isBlocked(matrix, i - 1, j)):
            nxt_i -= 1
        else:
            nxt_dir = 0
            nxt_j += 1
  
    spirallyDFSTravserse(matrix, nxt_i, nxt_j, nxt_dir, res)
  
# To traverse spirally
  
  
def spirallyTraverse(matrix):
    res = []
    spirallyDFSTravserse(matrix, 0, 0, 0, res)
    return res
  
  
# Driver code
if __name__ == "__main__":
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
  
    # Function Call
    res = spirallyTraverse(a)
    print(*res)
  
# This code is contributed by rag2127
#Output
#1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 
#Time Complexity: O(M*N). To traverse the matrix O(M*N) time is required.
#Auxiliary Space: O(1). No extra space is required (without consideration of the stack used by the recursion). 