Program to find the mid-point of a line

Difficulty Level : Basic
Last Updated : 12 Jun, 2022
Read
Discuss
Courses
Practice
Video
Given two coordinates of a line starting is (x1,y1) and ending is (x2,y2) find out the mid-point of a line. 
Examples : 
 

Input  : x1 = –1, y1 = 2, 
         x2 = 3, y2 = –6
Output : 1,–2

Input  : x1 = 6.4, y1 = 3 
         x2 = –10.7, y2 = 4
Output : –2.15, 3.5
 

Recommended: Please try your approach on {IDE} first, before moving on to the solution.
 



The Midpoint Formula: The midpoint of two points, (x1, y2) and (x2, y2) is the point M found by the following formula: M = ((x1+x2)/2 , (y1+y2)/2)
 

C++
Java
Python3
# Python3 program to find
# the midpoint of a line
 
# Function to find the
# midpoint of a line
def midpoint(x1, x2, y1, y2):
 
    print((x1 + x2) // 2, " , ",
                 (y1 + y2) // 2)
  
# Driver Code
x1, y1, x2, y2 = -1, 2, 3, -6
midpoint(x1, x2, y1, y2)
 
# This code is contributed by Anant Agarwal.
C#
PHP
Javascript
Output : 

1 , -2
Time complexity: O(1) since performing only constant operations



Auxiliary Space: O(1)

 





Like
2
Previous
Reflection of a point about a line in C++
Next
Sum of Manhattan distances between all pairs of points
Related Articles
1.
Find coordinates of the triangle given midpoint of each side
2.
Midpoint ellipse drawing algorithm
3.
Print level order traversal line by line | Set 1
4.
Level order traversal line by line | Set 2 (Using Two Queues)
5.
Slope of the line parallel to the line with the given slope
6.
Level order traversal line by line | Set 3 (Using One Queue)
7.
Equation of straight line passing through a given point which bisects it into two equal line segments
8.
Equation of a straight line passing through a point and making a given angle with a given line
9.
Program to find line passing through 2 Points
10.
Program to find slope of a line
Article Contributed By :
https://media.geeksforgeeks.org/auth/avatar.png
jaingyayak
@jaingyayak
Vote for difficulty
Current difficulty : Basic
Easy
Normal
Medium
Hard
Expert
Improved By :
jit_t
souravghosh0416
technophpfij
Article Tags :
DSA
Geometric
School Programming
Practice Tags :
Geometric
Improve Article
Report Issue