#Majority Element
#Difficulty Level : Medium
#-------------------------------------------------------
#Find the majority element in the array. A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element). 

#Examples : 

#Input : A[]={3, 3, 4, 2, 4, 4, 2, 4, 4}
#Output : 4
#Explanation: The frequency of 4 is 5 which is greater than the half of the size of the array size. 

#Input : A[] = {3, 3, 4, 2, 4, 4, 2, 4}
#Output : No Majority Element
#Explanation: There is no element whose frequency is greater than the half of the size of the array size.
#-----------------------------------------------


#Naive Approach: 
#The basic solution is to have two loops and keep track of the maximum count for all different elements. If the maximum count becomes greater than n/2 then break the loops and return the element having the maximum count. If the maximum count doesn’t become more than n/2 then the majority element doesn’t exist.

#Illustration:

#arr[] = {3, 4, 3, 2, 4, 4, 4, 4}, n = 8



#For i = 0:

#count = 0
#Loop over the array, whenever an element is equal to arr[i] (is 3), increment count
#count of arr[i] is 2, which is less than n/2, hence it can’t be majority element.
#For i = 1:

#count = 0
#Loop over the array, whenever an element is equal to arr[i] (is 4), increment count
#count of arr[i] is 5, which is greater than n/2 (i.e 4), hence it will be majority element.
#Hence, 4 is the majority element.

#Follow the steps below to solve the given problem:

#Create a variable to store the max count, count = 0
#Traverse through the array from start to end.
#For every element in the array run another loop to find the count of similar elements in the given array.
#If the count is greater than the max count update the max count and store the index in another variable.
#If the maximum count is greater than half the size of the array, print the element. Else print there is no majority element.
 
#Complete Interview Preparation - GFG

#Below is the implementation of the above idea:

# Python3 program to find Majority
# element in an array
 
# Function to find Majority
# element in an array
 
 
def findMajority(arr, n):
 
    maxCount = 0
    index = -1  # sentinels
    for i in range(n):
 
        count = 1
        # here we compare the element in
        # ith position with i+1th position
        for j in range(i+1, n):
 
            if(arr[i] == arr[j]):
                count += 1
 
        # update maxCount if count of
        # current element is greater
        if(count > maxCount):
 
            maxCount = count
            index = i
 
    # if maxCount is greater than n/2
    # return the corresponding element
    if (maxCount > n//2):
        print(arr[index])
 
    else:
        print("No Majority Element")
 
 
# Driver code
if __name__ == "__main__":
    arr = [1, 1, 2, 1, 3, 5, 1]
    n = len(arr)
 
    # Function calling
    findMajority(arr, n)
 
# This code is contributed
# by ChitraNayal
#Output
#1
#Time Complexity: O(n*n), A nested loop is needed where both the loops traverse the array from start to end.
#Auxiliary Space: O(1), No extra space is required.
#--------------------------------------------------------------
#Majority Element using Binary Search Tree
#Insert elements in BST one by one and if an element is already present then increment the count of the node. At any stage, if the count of a node becomes more than n/2 then return.

#Illustration:

#Follow the steps below to solve the given problem:

#Create a binary search tree, if the same element is entered in the binary search tree the frequency of the node is increased.
#traverse the array and insert the element in the binary search tree.
#If the maximum frequency of any node is greater than half the size of the array, then perform an inorder traversal and find the node with a frequency greater than half
#Else print No majority Element.
#Below is the implementation of the above idea:

# Python3 program to demonstrate insert operation in binary
# search tree.
# class for creating node
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1  # count of number of times data is inserted in tree
 
# class for binary search tree
# it initialises tree with None root
# insert function inserts node as per BST rule
# and also checks for majority element
# if no majority element is found yet, it returns None
 
 
class BST():
    def __init__(self):
        self.root = None
 
    def insert(self, data, n):
        out = None
        if (self.root == None):
            self.root = Node(data)
        else:
            out = self.insertNode(self.root, data, n)
        return out
 
    def insertNode(self, currentNode, data, n):
        if (currentNode.data == data):
            currentNode.count += 1
            if (currentNode.count > n//2):
                return currentNode.data
            else:
                return None
        elif (currentNode.data < data):
            if (currentNode.right):
                self.insertNode(currentNode.right, data, n)
            else:
                currentNode.right = Node(data)
        elif (currentNode.data > data):
            if (currentNode.left):
                self.insertNode(currentNode.left, data, n)
            else:
                currentNode.left = Node(data)
 
 
# Driver code
# declaring an array
arr = [3, 2, 3]
n = len(arr)
 
# declaring None tree
tree = BST()
flag = 0
for i in range(n):
    out = tree.insert(arr[i], n)
    if (out != None):
        print(arr[i])
        flag = 1
        break
if (flag == 0):
    print("No Majority Element")
#Output
#3
#Time Complexity: If a Binary Search Tree is used then time complexity will be O(n²). If a self-balancing-binary-search tree is used then it will be O(nlogn)
A#uxiliary Space: O(n), As extra space is needed to store the array in the tree.

#Majority Element Using Moore’s Voting Algorithm:
#This is a two-step process:

#The first step gives the element that may be the majority element in the array. If there is a majority element in an array, then this step will definitely return majority element, otherwise, it will return candidate for majority element.
#Check if the element obtained from the above step is the majority element. This step is necessary as there might be no majority element. 
#Illustration:

#arr[] = {3, 4, 3, 2, 4, 4, 4, 4}, n = 8

#maj_index = 0, count = 1

#At i = 1: arr[maj_index] != arr[i]

#count = count – 1 = 1 – 1 = 0
#now count == 0 then:
#maj_index = i = 1
#count = count + 1 = 0 + 1 = 1
#At i = 2: arr[maj_index] != arr[i]

#count = count – 1 = 1 – 1 = 0
#now count == 0 then:
#maj_index = i = 2
#count = count + 1 = 0 + 1 = 1
#At i = 3: arr[maj_index] != arr[i]

#count = count – 1 = 1 – 1 = 0
#now count == 0 then:
##maj_index = i = 3
#count = count + 1 = 0 + 1 = 1
#At i = 4: arr[maj_index] != arr[i]

#count = count – 1 = 1 – 1 = 0
#now count == 0 then:
#maj_index = i = 4
#count = count + 1 = 0 + 1 = 1
#At i = 5: arr[maj_index] == arr[i]

#count = count + 1 = 1 + 1 = 2
#At i = 6: arr[maj_index] == arr[i]

#count = count + 1 = 2 + 1 = 3
#At i = 7: arr[maj_index] == arr[i]

#count = count + 1 = 3 + 1 = 4
#Therefore, the arr[maj_index] may be the possible candidate for majority element.

#Now, Again traverse the array and check whether arr[maj_index] is the majority element or not.

#arr[maj_index] is 4

#4 occurs 5 times in the array therefore 4 is our majority element.

#Follow the steps below to solve the given problem:

#Loop through each element and maintains a count of the majority element, and a majority index, maj_index
#If the next element is the same then increment the count if the next element is not the same then decrement the count.
#f the count reaches 0 then change the maj_index to the current element and set the count again to 1.
#Now again traverse through the array and find the count of the majority element found.
##If the count is greater than half the size of the array, print the element
#Else print that there is no majority element
#Below is the implementation of the above idea: 