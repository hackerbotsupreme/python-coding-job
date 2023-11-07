#Maximum size rectangle binary sub-matrix with all 1s

#Difficulty Level : Hard
#Given a binary matrix, find the maximum size rectangle binary-sub-matrix with all 1’s. 

#Example: 

#Input:
#0 1 1 0
#1 1 1 1
#1 1 1 1
#1 1 0 0
#Output :
#8
#Explanation : 
#The largest rectangle with only 1's is from 
#(1, 0) to (2, 3) which is
#1 1 1 1
#1 1 1 1 

#Input:
#0 1 1
#1 1 1
#0 1 1      
#Output:
#6
#Explanation : 
#The largest rectangle with only 1's is from 
#(0, 1) to (2, 2) which is
#1 1
#1 1
#1 1
#Recommended Problem
#Max rectangle
#Dynamic Programming
#Stack
#+3 more
#Flipkart
#Amazon
#+6 more
#Solve Problem
#Submission count: 67.6K
#There is already an algorithm discussed a dynamic programming based solution for finding the largest square with 1s. 

#Approach: 

#In this post, an interesting method is discussed that uses largest rectangle under histogram as a subroutine. 

#If the height of bars of the histogram is given then the largest area of the histogram can be found. This way in each row, the largest area of bars of the histogram can be found. To get the largest rectangle full of 1’s, update the next row with the previous row and find the largest area under the histogram, i.e. consider each 1’s as filled squares and 0’s with an empty square and consider each row as the base.

#Illustration: 

#Input :
#0 1 1 0
##1 1 1 1
#1 1 1 1
#1 1 0 0
#Step 1: 
#0 1 1 0  maximum area  = 2
#Step 2:
#row 1  1 2 2 1  area = 4, maximum area becomes 4
#row 2  2 3 3 2  area = 8, maximum area becomes 8
#row 3  3 4 0 0  area = 6, maximum area remains 8
#Algorithm: 



#Run a loop to traverse through the rows.
#Now If the current row is not the first row then update the row as follows, if matrix[i][j] is not zero then matrix[i][j] = matrix[i-1][j] + matrix[i][j].
#Find the maximum rectangular area under the histogram, consider the ith row as heights of bars of a histogram. This can be calculated as given in this article Largest Rectangular Area in a Histogram
#Do the previous two steps for all rows and print the maximum area of all the rows.
#Note: It is strongly recommended to refer to this post first as most of the code is taken from there. 

#Implementation 


# Python3 program to find largest rectangle
# with all 1s in a binary matrix
 
# Finds the maximum area under the
# histogram represented
# by histogram. See below article for details.
 
 
class Solution():
    def maxHist(self, row):
        # Create an empty stack. The stack holds
        # indexes of hist array / The bars stored
        # in stack are always in increasing order
        # of their heights.
        result = []
 
        # Top of stack
        top_val = 0
 
        # Initialize max area in current
        max_area = 0
        # row (or histogram)
 
        area = 0  # Initialize area with current top
 
        # Run through all bars of given
        # histogram (or row)
        i = 0
        while (i < len(row)):
 
            # If this bar is higher than the
            # bar on top stack, push it to stack
            if (len(result) == 0) or (row[result[-1]] <= row[i]):
                result.append(i)
                i += 1
            else:
 
                # If this bar is lower than top of stack,
                # then calculate area of rectangle with
                # stack top as the smallest (or minimum
                # height) bar. 'i' is 'right index' for
                # the top and element before top in stack
                # is 'left index'
                top_val = row[result.pop()]
                area = top_val * i
 
                if (len(result)):
                    area = top_val * (i - result[-1] - 1)
                max_area = max(area, max_area)
 
        # Now pop the remaining bars from stack
        # and calculate area with every popped
        # bar as the smallest bar
        while (len(result)):
            top_val = row[result.pop()]
            area = top_val * i
            if (len(result)):
                area = top_val * (i - result[-1] - 1)
 
            max_area = max(area, max_area)
 
        return max_area
 
    # Returns area of the largest rectangle
    # with all 1s in A
    def maxRectangle(self, A):
 
        # Calculate area for first row and
        # initialize it as result
        result = self.maxHist(A[0])
 
        # iterate over row to find maximum rectangular
        # area considering each row as histogram
        for i in range(1, len(A)):
 
            for j in range(len(A[i])):
 
                # if A[i][j] is 1 then add A[i -1][j]
                if (A[i][j]):
                    A[i][j] += A[i - 1][j]
 
            # Update result if area with current
            # row (as last row) of rectangle) is more
            result = max(result, self.maxHist(A[i]))
 
        return result
 
 
# Driver Code
if __name__ == '__main__':
    A = [[0, 1, 1, 0],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 0, 0]]
    ans = Solution()
 
    print("Area of maximum rectangle is",
          ans.maxRectangle(A))
 
# This code is contributed
# by Aaryaman Sharma
#C#
#Javascript
#Output
#Area of maximum rectangle is 8
#Complexity Analysis:  

#Time Complexity: O(R x C). 
#Only one traversal of the matrix is required, so the time complexity is O(R X C)
#Space Complexity: O(C). 
#Stack is required to store the columns, so space complexity is O(C)
#This article is contributed by Sanjiv Kumar. If you like GeeksforGeeks and would like to contribute, you can also write an article and mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.





#Like
#124
#Previous
#Count number of islands where every island is row-wise and column-wise separated
#Next
#Maximum size square sub-matrix with all 1s
#Related Articles
#1.
#Minimum area such that all submatrix of the size have same maximum value
#2.
#Minimum operations to convert Binary Matrix A to B by flipping submatrix of size K
#3.
#Submatrix of given size with maximum 1's
#4.
#Maximum size rectangle binary sub-matrix with all 1s | Set 2
#5.
#Maximize the binary matrix by flipping submatrix once
#6.
#Queries to count minimum flips required to fill a binary submatrix with 0s only
#7.
#Minimum number of 1s present in a submatrix of given dimensions in a Binary Matrix
#8.
#Smallest submatrix with Kth maximum XOR
#9.
#Maximum value in a matrix which contain intersecting concentric submatrix
#10.
#Find Maximum Length Of A Square Submatrix Having Sum Of Elements At-Most K
#Article Contributed By :