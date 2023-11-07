Program to find correlation coefficient

Difficulty Level : Medium
Last Updated : 23 Nov, 2022
Read
Discuss
Courses
Practice
Video
Given two array elements and we have to find the correlation coefficient between two arrays. The correlation coefficient is an equation that is used to determine the strength of the relation between two variables. The correlation coefficient is sometimes called as cross-correlation coefficient. The correlation coefficient always lies between -1 to +1 where -1 represents X and Y are negatively correlated and +1 represents X and Y are positively correlated.

r=\frac{n\left(\sum x y\right)-\left(\sum x\right)\left(\sum y\right)}{\sqrt{\left[n \sum x^{2}-\left(\sum x\right)^{2}\right]\left[n \Sigma y^{2}-\left(\sum y\right)^{2}\right]}}

Where r is the correlation coefficient.

\begin{array}{|c|c|} \hline X & Y \\ \hline 15 & 25 \\ \hline 18 & 25 \\ \hline 21 & 27 \\ \hline 24 & 31 \\ \hline 27 & 32 \\ \hline \Sigma X=105 & \sum Y=140 \end{array}  [Tex]\begin{array}{|c|c|c|} \hline X^{*} Y & X^{*} X & Y^{*} Y \\ \hline 375 & 225 & 625 \\ \hline 450 & 324 & 625 \\ \hline 567 & 441 & 729 \\ \hline 744 & 576 & 961 \\ \hline 864 & 729 & 1024 \\ \hline \sum X^{*} Y=3000 & \sum X^{*} X=2295 & \sum Y^{*} Y=3964 \\ \hline \end{array} [/Tex]
 

Correlation coefficient 
= (5 * 3000 - 105 * 140) 
     / sqrt((5 * 2295 - 1052)*(5*3964 - 1402))
= 300 / sqrt(450 * 220) = 0.953463
Examples :

Input : X[] = {43, 21, 25, 42, 57, 59}
        Y[] = {99, 65, 79, 75, 87, 81}
Output : 0.529809

Input : X[] = {15, 18, 21, 24, 27};
        Y[] = {25, 25, 27, 31, 32}
Output : 0.953463
C++
Java
Python
# Python Program to find correlation coefficient.
import math
 
# function that returns correlation coefficient.
def correlationCoefficient(X, Y, n) :
    sum_X = 0
    sum_Y = 0
    sum_XY = 0
    squareSum_X = 0
    squareSum_Y = 0
     
     
    i = 0
    while i < n :
        # sum of elements of array X.
        sum_X = sum_X + X[i]
         
        # sum of elements of array Y.
        sum_Y = sum_Y + Y[i]
         
        # sum of X[i] * Y[i].
        sum_XY = sum_XY + X[i] * Y[i]
         
        # sum of square of array elements.
        squareSum_X = squareSum_X + X[i] * X[i]
        squareSum_Y = squareSum_Y + Y[i] * Y[i]
         
        i = i + 1
      
    # use formula for calculating correlation
    # coefficient.
    corr = (float)(n * sum_XY - sum_X * sum_Y)/
           (float)(math.sqrt((n * squareSum_X -
           sum_X * sum_X)* (n * squareSum_Y -
           sum_Y * sum_Y)))
    return corr
     
# Driver function
X = [15, 18, 21, 24, 27]
Y = [25, 25, 27, 31, 32]
      
# Find the size of array.
n = len(X)
 
# Function call to correlationCoefficient.
print ('{0:.6f}'.format(correlationCoefficient(X, Y, n)))
 
# This code is contributed by Nikita Tiwari.
C#
PHP
Javascript
Output
0.953463
Time complexity: O(n), where n is the size of given arrays
Auxiliary space: O(1)



Recommended
Solve DSA problems on GfG Practice.

Solve Problems




Like
7
Next
Program for Muller Method
Related Articles
1.
Python | Kendall Rank Correlation Coefficient
2.
Probability plot correlation coefficient
3.
Program for Spearman's Rank Correlation
4.
Program for Coefficient of variation
5.
Pearson Product Moment Correlation
6.
Spearman's Rank Correlation
7.
Space and time efficient Binomial Coefficient
8.
Clustering Coefficient in Graph Theory
9.
Maximum binomial coefficient term value
10.
Fibonomial coefficient and Fibonomial triangle
Article Contributed By :
https://media.geeksforgeeks.org/auth/avatar.png
GeeksforGeeks
Vote for difficulty
Current difficulty : Medium
Easy
Normal
Medium
Hard
Expert
Improved By :
jit_t
susmitakundugoaldanga
kumargaurav97520
Article Tags :
ML-Statistics
statistical-algorithms
Mathematical
Practice Tags :
Mathematical