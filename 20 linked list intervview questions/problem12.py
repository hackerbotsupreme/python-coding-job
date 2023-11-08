#Merge a linked list into another linked list at alternate positions

#Difficulty Level : Easy

#Given two linked lists, insert nodes of second list into first list at alternate positions of first list. 
#For example, if first list is 5->7->17->13->11 and second is 12->10->2->4->6, the first list should become 5->12->7->10->17->2->13->4->11->6 and second list should become empty. The nodes of second list should only be inserted when there are positions available. For example, if the first list is 1->2->3 and second list is 4->5->6->7->8, then first list should become 1->4->2->5->3->6 and second list to 7->8.

#Use of extra space is not allowed (Not allowed to create additional nodes), i.e., insertion must be done in-place. Expected time complexity is O(n) where n is number of nodes in first list. 

#Recommended Problem
#Merge Lists Alternatingly
#Linked List
#Data Structures
#Amazon
#Solve Problem
#Submission count: 12.3K
#The idea is to run a loop while there are available positions in first loop and insert nodes of second list by changing pointers.

#Following are implementations of this approach. 
# Python program to merge a linked list into another at
# alternate positions
  
class Node(object):
    def __init__(self, data:int):
        self.data = data
        self.next = None
  
  
class LinkedList(object):
    def __init__(self):
        self.head = None
          
    def push(self, new_data:int):
        new_node = Node(new_data)
        new_node.next = self.head
        # 4. Move the head to point to new Node
        self.head = new_node
          
    # Function to print linked list from the Head
    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
              
    # Main function that inserts nodes of linked list q into p at alternate positions. 
    # Since head of first list never changes
    # but head of second list/ may change, 
    # we need single pointer for first list and double pointer for second list.
    def merge(self, p, q):
        p_curr = p.head
        q_curr = q.head
  
        # swap their positions until one finishes off
        while p_curr != None and q_curr != None:
  
            # Save next pointers
            p_next = p_curr.next
            q_next = q_curr.next
  
            # make q_curr as next of p_curr
            q_curr.next = p_next  # change next pointer of q_curr
            p_curr.next = q_curr  # change next pointer of p_curr
  
            # update current pointers for next iteration
            p_curr = p_next
            q_curr = q_next
            q.head = q_curr
  
  
  
# Driver program to test above functions
llist1 = LinkedList()
llist2 = LinkedList()
  
# Creating LLs
  
# 1.
llist1.push(3)
llist1.push(2)
llist1.push(1)
llist1.push(0)
  
# 2.
for i in range(8, 3, -1):
    llist2.push(i)
  
print("First Linked List:")
llist1.printList()
  
print("Second Linked List:")
llist2.printList()
  
# Merging the LLs
llist1.merge(p=llist1, q=llist2)
  
print("Modified first linked list:")
llist1.printList()
  
print("Modified second linked list:")
llist2.printList()
  
# This code is contributed by Deepanshu Mehta

#Output
#First Linked List:
#1 2 3 
#Second Linked List:
#4 5 6 7 8 
#Modified First Linked List:
#1 4 2 5 3 6 
#Modified Second Linked List:
#7 8 
#Time Complexity: O(min(n1, n2)), where n1 and n2  represents the length of the given two linked lists.
#Auxiliary Space: O(1), no extra space is required, so it is a constant.
