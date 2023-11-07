#Construct Ancestor Matrix from a Given Binary Tree

#Difficulty Level : Hard
#Given a Binary Tree where all values are from 0 to n-1. Construct an ancestor matrix mat[n][n]. Ancestor matrix is defined as below.

#mat[i][j] = 1 if i is ancestor of j
#mat[i][j] = 0, otherwise
#Examples: 

#Input: Root of below Binary Tree.
#          0
#        /   \
#       1     2
#Output: 0 1 1
#        0 0 0 
#        0 0 0 

#Input: Root of below Binary Tree.
#           5
#        /    \
#       1      2
#      /  \    /
#     0    4  3
#Output: 0 0 0 0 0 0 
#        1 0 0 0 1 0 
#        0 0 0 1 0 0 
#        0 0 0 0 0 0 
#        0 0 0 0 0 0 
#        1 1 1 1 1 0
#We strongly recommend you to minimize your browser and try this yourself first.

#Method 1: The idea is to traverse the tree. While traversing, keep track of ancestors in an array. When we visit a node, we add it to ancestor array and consider the corresponding row in the adjacency matrix. We mark all ancestors in its row as 1. Once a node and all its children are processed, we remove the node from ancestor array.

#Below is the implementation of above idea. 

#C++
#Java
#Python3
# Python3 program to construct ancestor
# matrix for given tree.
 
class newnode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
         
# anc[] stores all ancestors of current node.
# This function fills ancestors for all nodes.
# It also returns size of tree. Size of tree 
# is used to print ancestor matrix.
def ancestorMatrixRec(root, anc):
    global mat, MAX
     
    # base case
    if root == None:
        return 0
 
    # Update all ancestors of current node
    data = root.data
    for i in range(len(anc)):
        mat[anc[i]][data] = 1
 
    # Push data to list of ancestors
    anc.append(data)
 
    # Traverse left and right subtrees
    l = ancestorMatrixRec(root.left, anc)
    r = ancestorMatrixRec(root.right, anc)
 
    # Remove data from list the list of ancestors
    # as all descendants of it are processed now.
    anc.pop(-1)
 
    return l + r + 1
 
# This function mainly calls ancestorMatrixRec()
def ancestorMatrix(root):
     
    # Create an empty ancestor array
    anc = []
 
    # Fill ancestor matrix and find
    # size of tree.
    n = ancestorMatrixRec(root, anc)
 
    # Print the filled values
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end = " ")
        print()
 
# Driver Code
MAX = 100
mat = [[0] * MAX for i in range(MAX)]
 
# Construct the following binary tree
#         5
#         / \
#     1     2
#     / \ /
#     0 4 3
root = newnode(5)
root.left = newnode(1)
root.right = newnode(2)
root.left.left = newnode(0)
root.left.right = newnode(4)
root.right.left = newnode(3)
 
ancestorMatrix(root)
 
# This code is contributed by PranchalK
#C#
#Javascript
#Output
#0 0 0 0 0 0 
#1 0 0 0 1 0 
#0 0 0 1 0 0 
#0 0 0 0 0 0 
#0 0 0 0 0 0 
#1 1 1 1 1 0 
#Time complexity of above solution is O(n2).
#Auxiliary Space: O(n2), since n2 extra space has been taken.



#Method 2:

#This method doesn’t use any auxiliary space to store values in the vector. Create a 2D matrix( say M) of the given size. Now the idea is to traverse the tree in PreOrder. While traversing, keep track of the last ancestor. 
#When we visit a node, if the node is NULL return, else assign M[lastAncestorValue][currentNodeValue]=1. 
#Through this, we have the Matrix(M) which keeps tracks of the Lowest Ancestor, Now by applying transitive closure to this Matrix(M), we get the required result.

#Below is the implementation of the above idea.

#C++
#Java
#Python3
# Python3 program to construct ancestor
# matrix for given tree.
size = 6
  
M = [[0 for j in range(size)]
        for i in range(size)]
 
# A binary tree node
class Node:
     
    def __init__(self, data):
         
        self.left = None
        self.right = None
        self.data = data
         
# Helper function to create a new node
def newnode(data):
 
    temp = Node(data)
     
    return temp
 
def printMatrix():
     
    for i in range(size):
        for j in range(size):
            print(M[i][j], end = ' ')
         
        print()    
  
# First PreOrder Traversal
def MatrixUtil(root, index):
     
    if (root == None):
        return
      
    preData = root.data
              
    # Since there is no ancestor for
    # root node, so we doesn't assign
    # it's value as 1           
    if (index == -1):
        index = root.data
    else:
        M[index][preData] = 1   
      
    MatrixUtil(root.left, preData)
    MatrixUtil(root.right, preData)
 
def Matrix(root):
     
    # Call Func MatrixUtil
    MatrixUtil(root, -1)
      
    # Applying Transitive Closure
    # for the given Matrix
    for i in range(size):
        for j in range(size):
            for k in range(size):
                M[j][k] = (M[j][k] or
                          (M[j][i] and
                           M[i][k]))
      
    # Printing Matrix
    printMatrix()
  
# Driver code
if __name__=="__main__":
     
    root = newnode(5)
    root.left = newnode(1)
    root.right = newnode(2)
    root.left.left = newnode(0)
    root.left.right = newnode(4)
    root.right.left = newnode(3)
  
    Matrix(root)
      
# This code is contributed by rutvik_56

#Output
#0 0 0 0 0 0 
#1 0 0 0 1 0 
#0 0 0 1 0 0 
#0 0 0 0 0 0 
#0 0 0 0 0 0 
#1 1 1 1 1 0 
#Time complexity of above solution is O(n2).
#Auxiliary Space: O(n2)

#How to do reverse – construct tree from ancestor matrix? 
#Construct tree from ancestor matrix

#This article is contributed by Aarti_Rathi and Dheeraj Gupta. Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.

#Recommended
#Solve DSA problems on GfG Practice.

#Solve Problems




#Like
#8
#Previous
#Find perimeter of shapes formed with 1s in binary matrix
#Next
#Program for Sudoku Generator
#Related Articles
#1.
#Construct Binary Tree from Ancestor Matrix | Top Down Approach
#2.
#Construct tree from ancestor matrix
#3.
#Lowest Common Ancestor in a Binary Search Tree.
#4.
#Lowest Common Ancestor in a Binary Tree
#5.
#Maximum difference between node and its ancestor in Binary Tree
#6.
#K-th ancestor of a node in Binary Tree
#7.
#Kth ancestor of a node in binary tree | Set 2
#8.
#Lowest Common Ancestor in a Binary Tree | Set 3 (Using RMQ)
#9.
#K-th ancestor of a node in Binary Tree | Set 3
#10.
#Kth ancestor of a node in an N-ary tree using Binary Lifting Technique