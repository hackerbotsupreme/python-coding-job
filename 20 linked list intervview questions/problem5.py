#Add 1 to a number represented as linked list
#Difficulty Level : Medium
#---------------------------------------------------
#Number is represented in linked list such that each digit corresponds to a node in linked list. Add 1 to it. For example 1999 is represented as (1-> 9-> 9 -> 9) and adding 1 to it should change it to (2->0->0->0) 
#elow are the steps : 

#Reverse given linked list. For example, 1-> 9-> 9 -> 9 is converted to 9-> 9 -> 9 ->1.
#Start traversing linked list from leftmost node and add 1 to it. If there is a carry, move to the next node. Keep moving to the next node while there is a carry.
#Reverse modified linked list and return head.
 
#Complete Interview Preparation - GFG

#Below is the implementation of above steps. 


# Python3 program to add 1 to a linked list
import sys
import math
 
# Linked list node
 
 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
# Function to create a new node with given data */
 
 
def newNode(data):
    return Node(data)
 
# Function to reverse the linked list */
 
 
def reverseList(head):
    if not head:
        return
    curNode = head
    prevNode = head
    nextNode = head.next
    curNode.next = None
 
    while(nextNode):
        curNode = nextNode
        nextNode = nextNode.next
        curNode.next = prevNode
        prevNode = curNode
 
    return curNode
 
# Adds one to a linked lists and return the head
# node of resultant list
 
 
def addOne(head):
 
    # Reverse linked list and add one to head
    head = reverseList(head)
    k = head
    carry = 0
    prev = None
    head.data += 1
 
    # update carry for next calculation
    while(head != None) and (head.data > 9 or carry > 0):
        prev = head
        head.data += carry
        carry = head.data // 10
        head.data = head.data % 10
        head = head.next
 
    if carry > 0:
        prev.next = Node(carry)
    # Reverse the modified list
    return reverseList(k)
 
# A utility function to print a linked list
 
 
def printList(head):
    if not head:
        return
    while(head):
        print("{}".format(head.data), end="")
        head = head.next
 
 
# Driver code
if __name__ == '__main__':
    head = newNode(1)
    head.next = newNode(9)
    head.next.next = newNode(9)
    head.next.next.next = newNode(9)
 
    print("List is: ", end="")
    printList(head)
 
    head = addOne(head)
 
    print("\nResultant list is: ", end="")
    printList(head)
 
 
# This code is contributed by Rohit
#Output
#List is 1999

#Resultant list is 2000
#Time Complexity: O(n), Here n is the number of nodes in the linked list.
#Auxiliary Space: O(1), As constant extra space is used.