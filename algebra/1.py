Program to add two polynomials

Difficulty Level : Easy
Last Updated : 27 Jan, 2023
Read
Discuss
Courses
Practice
Video
Given two polynomials represented by two arrays, write a function that adds given two polynomials. 
Example: 
 

Input:  A[] = {5, 0, 10, 6} #set format{} and list format are []
        B[] = {1, 2, 4} 
Output: sum[] = {6, 2, 14, 6}

The first input array represents "5 + 0x^1 + 10x^2 + 6x^3"
The second array represents "1 + 2x^1 + 4x^2" 
And Output is "6 + 2x^1 + 14x^2 + 6x^3"
We strongly recommend to minimize your browser and try this yourself first. 
Addition is simpler than multiplication of polynomials. We initialize result as one of the two polynomials, then we traverse the other polynomial and add all terms to the result.
 

add(A[0..m-1], B[0..n01])
1) Create a sum array sum[] of size equal to maximum of 'm' and 'n'
2) Copy A[] to sum[].
3) Traverse array B[] and do following for every element B[i]
          sum[i] = sum[i] + B[i]
4) Return sum[].
The following is implementation of above algorithm. 
 

C++
Java
Python3
# Simple Python 3 program to add two
# polynomials
 
# A utility function to return maximum
# of two integers
 
# A[] represents coefficients of first polynomial
# B[] represents coefficients of second polynomial
# m and n are sizes of A[] and B[] respectively
def add(A, B, m, n):
 
    size = max(m, n);
    sum = [0 for i in range(size)]
 
    # Initialize the product polynomial
     
    for i in range(0, m, 1):
        sum[i] = A[i]
 
    # Take ever term of first polynomial
    for i in range(n):
        sum[i] += B[i]
 
    return sum
 
# A utility function to print a polynomial
def printPoly(poly, n):
    for i in range(n):
        print(poly[i], end = "")#The end parameter in the print function is used to add any string. At the end of the output of the print statement in python. By default, the print function ends with a newline. Passing the whitespace to the end parameter (end=' ') indicates that the end character has to be identified by whitespace and not a newline.
        if (i != 0):#[anything here]-- computer will treat it like a list and poly[i] --- now computer will treat it like an index 
            print("x^", i, end = "")
        if (i != n - 1):
            print(" + ", end = "")
 
# Driver Code
if __name__ == '__main__':
     
    # The following array represents
    # polynomial 5 + 10x^2 + 6x^3
    A = [5, 0, 10, 6]
 
    # The following array represents
    # polynomial 1 + 2x + 4x^2
    B = [1, 2, 4]
    m = len(A)
    n = len(B)
 
    print("First polynomial is")
    printPoly(A, m)
    print("\n", end = "")
    print("Second polynomial is")
    printPoly(B, n)
    print("\n", end = "")
    sum = add(A, B, m, n)
    size = max(m, n)
 
    print("sum polynomial is")
    printPoly(sum, size)
     
# This code is contributed by
# Sahil_Shelangia
C#
PHP
Javascript
Output: 

First polynomial is
5 + 0x^1 + 10x^2 + 6x^3
Second polynomial is
1 + 2x^1 + 4x^2
Sum polynomial is
6 + 2x^1 + 14x^2 + 6x^3
Time complexity of the above algorithm and program is O(m+n) where m and n are orders of two given polynomials.

Auxiliary Space: O(max(m, n))
This article is contributed by Harsh. Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above
 

Recommended
Solve DSA problems on GfG Practice.

Solve Problems


Like
Previous
Generate Pythagorean Triplets
Next
Multiply two polynomials
Related Articles
1.
Polynomials in One Variable - Polynomials | Class 9 Maths
2.
C++ Program For Adding Two Polynomials Using Linked List
3.
Java Program For Adding Two Polynomials Using Linked List
4.
Adding two polynomials using Circular Linked List
5.
Multiplication of two polynomials using Linked list
6.
Multiply two polynomials
7.
Adding two polynomials using Linked List
8.
Remainder Theorem - Polynomials | Class 9 Maths
9.
Types of Polynomials
10.
Add two integers of different base and represent sum in smaller base of the two
Article Contributed By :
https://media.geeksforgeeks.org/auth/avatar.png
GeeksforGeeks
Vote for difficulty
Current difficulty : Easy
Easy
Normal
Medium
Hard
Expert
Improved By :
29AjayKumar
sahilshelangia
Code_Mech
Chandan_Kumar
shubham_singh
rohitsingh07052
simmytarika5
subham348
Article Tags :
maths-polynomial
Mathematical
Practice Tags :
Mathematic



#trial 1:
#take input and produce a polynomial equation
I=(1,2,3,4,5);
j=len(I);
for i in range(j):
    i+=i*"x"^I[i];#TypeError: unsupported operand type(s) for ^: 'str' and 'int'
    print(i)#the problem i  m facing is i need to figure out the syntzx  that fits with my assumed syntax 
    
    
#trial 2
#take input and produce a polynomial equation
#I=(1,2,3,4,5)
#i need to print 1.1+2x+3x^2+4x^3+5x^4
#                2.1x+2x^1+3x^3+4x^4+5x^5
I=(1,2,3,4,5);
j=len(I);    



 