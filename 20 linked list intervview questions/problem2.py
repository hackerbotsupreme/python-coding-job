#Flattening a Linked List

#Difficulty Level : Hard
#---------------------------------------------------------------
#Given a linked list where every node represents a linked list and contains two pointers of its type: 

#Pointer to next node in the main list (we call it ‘right’ pointer in the code below) 
#Pointer to a linked list where this node is headed (we call it the ‘down’ pointer in the code below). 
#Note: All linked lists are sorted and the resultant linked list should also be sorted

#Examples: 

#Input:    5 -> 10 -> 19 -> 28
#               |        |         |        |
#              V       V       V       V
#              7      20      22     35
#               |                 |        |
#              V               V       V
#              8               50     40
#              |                          |
#             V                        V
#            30                       45

#Output: 5->7->8->10->19->20->22->28->30->35->40->45->50

#Input:    3 -> 10 -> 7 -> 14
#               |        |         |        |
#              V       V       V       V
#              9      47      15     22
#               |                 |        
#              V                V      
#              17              30

#Output: 3->7->9->10->14->15->17->22->30->47   


#The idea is to use the Merge() process of merge sort for linked lists. Use merge() to merge lists one by one, recursively merge() the current list with the already flattened list. The down pointer is used to link nodes of the flattened list.

 
#Complete Interview Preparation - GFG

#Follow the given steps to solve the problem:

#Recursively call to merge the current linked list with the next linked list
#If the current linked list is empty or there is no next linked list then return the current linked list (Base Case)
#Start merging the linked lists, starting from the last linked list
#After merging the current linked list with the next linked list, return the head node of the current linked list
#Below is the implementation of the above approach:


# Python3 program for flattening a Linked List
 
 
class Node():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None
 
 
class LinkedList():
    def __init__(self):
 
        # head of list
        self.head = None
 
    # Utility function to insert a node at beginning of the
    #   linked list
    def push(self, head_ref, data):
 
        # 1 & 2: Allocate the Node &
        # Put in the data
        new_node = Node(data)
 
        # Make next of new Node as head
        new_node.down = head_ref
 
        # 4. Move the head to point to new Node
        head_ref = new_node
 
        # 5. return to link it back
        return head_ref
 
    def printList(self):
 
        temp = self.head
        while(temp != None):
            print(temp.data, end=" ")
            temp = temp.down
 
        print()
 
    # An utility function to merge two sorted linked lists
    def merge(self, a, b):
        # if first linked list is empty then second
        # is the answer
        if(a == None):
            return b
 
        # if second linked list is empty then first
        # is the result
        if(b == None):
            return a
 
        # compare the data members of the two linked lists
        # and put the larger one in the result
        result = None
 
        if (a.data < b.data):
            result = a
            result.down = self.merge(a.down, b)
        else:
            result = b
            result.down = self.merge(a, b.down)
 
        result.right = None
        return result
 
    def flatten(self, root):
 
        # Base Case
        if(root == None or root.right == None):
            return root
        # recur for list on right
 
        root.right = self.flatten(root.right)
 
        # now merge
        root = self.merge(root, root.right)
 
        # return the root
        # it will be in turn merged with its left
        return root
 
 
# Driver's code
if __name__ == '__main__':
    L = LinkedList()
 
    '''
    Let us create the following linked list
            5 -> 10 -> 19 -> 28
            |    |     |     |
            V    V     V     V
            7    20    22    35
            |          |     |
            V          V     V
            8          50    40
            |                |
            V                V
            30               45
    '''
    L.head = L.push(L.head, 30)
    L.head = L.push(L.head, 8)
    L.head = L.push(L.head, 7)
    L.head = L.push(L.head, 5)
 
    L.head.right = L.push(L.head.right, 20)
    L.head.right = L.push(L.head.right, 10)
 
    L.head.right.right = L.push(L.head.right.right, 50)
    L.head.right.right = L.push(L.head.right.right, 22)
    L.head.right.right = L.push(L.head.right.right, 19)
 
    L.head.right.right.right = L.push(L.head.right.right.right, 45)
    L.head.right.right.right = L.push(L.head.right.right.right, 40)
    L.head.right.right.right = L.push(L.head.right.right.right, 35)
    L.head.right.right.right = L.push(L.head.right.right.right, 20)
 
    # Function call
    L.head = L.flatten(L.head)
 
    L.printList()
    # This code is contributed by maheshwaripiyush9
#Output
#5 7 8 10 19 20 20 22 30 35 40 45 50 
#Time Complexity: O(N * N * M) – where N is the no of nodes in the main linked list and M is the no of nodes in a single sub-linked list 
#Explanation: As we are merging 2 lists at a time,

#After adding the first 2 lists, the time taken will be O(M+M) = O(2M).
#Then we will merge another list to above merged list -> time = O(2M + M) = O(3M).
#Then we will merge another list -> time = O(3M + M).
#We will keep merging lists to previously merged lists until all lists are merged.
#Total time taken will be O(2M + 3M + 4M + …. N*M) = (2 + 3 + 4 + … + N) * M
#Using arithmetic sum formula: time = O((N * N + N – 2) * M/2)
#The above expression is roughly equal to O(N * N * M) for a large value of N
#Auxiliary Space: O(N*M) – because of the recursion. The recursive functions will use a recursive stack of a size equivalent to a total number of elements in the lists, which is N*M.

#Flattening a Linked List using Priority Queues:
#The idea is, to build a Min-Heap and push head node of every linked list into it and then use Extract-min function to get minimum element from priority queue and then move forward in that linked list.

#Follow the given steps to solve the problem:

#Create a priority queue(Min-Heap) and push the head node of every linked list into it
#While the priority queue is not empty, extract the minimum value node from it and if there is a next node linked to the minimum value node then push it into the priority queue
#Also, print the value of the node every time after extracting the minimum value node
#Below is the implementation of the above approach:


from heapq import heappush, heappop
class Node:
    def __init__(self, d):
        self.data = d
        self.right = self.down = None
 
 
class LinkedList():
    def __init__(self):
 
        # head of list
        self.head = None
 
    # Utility function to insert a node at beginning of the
    #   linked list
    def push(self, head_ref, data):
 
        # 1 & 2: Allocate the Node &
        # Put in the data
        new_node = Node(data)
 
        # Make next of new Node as head
        new_node.down = head_ref
 
        # 4. Move the head to point to new Node
        head_ref = new_node
 
        # 5. return to link it back
        return head_ref
 
    def printList(self):
 
        temp = self.head
        while(temp != None):
            print(temp.data, end=" ")
            temp = temp.down
 
        print()
 
 
# class to compare two node objects
class Cmp:
    def __init__(self, node):
        self.node = node
 
    def __lt__(self, other):
        return self.node.data < other.node.data
 
 
def flatten(root):
    pq = []
    # push main linked list nodes to priority queue
    while root:
        heappush(pq, Cmp(root))
        root = root.right
    dummy = Node(0)
    temp = dummy
     
    # keep popping out the min node until there are no nodes left in priority queue
    while pq:
        node = heappop(pq).node
        temp.down = node
        temp = node
        # if bottom child exist add it to priority queue
        if node.down:
            heappush(pq, Cmp(node.down))
 
    return dummy.down
 
 
if __name__ == '__main__':
    L = LinkedList()
 
    '''
    Let us create the following linked list
            5 -> 10 -> 19 -> 28
            |    |     |     |
            V    V     V     V
            7    20    22    35
            |          |     |
            V          V     V
            8          50    40
            |                |
            V                V
            30               45
    '''
    L.head = L.push(L.head, 30)
    L.head = L.push(L.head, 8)
    L.head = L.push(L.head, 7)
    L.head = L.push(L.head, 5)
 
    L.head.right = L.push(L.head.right, 20)
    L.head.right = L.push(L.head.right, 10)
 
    L.head.right.right = L.push(L.head.right.right, 50)
    L.head.right.right = L.push(L.head.right.right, 22)
    L.head.right.right = L.push(L.head.right.right, 19)
 
    L.head.right.right.right = L.push(L.head.right.right.right, 45)
    L.head.right.right.right = L.push(L.head.right.right.right, 40)
    L.head.right.right.right = L.push(L.head.right.right.right, 35)
    L.head.right.right.right = L.push(L.head.right.right.right, 20)
 
flatten(L.head)
L.printList()
#Output
#5 7 8 10 19 20 22 28 30 35 40 45 50 
#Time Complexity: O(N * M * log(N)) – where N is the no of nodes in the main linked list (reachable using the next pointer) and M is the no of nodes in a single sub-linked list (reachable using a bottom pointer).
#Auxiliary Space: O(N) – where N is the no of nodes in the main linked list (reachable using the next pointer).