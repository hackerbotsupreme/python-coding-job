#Rotate a Linked List

#Difficulty Level : Easy

#Given a singly linked list, The task is to rotate the linked list counter-clockwise by k nodes.

#Examples:

#Input: linked list = 10->20->30->40->50->60, k = 4
#Output: 50->60->10->20->30->40. 
#Explanation: k is smaller than the count of nodes in a linked list so (k+1 )th node i.e. 50 becomes the head node and 60’s next points to 10

#Input: linked list = 30->40->50->60, k = 2
#Output: 50->60->30->40. 


#Recommended Problem
#Rotate a Linked List
#Linked List
#Data Structures
#Accolite
#Amazon
#+2 more
#Solve Problem
#Submission count: 1.7L
#Approach: Below is the idea to solve the problem:

#To rotate the linked list, we need to change the next pointer of kth node to NULL, the next pointer of the last node should point to the previous head node, and finally, change the head to (k+1)th node. So we need to get hold of three nodes: kth node, (k+1)th node, and last node. 
#Traverse the list from the beginning and stop at kth node. store k’s next in a tem pointer and point k’s next to NULL then start traversing from tem and keep traversing till the end and point end node’s next to start node and make tem as the new head.
#Follow the below steps to implement the idea:



#Initialize a count variable with 0 and pointer kthnode pointing to Null and current pointing to head node.
#Move from current till k-1 and point kthnode to current’s next and current’t next to NULL.
#Move current from kth node to end node and point current’s next to head.
 
#Complete Interview Preparation - GFG

#Below image shows how to rotate function works in the code :



#Below is the implementation of the above approach:
# Python program to rotate a linked list
 
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
        # allocate node and put the data
        new_node = Node(new_data)
 
        # Make next of new node as head
        new_node.next = self.head
 
        # move the head to point to the new Node
        self.head = new_node
 
    # Utility function to print it the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next
 
    # This function rotates a linked list counter-clockwise and
    # updates the head. The function assumes that k is smaller
    # than size of linked list. It doesn't modify the list if
    # k is greater than of equal to size
    def rotate(self, k):
        if k == 0:
            return
 
        # Let us understand the below code for example k = 4
        # and list = 10->20->30->40->50->60
        current = self.head
 
        # current will either point to kth or NULL after
        # this loop
        # current will point to node 40 in the above example
        count = 1
        while(count < k and current is not None):
            current = current.next
            count += 1
 
        # If current is None, k is greater than or equal
        # to count of nodes in linked list. Don't change
        # the list in this case
        if current is None:
            return
 
        # current points to kth node. Store it in a variable
        # kth node points to node 40 in the above example
        kthNode = current
 
        # current will point to last node after this loop
        # current will point to node 60 in above example
        while(current.next is not None):
            current = current.next
 
        # Change next of last node to previous head
        # Next of 60 is now changed to node 10
        current.next = self.head
 
        # Change head to (k + 1)th node
        # head is not changed to node 50
        self.head = kthNode.next
 
        # change next of kth node to NULL
        # next of 40 is not NULL
        kthNode.next = None
 
 
# Driver program to test above function
llist = LinkedList()
 
# Create a list 10->20->30->40->50->60
for i in range(60, 0, -10):
    llist.push(i)
 
#print "Given linked list"
llist.printList()
llist.rotate(4)
 
#print "\nRotated Linked list"
llist.printList()
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

#Output
#Given linked list 
#10 20 30 40 50 60 
#Rotated Linked list 
#50 60 10 20 30 40 
#Time Complexity: O(N), where N is the number of nodes in Linked List.
#Auxiliary Space: O(1)


#Another Approach: Rotate the linked list k times by placing the first element at the end.

#The idea is to traverse the given list to find the last element and store it in a node. Now we need to make the next of last element as the current head, which we can do by storing head in temporary node. Repeat the process k time.

#Follow the steps below to implement the above idea:

#Return head if the head is NULL or k=0.
#Initialize a node last and make it point to the last node of the given list.
#Make a temporary node pointing to head.
#while k>0 run a loop :
#make temp as last node and head point to next of head.
#Below is the implementation of the above approach:


# Python program for the above approach.
 
# Structure for a linked list node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
         
# Function to rotate a linked list.
def rotate(head,k):
    # let us consider the example
    #  10->20->30->40->50->60 - k=4
    # initialising 2 nodes temp and last
    last = head
    temp = head
     
    # if head is null or k==0 no rotation is required
    if head == None or k == 0:
        return head
         
    # Making last point to the last-node of the given
    # linked list in this case 60
    while last.next != None:
        last = last.next
         
    # Rotating the linked list k times, one rotation at a time.
    while k:
        # Make head point to next of head
        # so in the example given above head becomes 20
        head = head.next
         
        # Making next of temp as NULL
        # In the above example :10->NULL
        temp.next = None
         
        # Making temp as last node
        # (head)20->30->40->50->60->10(last)
        last.next = temp
        last = temp
         
        # Point temp to head again for next rotation
        temp = head
        k -= 1
    return head
     
def printList(head):
    temp = head
    while temp:
        print(temp.data, end = ' ')
        temp = temp.next
    print()
     
def push(head,new_data):
    # allocate node and put data in it
    new_node = Node(new_data)
     
    # link the old list of the new node
    new_node.next = head
     
    # move the head to point to the new node
    head = new_node
    return head
     
head = None
# create a list 10->20->30->40->50->60
for i in range(60,0,-10):
    head = push(head,i)
     
print("Given linked list: ")
printList(head)
head = rotate(head,4)
 
print("Rotated linked list: ")
printList(head)
 
# This code is contributed by hardikkushwaha.

#Given linked list 
#10 20 30 40 50 60 

#Rotated Linked list 
#50 60 10 20 30 40 
#Time Complexity: O(N)
#Auxiliary Space: O(1)