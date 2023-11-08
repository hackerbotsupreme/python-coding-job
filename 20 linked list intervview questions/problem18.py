#Generate Linked List consisting of maximum difference of squares of pairs of nodes from given Linked List

#Last Updated : 11 Oct, 2022
#Given a Linked List of even number of nodes, the task is to generate a new Linked List such that it contains the maximum difference of squares of node values in decreasing order by including each node in a single pair.

#Examples:

#Input: 1 -> 6 -> 4 -> 3 -> 5 ->2
#Output: 35 -> 21 -> 7
#Explanation:
#The difference between squares of 6 and 1 forms the first node with value 35.
#The difference between squares of 5 and 2 forms the second node with value 21.
#The difference between squares of 4 and 3 forms the third node with value 7.
#Therefore, the formed LL is 35 -> 21 -> 7.

#Input: 2 -> 4 -> 5 -> 3 -> 7 -> 8 -> 9 -> 10
#Output: 96 -> 72 -> 48 -> 24
#Explanation:
#The difference between squares of 10 and 2 forms the first node with value 96.
#T#he difference between squares of 9 and 3 forms the second node with value 72.
#The difference between squares of 8 and 4 forms the third node with value 48.
#The difference between squares of 7 and 5 forms the fourth node with value 24.
#Therefore, the formed LL is 96 -> 72 -> 48 -> 24.


#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#Approach: The approach is to find the maximum value of a node and always make the difference between the largest and the smallest node value. So create a deque and insert all node’s value in it, and sort the deque. Now, access the largest and smallest values from both ends. Below are the steps:

#Create a deque and insert all values into the deque.
#Sort the deque to get the largest node value and smallest node value in constant time.
#Create another linked list having the value difference of square’s of the largest and the smallest values from the back and the front of the deque respectively.
#After each iteration, pop both the smallest and largest value from the deque.
#After the above steps, print the nodes of the new Linked List formed.
#Below is the implementation of the above approach:
# Python3 program for the
# above approach
from collections import deque
 
# Linked list node
class Node:
   
    def __init__(self, x):
       
        self.data = x
        self.next = None
 
# Function to push into Linked List
# Function to push into Linked List
def push(head_ref, new_data):
 
    new_node = Node(new_data)
    new_node.next = head_ref
    head_ref = new_node
    return head_ref
 
# Function to print the Linked List
def printt(head):
 
    curr = head
 
    # Iterate until curr
    # is None
    while (curr):
 
        # Print the data
        print(curr.data,
              end = " ")
 
        # Move to next
        curr = curr.next
 
# Function used to re-order list
# Function used to re-order list
def reorder(head):
   
    # Stores the node of LL
    arr = []
    curr = head
 
    while curr:
        arr.append(curr.data)
        curr = curr.next
 
    arr = sorted(arr)
 
    # Sort the deque
    v = deque()
 
    for i in arr:
        v.append(i)
 
    # Node head1 stores the
    # head of the new Linked List
    head1 = None
    prev = None
 
    x = len(arr) // 2
 
    while x:
        a = v.popleft()
        b = v.pop()
 
        # Difference of squares of
        # largest and smallest value
        ans = pow(b, 2) - pow(a, 2)
 
        temp = Node(ans)
 
        if head1 == None:
            head1 = temp
            prev = temp
        else:
            prev.next = temp
            prev = temp
        x -= 1
 
    # Return head of the new LL
    return head1
 
# Driver Code
if __name__ == '__main__':
   
    head 
    = None
 
    # Given Linked list
    head = push(head, 6)
    head = push(head, 5)
    head = push(head, 4)
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
 
    # Function Call
    temp = reorder(head)
 
    # Print the new LL formed
    printt(temp)
 
# This code is contributed by Mohit kumar 29
#Output: 


#35 21 7
 

#Time Complexity: O(N*log N)
#Auxiliary Space: O(N)