#Minimum Initial Points to Reach Destination

#Difficulty Level : Hard
#Last Updated : 20 Dec, 2022
#Read
#Discuss(100)
#Courses
#Practice
#Video
#Given a grid with each cell consisting of positive, negative or no points i.e, zero points. We can move across a cell only if we have positive points ( > 0 ). Whenever we pass through a cell, points in that cell are added to our overall points. We need to find minimum initial points to reach cell (m-1, n-1) from (0, 0).

#Constraints :

#From a cell (i, j) we can move to (i+1, j) or (i, j+1).
#We cannot move from (i, j) if your overall points at (i, j) is <= 0.
#We have to reach at (n-1, m-1) with minimum positive points i.e., > 0.
#Example:

#Input: points[m][n] = { {-2, -3,   3}, 
#                        {-5, -10,  1}, 
#                        {10,  30, -5} 
#                      };
#Output: 7
#Explanation: 
#7 is the minimum value to reach destination with 
#positive throughout the path. Below is the path.#

#(0,0) -> (0,1) -> (0,2) -> (1, 2) -> (2, 2)

#We start from (0, 0) with 7, we reach(0, 1) 
#with 5, (0, 2) with 2, (1, 2) with 5, (2, 2)
#with and finally we have 1 point (we needed 
#greater than 0 points at the end).
#We strongly recommend that you click here and practice it, before moving on to the solution.
#At the first look, this problem looks similar Max/Min Cost Path, but maximum overall points gained will not guarantee the minimum initial points. Also, it is compulsory in the current problem that the points never drops to zero or below. For instance, Suppose following two paths exists from source to destination cell.

#We can solve this problem through bottom-up table filling dynamic programming technique.

#To begin with, we should maintain a 2D array dp of the same size as the grid, where dp[i][j] represents the minimum points that guarantees the continuation of the journey to destination before entering the cell (i, j). It’s but obvious that dp[0][0] is our final solution. Hence, for this problem, we need to fill the table from the bottom right corner to left top.
#Now, let us decide minimum points needed to leave cell (i, j) (remember we are moving from bottom to up). There are only two paths to choose: (i+1, j) and (i, j+1). Of course we will choose the cell that the player can finish the rest of his journey with a smaller initial points. Therefore we have: min_Points_on_exit = min(dp[i+1][j], dp[i][j+1]) 
#Now we know how to compute min_Points_on_exit, but we need to fill the table dp[][] to get the solution in dp[0][0].

#How to compute dp[i][j]?



#The value of dp[i][j] can be written as below.

#dp[i][j] = max(min_Points_on_exit – points[i][j], 1)
#Let us see how above expression covers all cases.

#If points[i][j] == 0, then nothing is gained in this cell; the player can leave the cell with the same points as he enters the room with, i.e. dp[i][j] = min_Points_on_exit.
#If points[i][j] < 0, then the player must have points greater than min_Points_on_exit before entering (i, j) in order to compensate for the points lost in this cell. The minimum amount of compensation is ” – points[i][j] “, so we have dp[i][j] = min_Points_on_exit – points[i][j].
#If points[i][j] > 0, then the player could enter (i, j) with points as little as min_Points_on_exit – points[i][j]. since he could gain “points[i][j]” points in this cell. However, the value of min_Points_on_exit – points[i][j] might drop to 0 or below in this situation. When this happens, we must clip the value to 1 in order to make sure dp[i][j] stays positive: dp[i][j] = max(min_Points_on_exit – points[i][j], 1).
#Finally return dp[0][0] which is our answer.

#Below is the implementation of above algorithm.

#C++14
#Java
#Python3
# Python3 program to find minimum initial
# points to reach destination
import math as mt
R = 3
C = 3
 
 
def minInitialPoints(points):
    '''
    dp[i][j] represents the minimum initial
    points player should have so that when
    starts with cell(i, j) successfully
    reaches the destination cell(m-1, n-1)
    '''
    dp = [[0 for x in range(C + 1)]
          for y in range(R + 1)]
    m, n = R, C
 
    if points[m - 1][n - 1] > 0:
        dp[m - 1][n - 1] = 1
    else:
        dp[m - 1][n - 1] = abs(points[m - 1][n - 1]) + 1
    '''
    Fill last row and last column as base
    to fill entire table
    '''
    for i in range(m - 2, -1, -1):
        dp[i][n - 1] = max(dp[i + 1][n - 1] -
                           points[i][n - 1], 1)
    for i in range(n - 2, -1, -1):
        dp[m - 1][i] = max(dp[m - 1][i + 1] -
                           points[m - 1][i], 1)
    '''
    fill the table in bottom-up fashion
    '''
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            min_points_on_exit = min(dp[i + 1][j],
                                     dp[i][j + 1])
            dp[i][j] = max(min_points_on_exit -
                           points[i][j], 1)
 
    return dp[0][0]
 
 
# Driver code
points = [[-2, -3, 3],
          [-5, -10, 1],
          [10, 30, -5]]
 
print("Minimum Initial Points Required:",
      minInitialPoints(points))
 
 
# This code is contributed by
# Mohit kumar 29 (IIIT gwalior)
C#
#Javascript
#PHP
#Output
#Minimum Initial Points Required: 7
#Time Complexity: O(R*C)
#Auxiliary Space: O(R*C)

#This article is contributed by Gaurav Ahirwar. Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.

#Recommended
#Solve DSA problems on GfG Practice.

#Solve Problems




#Like
#70
#Previous
#Print all palindromic paths from top left to bottom right in a matrix
#Next
#Number of paths with exactly k coins
#Related Articles
#1.
#Find the minimum cost to reach destination using a train
#2.
#Minimum steps to reach a destination
#3.
#Minimum cells required to reach destination with jumps equal to cell values
#4.
#Count number of ways to reach destination in a Maze
#5.
#Number of decisions to reach destination
#6.
#Count number of ways to reach destination in a maze
#7.
#Count number of ways to reach destination in a Maze using BFS
#8.
#Check if it is possible to reach destination in even number of steps in an Infinite Matrix
#9.
#Count all possible walks from a source to a destination with exactly k edges
#10.
#Source to destination in 2-D path with fixed sized jumps
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
#nitin mittal
#PrathamKohli
#Mr.Lazy
#mohit kumar 29
#jit_t
#shruti456rawal
##shivamanandrj9
#hardikkoriintern
#rkbhola5
#sbchaudhari581
#vforviksvy5
#Article Tags :
#Microsoft
#Samsung
#Dynamic Programming
#Matrix
#Practice Tags :
#Microsoft
#Samsung
#Dynamic Programming
#Matrix
#Improve Article
#Report Issue