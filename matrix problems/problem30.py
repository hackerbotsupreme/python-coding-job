#Find all permuted rows of a given row in a matrix

#Difficulty Level : Easy
#We are given an m*n matrix of positive integers and a row number. The task is to find all rows in given matrix which are permutations of given row elements. It is also given that values in every row are distinct.

#Examples:  

#Input : mat[][] = {{3, 1, 4, 2}, 
#                   {1, 6, 9, 3},
#                   {1, 2, 3, 4},
#                   {4, 3, 2, 1}}
#        row = 3    
#Output: 0, 2
#Rows at indexes 0 and 2 are permutations of
#row at index 3. 
#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#A simple solution is to one by one sort all rows and check all rows. If any row is completely equal to the given row, that means the current row is a permutation of the given row. The time complexity for this approach will be O(m*n log n).

#An efficient approach is to use hashing. Simply create a hash set for the given row. After hash set creation, traverse through the remaining rows, and for every row check if all of its elements are present in the hash set or not.  

#Implementation:


# Python program to find all
# permutations of a given row
 
# Function to find all
# permuted rows of a given row r
def permutatedRows(mat, m, n, r):
 
 
    # Creating an empty set
    s=set()
 
    # Count frequencies of
    # elements in given row r
    for j in range(n):
        s.add(mat[r][j])   
 
    # Traverse through all remaining rows
    for i in range(m):
 
        # we do not need to check
        # for given row r
        if i == r:
            continue
 
        # initialize hash i.e
        # count frequencies
        # of elements in row i
        for j in range(n):
            if mat[i][j] not in s:
 
                # to avoid the case when last
                # element does not match
                j = j - 2
                break;
        if j + 1 != n:
            continue
        print(i)
             
     
 
# Driver program to run the case
m = 4
n = 4
r = 3
mat = [[3, 1, 4, 2],
       [1, 6, 9, 3],
       [1, 2, 3, 4],
       [4, 3, 2, 1]]
 
permutatedRows(mat, m, n, r)
 
# This code is contributed
# by Upendra Singh Bartwal.

#Output
#0, 2, 
#Time complexity: O(m*n) 
#Auxiliary space: O(n)



#Another approach to the solution is using the Standard Template Library(STL):  


# Python3 program to find all permutations of a given row
MAX = 100
 
# This function checks if two arrays are permutations of each other
def is_permutation(a, b):
    return sorted(a) == sorted(b)
     
# Function to find all permuted rows of a given row r
def permutatedRows(mat, m, n, r):
     
    for i in range(min(m, r)):
        if is_permutation(mat[i], mat[r]):
            print(i, end = ", ")
 
# Driver program to run the case
m = 4
n = 4
r = 3;
mat =  [[ 3, 1, 4, 2], [1, 6, 9, 3], [1, 2, 3, 4], [4, 3, 2, 1]];
             
permutatedRows(mat, m, n, r);
 
# This code is contributed by phasing17

#Output
#0,2,
#Time Complexity: O(m*n), where m is the number of rows and n is the size of each row. We need to compare each row with the given row, so the time complexity is O(m*n).
#Auxiliary Space : O(1). No extra space is used.

#Exercise : 
#Extend the above solution to work for an input matrix where all elements of a row don’t have to be distinct. (Hit: We can use Hash Map instead of a Hash Set)

#This article is contributed by Shashank Mishra ( Gullu ). If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.
 





#Like
#7
#Next
#Change the array into a permutation of numbers from 1 to n
#Related Articles
#1.
#Find a common element in all rows of a given row-wise sorted matrix
#2.
#Generate a Matrix such that given Matrix elements are equal to Bitwise OR of all corresponding row and column elements of generated Matrix
#3.
#Find row and column pair in given Matrix with equal row and column sum
#4.
#Replace diagonal elements in each row of given Matrix by Kth smallest element of that row
#5.
#Check if any row of the matrix can be converted to the elements present in the target row
#6.
#Check if a given matrix can be converted to another given matrix by row and column exchanges
#7.
#Print all possible paths from the first row to the last row in a 2D array
#8.
#Find trace of matrix formed by adding Row-major and Column-major order of same matrix
#9.
#Find sum of all elements in a matrix except the elements in row and/or column of given cell?
#10.
#Find product of GCDs of all possible row-column pair of given Matrix