#Divide and Conquer | Set 5 (Strassen’s Matrix Multiplication)

#Difficulty Level : Medium
#Last Updated : 21 Nov, 2022
#Read
#Discuss(40+)
#Courses
#Practice
#Video
#Given two square matrices A and B of size n x n each, find their multiplication matrix. 

#Naive Method: Following is a simple way to multiply two matrices. 

#C++
#
#Java
#Python3
def multiply(A, B, C):
 
    for i in range(N):
     
        for j in range( N):
         
            C[i][j] = 0
            for k in range(N):
             
                C[i][j] += A[i][k]*B[k][j]
 
# this code is contributed by shivanisinghss2110
#C#
#Javascript
#Time Complexity of above method is O(N3). 



#Divide and Conquer :

#Following is simple Divide and Conquer method to multiply two square matrices. 

#Divide matrices A and B in 4 sub-matrices of size N/2 x N/2 as shown in the below diagram. 
#Calculate following values recursively. ae + bg, af + bh, ce + dg and cf + dh. 
#strassen_new

#Implementation:



#C++
#include <bits/stdc++.h>
#using namespace std;
 
#define ROW_1 4
#define COL_1 4
 
#define ROW_2 4
#define COL_2 4
 
void print(string display, vector<vector<int> > matrix,
           int start_row, int start_column, int end_row,
           int end_column)
{
    cout << endl << display << " =>" << endl;
    for (int i = start_row; i <= end_row; i++) {
        for (int j = start_column; j <= end_column; j++) {
            cout << setw(10);
            cout << matrix[i][j];
        }
        cout << endl;
    }
    cout << endl;
    return;
}
 
void add_matrix(vector<vector<int> > matrix_A,
                vector<vector<int> > matrix_B,
                vector<vector<int> >& matrix_C,
                int split_index)
{
    for (auto i = 0; i < split_index; i++)
        for (auto j = 0; j < split_index; j++)
            matrix_C[i][j]
                = matrix_A[i][j] + matrix_B[i][j];
}
 
vector<vector<int> >
multiply_matrix(vector<vector<int> > matrix_A,
                vector<vector<int> > matrix_B)
{
    int col_1 = matrix_A[0].size();
    int row_1 = matrix_A.size();
    int col_2 = matrix_B[0].size();
    int row_2 = matrix_B.size();
 
    if (col_1 != row_2) {
        cout << "\nError: The number of columns in Matrix "
                "A  must be equal to the number of rows in "
                "Matrix B\n";
        return {};
    }
 
    vector<int> result_matrix_row(col_2, 0);
    vector<vector<int> > result_matrix(row_1,
                                       result_matrix_row);
 
    if (col_1 == 1)
        result_matrix[0][0]
            = matrix_A[0][0] * matrix_B[0][0];
    else {
        int split_index = col_1 / 2;
 
        vector<int> row_vector(split_index, 0);
        vector<vector<int> > result_matrix_00(split_index,
                                              row_vector);
        vector<vector<int> > result_matrix_01(split_index,
                                              row_vector);
        vector<vector<int> > result_matrix_10(split_index,
                                              row_vector);
        vector<vector<int> > result_matrix_11(split_index,
                                              row_vector);
 
        vector<vector<int> > a00(split_index, row_vector);
        vector<vector<int> > a01(split_index, row_vector);
        vector<vector<int> > a10(split_index, row_vector);
        vector<vector<int> > a11(split_index, row_vector);
        vector<vector<int> > b00(split_index, row_vector);
        vector<vector<int> > b01(split_index, row_vector);
        vector<vector<int> > b10(split_index, row_vector);
        vector<vector<int> > b11(split_index, row_vector);
 
        for (auto i = 0; i < split_index; i++)
            for (auto j = 0; j < split_index; j++) {
                a00[i][j] = matrix_A[i][j];
                a01[i][j] = matrix_A[i][j + split_index];
                a10[i][j] = matrix_A[split_index + i][j];
                a11[i][j] = matrix_A[i + split_index]
                                    [j + split_index];
                b00[i][j] = matrix_B[i][j];
                b01[i][j] = matrix_B[i][j + split_index];
                b10[i][j] = matrix_B[split_index + i][j];
                b11[i][j] = matrix_B[i + split_index]
                                    [j + split_index];
            }
 
        add_matrix(multiply_matrix(a00, b00),
                   multiply_matrix(a01, b10),
                   result_matrix_00, split_index);
        add_matrix(multiply_matrix(a00, b01),
                   multiply_matrix(a01, b11),
                   result_matrix_01, split_index);
        add_matrix(multiply_matrix(a10, b00),
                   multiply_matrix(a11, b10),
                   result_matrix_10, split_index);
        add_matrix(multiply_matrix(a10, b01),
                   multiply_matrix(a11, b11),
                   result_matrix_11, split_index);
 
        for (auto i = 0; i < split_index; i++)
            for (auto j = 0; j < split_index; j++) {
                result_matrix[i][j]
                    = result_matrix_00[i][j];
                result_matrix[i][j + split_index]
                    = result_matrix_01[i][j];
                result_matrix[split_index + i][j]
                    = result_matrix_10[i][j];
                result_matrix[i + split_index]
                             [j + split_index]
                    = result_matrix_11[i][j];
            }
 
        result_matrix_00.clear();
        result_matrix_01.clear();
        result_matrix_10.clear();
        result_matrix_11.clear();
        a00.clear();
        a01.clear();
        a10.clear();
        a11.clear();
        b00.clear();
        b01.clear();
        b10.clear();
        b11.clear();
    }
    return result_matrix;
}
 
int main()
{
    vector<vector<int> > matrix_A = { { 1, 1, 1, 1 },
                                      { 2, 2, 2, 2 },
                                      { 3, 3, 3, 3 },
                                      { 2, 2, 2, 2 } };
 
    print("Array A", matrix_A, 0, 0, ROW_1 - 1, COL_1 - 1);
 
    vector<vector<int> > matrix_B = { { 1, 1, 1, 1 },
                                      { 2, 2, 2, 2 },
                                      { 3, 3, 3, 3 },
                                      { 2, 2, 2, 2 } };
 
    print("Array B", matrix_B, 0, 0, ROW_2 - 1, COL_2 - 1);
 
    vector<vector<int> > result_matrix(
        multiply_matrix(matrix_A, matrix_B));
 
    print("Result Array", result_matrix, 0, 0, ROW_1 - 1,
          COL_2 - 1);
}
 
// Time Complexity: O(n^3)
// Code Contributed By: lucasletum
Java
C#
Output
Array A =>
         1         1         1         1
         2         2         2         2
         3         3         3         3
         2         2         2         2


Array B =>
         1         1         1         1
         2         2         2         2
         3         3         3         3
         2         2         2         2


Result Array =>
         8         8         8         8
        16        16        16        16
        24        24        24        24
        16        16        16        16
In the above method, we do 8 multiplications for matrices of size N/2 x N/2 and 4 additions. Addition of two matrices takes O(N2) time. So the time complexity can be written as 

T(N) = 8T(N/2) + O(N2)  

From Master's Theorem, time complexity of above method is O(N3)
which is unfortunately same as the above naive method.
Simple Divide and Conquer also leads to O(N3), can there be a better way? 

In the above divide and conquer method, the main component for high time complexity is 8 recursive calls. The idea of Strassen’s method is to reduce the number of recursive calls to 7. Strassen’s method is similar to above simple divide and conquer method in the sense that this method also divide matrices to sub-matrices of size N/2 x N/2 as shown in the above diagram, but in Strassen’s method, the four sub-matrices of result are calculated using following formulae.
 

stressen_formula_new_new

Time Complexity of Strassen’s Method

Addition and Subtraction of two matrices takes O(N2) time. So time complexity can be written as 

T(N) = 7T(N/2) +  O(N2)

From Master's Theorem, time complexity of above method is 
O(NLog7) which is approximately O(N2.8074)
Generally Strassen’s Method is not preferred for practical applications for following reasons. 

The constants used in Strassen’s method are high and for a typical application Naive method works better. 
For Sparse matrices, there are better methods especially designed for them. 
The submatrices in recursion take extra space. 
Because of the limited precision of computer arithmetic on noninteger values, larger errors accumulate in Strassen’s algorithm than in Naive Method
Implementation:

C++
Python3
# Version 3.6
 
import numpy as np
 
def split(matrix):
    """
    Splits a given matrix into quarters.
    Input: nxn matrix
    Output: tuple containing 4 n/2 x n/2 matrices corresponding to a, b, c, d
    """
    row, col = matrix.shape
    row2, col2 = row//2, col//2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]
 
def strassen(x, y):
    """
    Computes matrix product by divide and conquer approach, recursively.
    Input: nxn matrices x and y
    Output: nxn matrix, product of x and y
    """
 
    # Base case when size of matrices is 1x1
    if len(x) == 1:
        return x * y
 
    # Splitting the matrices into quadrants. This will be done recursively
    # until the base case is reached.
    a, b, c, d = split(x)
    e, f, g, h = split(y)
 
    # Computing the 7 products, recursively (p1, p2...p7)
    p1 = strassen(a, f - h) 
    p2 = strassen(a + b, h)       
    p3 = strassen(c + d, e)       
    p4 = strassen(d, g - e)       
    p5 = strassen(a + d, e + h)       
    p6 = strassen(b - d, g + h) 
    p7 = strassen(a - c, e + f) 
 
    # Computing the values of the 4 quadrants of the final matrix c
    c11 = p5 + p4 - p2 + p6 
    c12 = p1 + p2          
    c21 = p3 + p4           
    c22 = p1 + p5 - p3 - p7 
 
    # Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
 
    return c
Output
Array A =>
         1         1         1         1
         2         2         2         2
         3         3         3         3
         2         2         2         2


Array B =>
         1         1         1         1
         2         2         2         2
         3         3         3         3
         2         2         2         2


Result Array =>
         8         8         8         8
        16        16        16        16
        24        24        24        24
        16        16        16        16
Easy way to remember Strassen’s Matrix Equation
 

References: 
Introduction to Algorithms 3rd Edition by Clifford Stein, Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest 
Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above
 

Recommended
Solve DSA problems on GfG Practice.

Solve Problems




Like
73
Previous
Write program to calculate pow(x, n)
Next
Convex Hull using Divide and Conquer Algorithm
Related Articles
1.
Karatsuba algorithm for fast multiplication using Divide and Conquer algorithm
2.
Merge K sorted arrays | Set 3 ( Using Divide and Conquer Approach )
3.
Maximum Sum SubArray using Divide and Conquer | Set 2
4.
Introduction to Divide and Conquer Algorithm - Data Structure and Algorithm Tutorials
5.
Search in a Row-wise and Column-wise Sorted 2D Array using Divide and Conquer algorithm
6.
Difference between Greedy Algorithm and Divide and Conquer Algorithm
7.
Comparison among Greedy, Divide and Conquer and Dynamic Programming algorithm
8.
Tiling Problem using Divide and Conquer algorithm
9.
The Skyline Problem using Divide and Conquer algorithm
10.
Longest Common Prefix using Divide and Conquer Algorithm
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
PrayushDawda
rrrtnx
anikaseth98
shivanisinghss2110
rutvik_56
noob2000
amartyaghoshgfg
lucasletum
shruti456rawal
hardikkoriintern
phasing17
Article Tags :
Divide and Conquer
Matrix
Practice Tags :
Divide and Conquer
Matrix
Improve Article
Report Issue