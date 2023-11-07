#Check if all rows of a matrix are circular rotations of each other

#Difficulty Level : Medium
#Given a matrix of n*n size, the task is to find whether all rows are circular rotations of each other or not. 

#Examples: 

#Input: mat[][] = 1, 2, 3
#                 3, 1, 2
#                 2, 3, 1
#Output:  Yes
#All rows are rotated permutation
#of each other.

#Input: mat[3][3] = 1, 2, 3
#                   3, 2, 1
#                   1, 3, 2
#Output:  No
#Explanation : As 3, 2, 1 is not a rotated or 
#circular permutation of 1, 2, 3
#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#The idea is based on below article. 
#A Program to check if strings are rotations of each other or not

#Steps :  

#Create a string of first row elements and concatenate the string with itself so that string search operations can be efficiently performed. Let this string be str_cat.
#Traverse all remaining rows. For every row being traversed, create a string str_curr of current row elements. If str_curr is not a substring of str_cat, return false.
#Return true.
#Below is the implementation of above steps. 

#C++
#Java
#Python3
# Python3 program to check if all rows
# of a matrix are rotations of each other
 
MAX = 1000
 
# Returns true if all rows of mat[0..n-1][0..n-1]
# are rotations of each other.
def isPermutedMatrix(mat, n) :
     
    # Creating a string that contains
    # elements of first row.
    str_cat = ""
    for i in range(n) :
        str_cat = str_cat + "-" + str(mat[0][i])
 
    # Concatenating the string with itself
    # so that substring search operations
    # can be performed on this
    str_cat = str_cat + str_cat
 
    # Start traversing remaining rows
    for i in range(1, n) :
         
        # Store the matrix into vector
        # in the form of strings
        curr_str = ""
         
        for j in range(n) :
            curr_str = curr_str + "-" + str(mat[i][j])
 
        # Check if the current string is present
        # in the concatenated string or not
        if (str_cat.find(curr_str)) :
            return True
             
    return False
 
# Driver code
if __name__ == "__main__" :
    n = 4
    mat = [[1, 2, 3, 4],
           [4, 1, 2, 3],
           [3, 4, 1, 2],
           [2, 3, 4, 1]]
     
    if (isPermutedMatrix(mat, n)):
        print("Yes")
    else :
        print("No")
         
# This code is contributed by Ryuga
#C#
#PHP
#Javascript
#Output
#Yes
#Time complexity: O(n3) 
#Auxiliary Space: O(n), since n extra space has been taken.

#This article is contributed by Sahil Chhabra (akku). If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks. 



#Like
#Previous
#Move matrix elements in given direction and add elements with same value
#Next
#Minimum flip required to make Binary Matrix symmetric
#Related Articles
#1.
#C++ Program to Check if all rows of a matrix are circular rotations of each other
#2.
#Java Program to Check if all rows of a matrix are circular rotations of each other
#3.
#Python3 Program to Check if all rows of a matrix are circular rotations of each other
#4.
#Php Program to Check if all rows of a matrix are circular rotations of each other
#5.
#Javascript Program to Check if all rows of a matrix are circular rotations of each other
#6.
#Check if two numbers are bit rotations of each other or not
#7.
#Check if strings are rotations of each other or not | Set 2
#8.
#C++ Program to Check if strings are rotations of each other or not | Set 2
##9.
##Java Program to Check if strings are rotations of each other or not | Set 2
#10.
#Python3 Program to Check if strings are rotations of each other or not | Set 2