#Convert Singly Linked List to XOR Linked List

#Difficulty Level : Basic
#Prerequisite: 

#XOR Linked List – A Memory Efficient Doubly Linked List | Set 1
#XOR Linked List – A Memory Efficient Doubly Linked List | Set 2
#An XOR linked list is a memory efficient doubly linked list in which the next pointer of every node stores the XOR of previous and next node’s address. 
#Given a singly linked list, the task is to convert the given singly list to a XOR linked list.

#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#Approach: Since in XOR linked list each next pointer stores the XOR of prev and next nodes’s address. So the idea is to traverse the given singly linked list and keep track of the previous node in a pointer say prev.

#Now, while traversing the list, change the next pointer of every node as: 


#current -> next = XOR(prev, current->next)
#Printing the XOR linked list: 

#While printing XOR linked list we have to find the exact address of the next node every time. As we have seen above that the next pointer of every node stores the XOR value of prev and next node’s address. Therefore, the next node’s address can be obtained by finding XOR of prev and next pointer of current node in the XOR linked list.

#So, to print the XOR linked list, traverse it by maintaining a prev pointer which stores the address of the previous node and to find the next node, calculate XOR of prev with next of current node.
Below is the implementation of the above approach: 

CPP
Java
Python3
# Python3 program to Convert a Singly Linked
# List to XOR Linked List
 
# Linked List node
class Node:
    def __init__(self,d):
        self.data = d
        self.next = None
 
# Print singly linked list before conversion
def printt(head):
    while (head):
 
        # print current node
        print(head.data, end=" ")
        head = head.next
    print()
 
# Function to find XORed value of
# the node addresses
def XOR(a, b):
    return b
 
# Function to convert singly linked
# list to XOR linked list
def convert(head):
    curr = head
    prev = None
    next = curr.next
 
    while (curr):
 
        # store curr.next in next
        next = curr.next
 
        # change curr.next to XOR of prev and next
        curr.next = XOR(prev, next)
 
        # prev will change to curr for next iteration
        prev = curr
 
        # curr is now pointing to next for next iteration
        curr = next
 
# Function to print XORed linked list
def printXOR(head):
    curr = head
    prev = None
 
    while (curr):
 
        # print current node
        print(curr.data, end=" ")
 
        temp = curr
 
        # /* compute curr as prev^curr.next as
        #    it is previously set as prev^curr.next so
        #    this time curr would be prev^prev^curr.next
        #    which is curr.next */
        curr = XOR(prev, curr.next)
 
        prev = temp
 
    print()
 
# Driver Code
if __name__ == '__main__':
     
    # Create following singly linked list
    # 1.2.3.4
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
 
    print("Before Conversion : ")
    printt(head)
 
    convert(head)
    print("After Conversion : ")
    printXOR(head)
 
# This code is contributed by mohitkumar29
C#
Javascript
Output
Before Conversion : 
1 2 3 4 
After Conversion : 
1 2 3 4 
Complexity Analysis:

Time complexity: O(N) where N is no of nodes in given linked list 
Auxiliary Space: O(1)