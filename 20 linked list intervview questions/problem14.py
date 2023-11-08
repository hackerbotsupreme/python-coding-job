#Reverse a Linked List

#Difficulty Level : Medium
#Given a pointer to the head node of a linked list, the task is to reverse the linked list. We need to reverse the list by changing the links between nodes.

#Examples: 

#Input: Head of following linked list 
#1->2->3->4->NULL 
#Output: Linked list should be changed to, 
#4->3->2->1->NULL

#Input: Head of following linked list 
#1->2->3->4->5->NULL 
#Output: Linked list should be changed to, 
#5->4->3->2->1->NULL


#Input: NULL 
#Output: NULL

#Input: 1->NULL 
#Output: 1->NULL 
#Reverse a linked list by Iterative Method:
#The idea is to use three pointers curr, prev, and next to keep track of nodes to update reverse links.



#Illustration:



#Follow the steps below to solve the problem:

#Initialize three pointers prev as NULL, curr as head, and next as NULL.
#Iterate through the linked list. In a loop, do the following:
#Before changing the next of curr, store the next node 
#next = curr -> next
#Now update the next pointer of curr to the prev 
#curr -> next = prev 
#Update prev as curr and curr as next 
#prev = curr 
#curr = next
#Below is the implementation of the above approach: 
# Python program to reverse a linked list
# Time Complexity : O(n)
# Space Complexity : O(1)
 
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
 
    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Utility function to print the LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
 
 
# Driver code
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
 
print ("Given linked list")
llist.printList()
llist.reverse()
print ("\nReversed linked list")
llist.printList()
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

#Output
#Given linked list
#85 15 4 20 
#Reversed linked list 
#20 4 15 85 
#Time Complexity: O(N), Traversing over the linked list of size N. 
#Auxiliary Space: O(1)

Reverse a linked list using Recursion:
The idea is to reach the last node of the linked list using recursion then start reversing the linked list.

Illustration:

Linked List Rverse

Follow the steps below to solve the problem:

Divide the list in two parts – first node and rest of the linked list.
Call reverse for the rest of the linked list.
Link the rest linked list to first.
Fix head pointer to NULL
Below is the implementation of above approach:

C++
Java
Python3
"""Python3 program to reverse linked list
using recursive method"""
 
# Linked List Node
 
 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
# Create and Handle list operations
 
 
class LinkedList:
    def __init__(self):
        self.head = None  # Head of list
 
    # Method to reverse the list
    def reverse(self, head):
 
        # If head is empty or has reached the list end
        if head is None or head.next is None:
            return head
 
        # Reverse the rest list
        rest = self.reverse(head.next)
 
        # Put first element at the end
        head.next.next = head
        head.next = None
 
        # Fix the header pointer
        return rest
 
    # Returns the linked list in display format
    def __str__(self):
        linkedListStr = ""
        temp = self.head
        while temp:
            linkedListStr = (linkedListStr +
                             str(temp.data) + " ")
            temp = temp.next
        return linkedListStr
 
    # Pushes new data to the head of the list
    def push(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
 
 
# Driver code
linkedList = LinkedList()
linkedList.push(20)
linkedList.push(4)
linkedList.push(15)
linkedList.push(85)
 
print("Given linked list")
print(linkedList)
 
linkedList.head = linkedList.reverse(linkedList.head)
 
print("Reversed linked list")
print(linkedList)
 
# This code is contributed by Debidutta Rath

#Output
#Given linked list
#85 15 4 20 
#Reversed linked list 
#20 4 15 85 
#Time Complexity: O(N), Visiting over every node one time 
#Auxiliary Space: O(N), Function call stack space

#Reverse a linked list by Tail Recursive Method:
#The idea is to maintain three pointers previous, current and next, recursively visit every node and make links using these three pointers.

#Follow the steps below to solve the problem:

#First update next with next node of current i.e. next = current->next
#Now make a reverse link from current node to previous node i.e. curr->next = prev
#If the visited node is the last node then just make a reverse link from the current node to previous node and update head. 
#Below is the implementation of the above approach:





# Simple and tail recursive Python program to
# reverse a linked list
 
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
 
    def reverseUtil(self, curr, prev):
 
        # If last node mark it head
        if curr.next is None:
            self.head = curr
 
            # Update next to prev node
            curr.next = prev
            return
 
        # Save curr.next node for recursive call
        next = curr.next
 
        # And update next
        curr.next = prev
 
        self.reverseUtil(next, curr)
 
    # This function mainly calls reverseUtil()
    # with previous as None
 
    def reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)
 
    # Function to insert a new node at the beginning
 
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data, end=" ")
            temp = temp.next
 
 
# Driver code
llist = LinkedList()
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
 
print ("Given linked list")
llist.printList()
 
llist.reverse()
 
print ("\nReversed linked list")
llist.printList()
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

#Output
#Given linked list
#1 2 3 4 5 6 7 8 
#Reversed linked list
#8 7 6 5 4 3 2 1 
#Time Complexity: O(N), Visiting every node of the linked list of size N.
#Auxiliary Space: O(N), Function call stack space

#Reverse a linked list using Stack:
#The idea is to store the all the nodes in the stack then make a reverse linked list.

#Follow the steps below to solve the problem:

#Store the nodes(values and address) in the stack until all the values are entered.
#Once all entries are done, Update the Head pointer to the last location(i.e the last value).
#Start popping the nodes(value and address) and store them in the same order until the stack is empty.
#Update the next pointer of last Node in the stack by NULL.
#Below is the implementation of the above approach:

#C++
#Java
#Python3
# Python code for the above approach
 
# Definition for singly-linked list.
 
 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
 
class Solution:
 
    # Program to reverse the linked list
    # using stack
    def reverseLLUsingStack(self, head):
 
        # Initialise the variables
        stack, temp = [], head
 
        while temp:
            stack.append(temp)
            temp = temp.next
 
        head = temp = stack.pop()
 
        # Until stack is not
        # empty
        while len(stack) > 0:
            temp.next = stack.pop()
            temp = temp.next
 
        temp.next = None
        return head
 
 
# Driver Code
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print("Given linked list")
    temp = head
    while temp:
        print(temp.val, end=' ')
        temp = temp.next
    obj = Solution()
    print("\nReversed linked list")
    head = obj.reverseLLUsingStack(head)
    while head:
        print(head.val, end=' ')
        head = head.next
#

#Output
#Given linked list
#1 2 3 4 
#Reversed linked list
#4 3 2 1 
##Time Complexity: O(N), Visiting every node of the linked list of size N.
#Auxiliary Space: O(N), Space is used to store the nodes in the stack.
