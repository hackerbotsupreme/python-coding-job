#Find pairs with given sum such that elements of pair are in different rows

#Difficulty Level : Medium


#Given a matrix of distinct values and a sum. The task is to find all the pairs in a given matrix whose summation is equal to the given sum. Each element of a pair must be from different rows i.e; the pair must not lie in the same row.

#Examples:  

#Input : mat[4][4] = {{1, 3, 2, 4},
#                     {5, 8, 7, 6},
#                     {9, 10, 13, 11},
#                     {12, 0, 14, 15}}
#        sum = 11
#Output: (1, 10), (3, 8), (2, 9), (4, 7), (11, 0) 
#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#Method 1 (Simple):

#A simple solution for this problem is to, one by one, take each element of all rows and find pairs starting from the next immediate row in the matrix.

#C++
#Java
#Python3
# Python program to find a pair with given sum such that
# every element of pair is in different rows.
 
# Function to find pair for given sum in matrix
def pair_sum(mat, sum):
    count = 0
    m = len(mat)
    n = len(mat[0])
    for i in range(m):
        for j in range(i + 1, m):
            for k in range(n):
                for l in range(n):
                    if mat[i][k] + mat[j][l] == sum:
                        print(f"({mat[i][k]}, {mat[j][l]}), ")
    return count
 
sum = 11
mat = [[1, 3, 2, 4],
       [5, 8, 7, 6],
       [9, 10, 13, 11],
       [12, 0, 14, 15]]
pair_sum(mat, sum)
 
# This code is contributed by vikramshrisath177.
#Javascript
#Output
#(3, 8), (4, 7), (1, 10), (2, 9), (11, 0), 
#Time Complexity: O(m2*n2), where m and n are the numbers of rows and columns of the given matrix respectively.
#Auxiliary Space: O(1)

#Method 2 (Use Sorting)



#Sort all the rows in ascending order. The time complexity for this preprocessing will be O(n2 logn).
#Now we will select each row one by one and find pair elements in the remaining rows after the current row.
#Take two iterators, left and right. left iterator points left corner of the current i’th row and right iterator points right corner of the next j’th row in which we are going to find a pair of elements.
#If mat[i][left] + mat[j][right] < sum then left++ i.e; move in i’th row towards the right corner, otherwise right++ i.e; move in j’th row towards the left corner
#Implementation:


# Python 3 program to find a pair with
# given sum such that every element of
# pair is in different rows.
MAX = 100
 
# Function to find pair for given
# sum in matrix mat[][] --> given matrix
# n --> order of matrix
# sum --> given sum for which we
# need to find pair
def pairSum(mat, n, sum):
 
    # First sort all the rows
    # in ascending order
    for i in range(n):
        mat[i].sort()
 
    # Select i'th row and find pair for
    # element in i'th row in j'th row
    # whose summation is equal to given sum
    for i in range(n - 1):
        for j in range(i + 1, n):
            left = 0
            right = n - 1
            while (left < n and right >= 0):
                if ((mat[i][left] + mat[j][right]) == sum):
                    print( "(", mat[i][left],
                           ", ", mat[j][right], "), ",
                                            end = " ")
                    left += 1
                    right -= 1
                 
                else:
                    if ((mat[i][left] +
                         mat[j][right]) < sum):
                        left += 1
                    else:
                        right -= 1
 
# Driver Code
if __name__ == "__main__":
    n = 4
    sum = 11
    mat = [[1, 3, 2, 4],
           [5, 8, 7, 6],
           [9, 10, 13, 11],
           [12, 0, 14, 15]]
    pairSum(mat, n, sum)
 
# This code is contributed
# by ChitraNayal

#Output
#(3, 8), (4, 7), (1, 10), (2, 9), (11, 0), 
#Time complexity : O(n2logn + n^3) 
#Auxiliary space : O(1)

#Method 3 (Hashing)  

#Create an empty hash table and store all elements of the matrix in the hash as keys and their locations as values.
#Traverse the matrix again to check for every element whether its pair exists in the hash table or not. If it exists, then compare row numbers. If row numbers are not the same, then print the pair.
#Implementation:


# Python3 program to find pairs with given sum such
# the two elements of pairs are from different rows
MAX = 100
 
# Function to find pair for given sum in matrix
  # mat[][] --> given matrix
  # n --> order of matrix
  # sum --> given sum for which we need to find pair
def pairSum(mat, n, sum):
     
    # Create a hash and store all elements of matrix
    # as keys, and row and column numbers as values
    hm = {}
     
    for i in range(n):
        for j in range(n):
            hm[mat[i][j]] = [i, j]
     
    # Traverse the matrix again to check for every
    # element whether its pair exists or not.
    for i in range(n):
        for j in range(n):
           
            # Look for remaining sum in hash
            remSum = sum - mat[i][j]
             
            # If an element with value equal to remaining sum exists
            if remSum in hm:
               
                # Find row and column numbers of element with
                # value equal to remaining sum.
                p=hm[remSum]
                row = p[0]
                col = p[1]
                 
                # If row number of pair is not same as current
                # row, then print it as part of result.
                # Second condition is there to make sure that a
                # pair is printed only once.
                if (row != i and row > i):
                    print("(" , mat[i][j] , "," , mat[row][col] , "), ", end="")
                     
# Driver code
n = 4
sum = 11
mat = [[1, 3, 2, 4],
                   [5, 8, 7, 6],
                   [9, 10, 13, 11],
                   [12, 0, 14, 15]]
pairSum(mat, n, sum)
 
# This code is contributed by patel2127

#Output
#(8, 3), (7, 4), (9, 2), (10, 1), (0, 11), 
#One important thing is, when we traverse a matrix, a pair may be printed twice. To make sure that a pair is printed only once, we check if the row number of other elements picked from the hash table is more than the row number of the current element.

#Time Complexity: O(n2) under the assumption that hash table inserts and search operations take O(1) time.
#Auxiliary Space: O(n2) because using HashMap

#This article is contributed by Shashank Mishra ( Gullu ). If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.





#Like
#7
#Previous
#Minimum Index Sum for Common Elements of Two Lists
#Next
#Common elements in all rows of a given matrix
#Related Articles
#1.
#Maximize remainder of sum of a pair of array elements with different parity modulo K
#2.
#Minimum count of rows between rows containing X and Y respectively
#3.
#Find pair of rows in a binary matrix that has maximum bit difference
#4.
#Count ways to remove pairs from a matrix such that remaining elements can be grouped in vertical or horizontal pairs
#5.
#Pair with given product | Set 1 (Find if any pair exists)
#6.
#Count of pairs in Array such that bitwise AND of XOR of pair and X is 0
#7.
#Minimum sum of all absolute differences of same column elements in adjacent rows in a given Matrix
#8.
#Maximize count of pairs whose Bitwise AND exceeds Bitwise XOR by replacing such pairs with their Bitwise AND
#9.
#Find three element from different three arrays such that a + b + c = sum
#10.
#Count all pairs of rows and columns which are equal