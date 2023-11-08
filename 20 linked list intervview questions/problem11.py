#Delete N nodes after M nodes of a linked list

#Difficulty Level : Easy
#Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes then delete next N nodes, continue the same till end of the linked list.
#Difficulty Level: Rookie 

#Examples: 

#Input:
#M = 2, N = 2
#Linked List: 1->2->3->4->5->6->7->8
#Output:
#Linked List: 1->2->5->6

#Input:
#M = 3, N = 2
#Linked List: 1->2->3->4->5->6->7->8->9->10
#Output:
#Linked List: 1->2->3->6->7->8

#Input:
#M = 1, N = 1
#Linked List: 1->2->3->4->5->6->7->8->9->10
#Output:
#Linked List: 1->3->5->7->9
#Recommended Problem
#Delete N nodes after M nodes of a linked list
#Linked List
#Data Structures
#Amazon
#Microsoft
#Solve Problem
#Submission count: 42K
#The main part of the problem is to maintain proper links between nodes, and make sure that all corner cases are handled. Following is C implementation of function skipMdeleteN() that skips M nodes and delete N nodes till end of list. It is assumed that M cannot be 0. 

#Implementation:

# Python program to delete M nodes after N nodes
  
# Node class 
class Node:
  
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
  
class LinkedList:
  
    # Function to initialize head
    def __init__(self):
        self.head = None
  
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data,end=" ")
            temp = temp.next
  
    def skipMdeleteN(self, M, N):
        curr = self.head
          
        # The main loop that traverses through the
        # whole list
        while(curr):
            # Skip M nodes
            for count in range(1, M):
                if curr is None:
                    return 
                curr = curr.next
                      
            if curr is None :
                return 
  
            # Start from next node and delete N nodes
            t = curr.next 
            for count in range(1, N+1):
                if t is None:
                    break
                t = t.next
      
            # Link the previous list with remaining nodes
            curr.next = t
            # Set Current pointer for next iteration
            curr = t 
  
# Driver program to test above function
  
# Create following linked list
# 1->2->3->4->5->6->7->8->9->10
llist = LinkedList()
M = 2 
N = 3
llist.push(10)
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
  
print ("M = %d, N = %d\nGiven Linked List is:" %(M, N))
llist.printList()
print()
  
llist.skipMdeleteN(M, N)
  
print ("\nLinked list after deletion is")
llist.printList()
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

#Output
#M = 2 N = 3
#Given Linked list is :
#1 2 3 4 5 6 7 8 9 10 

#Linked list after deletion is :
#1 2 6 7 
#Time Complexity: O(n) where n is number of nodes in linked list. 
#Auxiliary Space: O(1)
