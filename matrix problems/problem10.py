#Sum of middle row and column in Matrix

#Difficulty Level : Basic

#Given an integer matrix of odd dimensions (3 * 3, 5 * 5). then the task is to find the sum of the middle row & column elements. 

#Examples: 

#Input :  2 5 7
#         3 7 2
#         5 6 9
#Output : Sum of middle row = 12
#         Sum of middle column = 18

#Input :  1 3 5 6 7
#         3 5 3 2 1
#         1 2 3 4 5
#         7 9 2 1 6
#         9 1 5 3 2
#Output : Sum of middle row = 15
#         Sum of middle column = 18
#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#Implementation:

#CPP
#Java
#Python3
# Python program to find sum of
# middle row and column in matrix
 
  
def middlesum(mat,n):
  
    row_sum = 0
    col_sum = 0
      
    # loop for sum of row
    for i in range(n):
        row_sum += mat[n // 2][i]
      
    print("Sum of middle row = ",
                     row_sum)
      
    # loop for sum of column
    for i in range(n):
        col_sum += mat[i][n // 2]
      
    print("Sum of middle column = ",
                            col_sum)
 
# Driver code
mat= [[2, 5, 7],
     [3, 7, 2],
     [5, 6, 9]]
      
middlesum(mat, 3)
 
# This code is contributed
# by Anant Agarwal.
#C#
#PHP
#Javascript
#Output
#Sum of middle row = 12
#Sum of middle column = 18
#Time Complexity : O(n) 
#Auxiliary Space: O(1) using constant space to initialize row_sum and col_sum variables, since no extra space has been taken.
#
#Using Stl:

#    Here we use accumulate function to do it.



#C++
#include <iostream>
#include<bits/stdc++.h>
#using namespace std;
 
#int main() {
#    vector<vector<int>>v{{2, 5, 7},
#                         {3, 7, 2},
#                         {5, 6, 9}};
#    int n=v.size();
#    cout<<"The sum of all the element in middle row : "<<endl;
#    cout<<accumulate(v[n/2].begin(),v[n/2].end(),0)<<endl;
#    for(int i=0;i<n;i++)
#        for(int j=i+1;j<n;j++)
#            swap(v[i][j],v[j][i]);
#   cout<<"The sum of all the element in middle column : "<<endl;
#   cout<<accumulate(v[n/2].begin(),v[n/2].end(),0);
#    return 0;
#}
#Output
#The sum of all the element in middle row : 
#12
#The sum of all the element in middle column : 
#18
#The accumulated value of f applications. Complexity: O(n×k), where n is the distance from first to last , O(k) is complexity of f function.

#Time Complexity: O(n*k).
#Auxiliary Space : O(k) 