#Find the number of islands using DFS

#Difficulty Level : Medium

#Given a binary 2D matrix, find the number of islands. A group of connected 1s forms an island. For example, the below matrix contains 5 islands.

#Example: 

#Input: mat[][] = {{1, 1, 0, 0, 0},
#                           {0, 1, 0, 0, 1},
#                           {1, 0, 0, 1, 1},
#                          {0, 0, 0, 0, 0},
#                         {1, 0, 1, 0, 0}}
#Output: 5

#This is a variation of the standard problem: “Counting the number of connected components in an undirected graph”. 


#Before we go to the problem, let us understand what is a connected component. A connected component of an undirected graph is a subgraph in which every two vertices are connected to each other by a path(s), and which is connected to no other vertices outside the subgraph. 
#For example, the graph shown below has three connected components. 
 

#Find the number of islands
 

#Recommended Problem
#Find the number of islands
#DFS
#Graph
#+2 more
#Paytm
#Flipkart
#+17 more
#Solve Problem
#Submission count: 1.3L
#A graph where all vertices are connected with each other has exactly one connected component, consisting of the whole graph. Such a graph with only one connected component is called a Strongly Connected Graph.
#This problem can be easily solved by applying DFS() on each component. In each DFS() call, a component or a sub-graph is visited. We will call DFS on the next un-visited component. The number of calls to DFS() gives the number of connected components. BFS can also be used.



#What is an island? 
#A group of connected 1s forms an island. For example, the below matrix contains 4 islands

#island

#Recommended Practice
#Find the number of islands
#Try It!
#Finding the number of islands using an additional Matrix:
#The idea is to keep an additional matrix to keep track of the visited nodes in the given matrix, and perform DFS to find the total number of islands

#Follow the steps below to solve the problem:

#Initialize a boolean matrix visited of the size of the given matrix to false.
#Initialize count = 0, to store the answer.
#Traverse a loop from 0 till ROW
#Traverse a nested loop from 0 to COL
#If the value of the current cell in the given matrix is 1 and is not visited
#Call DFS function
#Initialize rowNbr[] = { -1, -1, -1, 0, 0, 1, 1, 1 } and colNbr[] = { -1, 0, 1, -1, 1, -1, 0, 1 } for the neighbour cells.
#Mark the current cell as visited
#Run a loop from 0 till 8 to traverse the neighbor
#If the neighbor is safe to visit and is not visited
#Call DFS recursively on the neighbor.
#Increment count by 1
#Return count as the final answer.
#Below is the code implementation of the above approach:


# Program to count islands in boolean 2D matrix
class Graph:
 
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g
 
    # A function to check if a given cell
    # (row, col) can be included in DFS
    def isSafe(self, i, j, visited):
        # row number is in range, column number
        # is in range and value is 1
        # and not yet visited
        return (i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j])
 
    # A utility function to do DFS for a 2D
    # boolean matrix. It only considers
    # the 8 neighbours as adjacent vertices
 
    def DFS(self, i, j, visited):
 
        # These arrays are used to get row and
        # column numbers of 8 neighbours
        # of a given cell
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]
 
        # Mark this cell as visited
        visited[i][j] = True
 
        # Recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)
 
    # The main function that returns
    # count of islands in a given boolean
    # 2D matrix
 
    def countIslands(self):
        # Make a bool array to mark visited cells.
        # Initially all cells are unvisited
        visited = [[False for j in range(self.COL)]for i in range(self.ROW)]
 
        # Initialize count as 0 and traverse
        # through the all cells of
        # given matrix
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet,
                # then new island found
                if visited[i][j] == False and self.graph[i][j] == 1:
                    # Visit all cells in this island
                    # and increment island count
                    self.DFS(i, j, visited)
                    count += 1
 
        return count
 
 
graph = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]
 
 
row = len(graph)
col = len(graph[0])
 
g = Graph(row, col, graph)
 
print("Number of islands is:")
print(g.countIslands())
 
# This code is contributed by Neelam Yadav

#Output
#Number of islands is: 5
#Time complexity: O(ROW x COL), where ROW is the number of rows and COL is the number of columns in the given matrix.
#Auxiliary Space: O(ROW x COL), for creating an additional visited matrix.

#Finding the number of islands using DFS:
#The idea is to modify the given matrix, and perform DFS to find the total number of islands

#Follow the steps below to solve the problem:

#Initialize count = 0, to store the answer.
#Traverse a loop from 0 till ROW
#Traverse a nested loop from 0 to COL
#If the value of the current cell in the given matrix is 1
#Increment count by 1
#Call DFS function
#If the cell exceeds the boundary or the value at the current cell is 0
#Return.
#Update the value at the current cell as 0.
#Call DFS on the neighbor recursively
#Return count as the final answer.
#Below is the code implementation of the above approach:


# Program to count islands in boolean 2D matrix
class Graph:
 
    def __init__(self, row, col, graph):
        self.ROW = row
        self.COL = col
        self.graph = graph
 
    # A utility function to do DFS for a 2D
    # boolean matrix. It only considers
    # the 8 neighbours as adjacent vertices
    def DFS(self, i, j):
        if i < 0 or i >= len(self.graph) or j < 0 or j >= len(self.graph[0]) or self.graph[i][j] != 1:
            return
 
        # mark it as visited
        self.graph[i][j] = -1
 
        # Recur for 8 neighbours
        self.DFS(i - 1, j - 1)
        self.DFS(i - 1, j)
        self.DFS(i - 1, j + 1)
        self.DFS(i, j - 1)
        self.DFS(i, j + 1)
        self.DFS(i + 1, j - 1)
        self.DFS(i + 1, j)
        self.DFS(i + 1, j + 1)
 
    # The main function that returns
    # count of islands in a given boolean
    # 2D matrix
    def countIslands(self):
        # Initialize count as 0 and traverse
        # through the all cells of
        # given matrix
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet,
                # then new island found
                if self.graph[i][j] == 1:
                    # Visit all cells in this island
                    # and increment island count
                    self.DFS(i, j)
                    count += 1
 
        return count
 
 
graph = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]
 
 
row = len(graph)
col = len(graph[0])
 
g = Graph(row, col, graph)
 
print("Number of islands is:", g.countIslands())
 
# This code is contributed by Shivam Shrey
#C#
#Javascript
#Output
#Number of islands is: 5
#Time complexity: O(ROW x COL), where ROW is the number of rows and COL is the number of columns in the given matrix.
#Auxiliary Space: O(ROW * COL), as to do DFS we need extra auxiliary stack space.

#Using Extra O(n*m) Space:

#      Approach:#

#        in this approach we are traversing over matrix and if the current element is equal to one and not visited already than we mark all connect(mark visit) element/point as visted and increment count (cnt) by one.

#C++14
#include <iostream>
#include<bits/stdc++.h>
#using namespace std;
 
#int n,m;
#//valid row and column checker.
bool check(int i,int j){
  return i>=0&&j>=0&&i<n&&j<m;
}
 
void mark_component(vector<vector<int>>&v,vector<vector<bool>>&vis,int i,int j){
   if(!check(i,j))return;
   vis[i][j]=1;
   //marking(connecting all possible part of single island.
   if (v[i][j] == 1) {
        v[i][j] = 0;
        mark_component(v,vis,i+1,j);
        mark_component(v,vis,i-1,j);
        mark_component(v,vis,i,j+1);
        mark_component(v,vis,i,j-1);
        mark_component(v,vis,i+1,j+1);
        mark_component(v,vis,i-1,j-1);
        mark_component(v,vis,i+1,j-1);
        mark_component(v,vis,i-1,j+1);
    }
}
 
int main() {
    vector<vector<int>>v{{ 1, 1, 0, 0, 0 },
                         { 0, 1, 0, 0, 1 },
                         { 1, 0, 0, 1, 1 },
                         { 0, 0, 0, 0, 0 },
                         { 1, 0, 1, 0, 1 }};
    n=v.size();
    m=v[0].size();
   int cnt=0;
  //visit vector.
   vector<vector<bool>>vis(n,vector<bool>(m,0));
   for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){
      if(!vis[i][j]&&v[i][j]==1){
         ++cnt;
         mark_component(v,vis,i,j);
       }
     }
   }
   cout<<"The number of islands in the matrix are :"<<endl;
   cout<<cnt<<endl;
  //code by Sanket Gode
    return 0;
}
Output
The number of islands in the matrix are :
5
Time complexity: O(n*m).
Auxiliary Space: O(n*m).

Find the number of Islands | Set 2 (Using Disjoint Set) 
Islands in a graph using BFS





#Like
#170
#Previous
#Transitive closure of a graph
#Next
#Euler Circuit in a Directed Graph
#Related Articles
#1.
#Find the number of Islands using Disjoint Set
#2.
#Find the number of distinct islands in a 2D matrix
#3.
#Find number of closed islands in given Matrix
#4.
#Count number of islands where every island is row-wise and column-wise separated
#5.
#Minimum number of Water to Land conversion to make two islands connected in a Grid
#6.
#Number of Islands after changing given cell for K queries
#7.
#Minimum number of Water to Land conversion to make two islands connected in a Grid | Set 2
#8.
#Islands in a graph using BFS
#9.
#Distance between closest pair of islands
#10.
#Calculate number of nodes in all subtrees | Using 