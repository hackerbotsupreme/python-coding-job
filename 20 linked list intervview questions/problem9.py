#Delete last occurrence of an item from linked list
#Difficulty Level : Easy
#Using pointers, loop through the whole list and keep track of the node prior to the node containing the last occurrence key using a special pointer. After this just store the next of next of the special pointer, into to next of special pointer to remove the required node from the linked list.
# A linked list Node
class Node: 
    def __init__(self, new_data): 
          
        self.data = new_data 
        self.next = None
  
# Function to delete the last occurrence
def deleteLast(head, x):
  
    temp = head
    ptr = None
      
    while (temp != None): 
          
        # If found key, update
        if (temp.data == x):
            ptr = temp     
              
        temp = temp.next
      
    # If the last occurrence is the last node
    if (ptr != None and ptr.next == None): 
        temp = head
        while (temp.next != ptr):
            temp = temp.next
              
        temp.next = None
      
    # If it is not the last node
    if (ptr != None and ptr.next != None): 
        ptr.data = ptr.next.data
        temp = ptr.next
        ptr.next = ptr.next.next
          
    return head
      
# Utility function to create a new node
# with given key 
def newNode(x):
  
    node = Node(0)
    node.data = x
    node.next = None
    return node
  
# This function prints contents of linked 
# list starting from the given Node
def display(head):
  
    temp = head
      
    if (head == None): 
        print("NULL\n")
        return
      
    while (temp != None): 
        print( temp.data," --> ", end = "")
        temp = temp.next
      
    print("NULL")
  
# Driver code
head = newNode(1)
head.next = newNode(2)
head.next.next = newNode(3)
head.next.next.next = newNode(4)
head.next.next.next.next = newNode(5)
head.next.next.next.next.next = newNode(4)
head.next.next.next.next.next.next = newNode(4)
  
print("Created Linked list: ", end = '')
display(head)
  
# Pass the address of the head pointer
head = deleteLast(head, 4) 
print("List after deletion of 4: ", end = '')
  
display(head)
  
# This code is contributed by rutvik_56

#Output
#Created Linked list: 1 --> 2 --> 3 --> 4 --> 5 --> 4 --> 4 --> NULL
#List after deletion of 4: 1 --> 2 --> 3 --> 4 --> 5 --> 4 --> NULL
#Time Complexity: O(n)

#Auxiliary Space: O(1)
#Given a linked list and a key to be deleted. Delete last occurrence of key from linked. The list may have duplicates.

#Examples:  

#Input:   1->2->3->5->2->10, key = 2
#Output:  1->2->3->5->10
#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#The idea is to traverse the linked list from beginning to end. While traversing, keep track of last occurrence key. After traversing the complete list, delete the last occurrence by copying data of next node and deleting the next node.  




# Python3 program to demonstrate deletion of 
# last Node in singly linked list 
  
# A linked list Node 
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
def deleteLast(head, key) :
  
    # Initialize previous of Node to be deleted 
    x = None
  
    # Start from head and find the Node to be 
    # deleted 
    temp = head 
    while (temp != None) :
      
        # If we found the key, update xv 
        if (temp.key == key) :
            x = temp 
  
        temp = temp.next
      
    # key occurs at-least once 
    if (x != None) :
      
        # Copy key of next Node to x 
        x.key = x.next.key 
  
        # Store and unlink next 
        temp = x.next
        x.next = x.next.next
  
        # Free memory for next 
      
    return head
  
# Utility function to create 
# a new node with given key 
def newNode(key) :
  
    temp = Node(0) 
    temp.key = key 
    temp.next = None
    return temp 
  
# This function prints contents of linked list 
# starting from the given Node 
def printList( node) :
  
    while (node != None) :
      
        print ( node.key, end = " ") 
        node = node.next
      
# Driver Code 
if __name__=='__main__': 
  
    # Start with the empty list 
    head = newNode(1) 
    head.next = newNode(2) 
    head.next.next = newNode(3) 
    head.next.next.next = newNode(5) 
    head.next.next.next.next = newNode(2) 
    head.next.next.next.next.next = newNode(10) 
  
    print("Created Linked List: ") 
    printList(head) 
    deleteLast(head, 2) 
      
    print("\nLinked List after Deletion of 2: ") 
    printList(head) 
  
# This code is contributed by Arnab Kun
#Output
#Created Linked List: 
# 1  2  3  5  2  10 
#Linked List after Deletion of 2: 
# 1  2  3  5  10 
#Time Complexity: O(n)

#Auxiliary Space: O(1)
#The above solution doesn’t work when the node to be deleted is the last node.
#Following solution handles all cases. 


# A Python3 program to demonstrate deletion of last
# Node in singly linked list
  
# A linked list Node
class Node: 
    def __init__(self, new_data): 
        self.data = new_data 
        self.next = None
  
# Function to delete the last occurrence
def deleteLast(head, x):
  
    temp = head
    ptr = None
    while (temp!=None): 
  
        # If found key, update
        if (temp.data == x) :
            ptr = temp     
        temp = temp.next
      
    # If the last occurrence is the last node
    if (ptr != None and ptr.next == None): 
        temp = head
        while (temp.next != ptr) :
            temp = temp.next    
        temp.next = None
      
    # If it is not the last node
    if (ptr != None and ptr.next != None): 
        ptr.data = ptr.next.data
        temp = ptr.next
        ptr.next = ptr.next.next
          
    return head
      
# Utility function to create a new node with
# given key 
def newNode(x):
  
    node = Node(0)
    node.data = x
    node.next = None
    return node
  
# This function prints contents of linked list
# starting from the given Node
def display( head):
  
    temp = head
    if (head == None): 
        print("None\n")
        return
      
    while (temp != None): 
        print( temp.data," -> ",end="")
        temp = temp.next
      
    print("None")
  
# Driver code
  
head = newNode(1)
head.next = newNode(2)
head.next.next = newNode(3)
head.next.next.next = newNode(4)
head.next.next.next.next = newNode(5)
head.next.next.next.next.next = newNode(4)
head.next.next.next.next.next.next = newNode(4)
print("Created Linked list: ")
display(head)
head = deleteLast(head, 4)
print("List after deletion of 4: ")
display(head)
  
# This code is contributed by Arnab Kundu

#Output
#Created Linked list:  --> 1 --> 2 --> 3 --> 4 --> 5 --> 4 --> 4NULL
#Linked List after deletion of 4:  --> 1 --> 2 --> 3 --> 4 --> 5 --> 4NULL
#Time Complexity: O(n)

#Auxiliary Space: O(1)
#Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above