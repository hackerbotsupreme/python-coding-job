#Write a function to delete a Linked List

#Difficulty Level : Basic
#Algorithm For C/C++: Iterate through the linked list and delete all the nodes one by one. The main point here is not to access the next of the current pointer if the current pointer is deleted.
#In Java, Python, and JavaScript automatic garbage collection happens, so deleting a linked list is easy. Just need to change head to null.

#You can delete the link list by following 3 methods:

#Delete from beginning
#Delete from the end
#Delete from middle
#Delete from the beginning :

#ALGORITHM:


#Store the address of the first node in a pointer. 
#move the head node to the next node
#dispose or free memory  of the pointer node 

# Delete linkedlist from beginiing
X = head
head = head.next
X = None

#Complete Interview Preparation - GFG
#ALGORITHM:

#Traverse link list  to second last element
#Change its next pointer to null
#Free the memory of the last node.
#C
#Python3
# Delete linkedlist from end
temp = head
while (temp.next and temp.next.next != None):
  temp = temp.next
temp.next = None
#Delete from the middle:

#ALGORITHM:

#Store the address of the deleted node as a key node.
#Store the address of the preceding node in a pointer. Eg . P
#Store the address of a key node in the pointer variable  . eg . X
#Make the successor of the key node as the successor of the node pointed by p.
#Free node X.



# Delete linkedlist from middle
for i in range(2,position):
  if temp.next != None:
    temp = temp.next;
temp.next = temp.next.next;
#Delete from the middle:

#ALGORITHM:

#Store the address of the deleted node as a key node.
#Store the address of the preceding node in a pointer. Eg . P
#Store the address of a key node in the pointer variable  . eg . X
#Make the successor of the key node as the successor of the node pointed by p.
#Free node X.



# Delete linkedlist from middle
for i in range(2,position):
  if temp.next != None:
    temp = temp.next;
temp.next = temp.next.next;
#Implementation: 

# Python3 program to delete all
# the nodes of singly linked list
 
# Node class
 
 
class Node:
 
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
 
 
# Constructor to initialize the node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    def deleteList(self):
 
        # initialize the current node
        current = self.head
        while current:
            next_to_current = current.next  # move next node
 
            # delete the current node
            del current.data
 
            # set current equals prev node
            current = next_to_current
 
        # In python garbage collection happens
        # therefore, only
        # self.head = None
        # would also delete the link list
 
    # push function to add node in front of llist
    def push(self, new_data):
 
        # Allocate the Node &
        # Put in the data
        new_node = Node(new_data)
 
        # Make next of new Node as head
        new_node.next = self.head
 
        # Move the head to point to new Node
        self.head = new_node
 
 
# Use push() to construct below
# list 1-> 12-> 1-> 4-> 1
if __name__ == '__main__':
 
    llist = LinkedList()
    llist.push(1)
    llist.push(4)
    llist.push(1)
    llist.push(12)
    llist.push(1)
 
    print("Deleting linked list")
    llist.deleteList()
 
    print("Linked list deleted")
 
 
# This article is provided by Shrikant13

#Output
#Deleting linked list
#Linked list deleted
#Time Complexity: O(n) 
#Auxiliary Space: O(1)