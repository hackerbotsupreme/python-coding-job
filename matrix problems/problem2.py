#Program for scalar multiplication of a matrix

#Difficulty Level : Basic

#Given a matrix and a scalar element k, our task is to find out the scalar product of that matrix. 
#Examples: 
 

#Input : mat[][] = {{2, 3}
#                   {5, 4}}
#        k = 5
#Output : 10 15 
#         25 20 
#We multiply 5 with every element.
#
#Input : 1 2 3 
#        4 5 6
#        7 8 9
#        k = 4
#Output :  4 8  12
#          16 20 24
#          28 32 36 
 

#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#The scalar multiplication of a number k(scalar), multiply it on every entry in the matrix. and a matrix A is the matrix kA.
# Python 3 program to find the scalar
# product of a matrix
 
# Size of given matrix
N = 3
 
def scalarProductMat( mat, k):
 
    # scalar element is multiplied
    # by the matrix
    for i in range( N):
        for j in range( N):
            mat[i][j] = mat[i][j] * k    
 
# Driver code
if __name__ == "__main__":
     
    mat = [[ 1, 2, 3 ],
           [ 4, 5, 6 ],
           [ 7, 8, 9 ]]
    k = 4
 
    scalarProductMat(mat, k)
 
    # to display the resultant matrix
    print("Scalar Product Matrix is : ")
    for i in range(N):
        for j in range(N):
            print(mat[i][j], end = " ")
        print()
 
# This code is contributed by ita_c

#Output: 
#Scalar Product Matrix is : 
#4 8 12 
#16 20 24 
#28 32 36
 

#Time Complexity: O(n2),

#Auxiliary Space: O(1), since no extra space has been taken.



