#Function to check if a singly linked list is palindrome

#Difficulty Level : Medium
 
#Given a singly linked list of characters, write a function that returns true if the given list is a palindrome, else false.



#Examples:

#Input: R->A->D->A->R->NULL
#Output: Yes


#Input: C->O->D->E->NULL
#Output: No
#Check if a Singly Linked List is Palindrome using Stack:
#The idea is to use a stack and push all the nodes into the stack, then again iterate over the linked list to validate if the linked list is palindrome or not.

#Follow the steps below to solve the problem:

#A simple solution is to use a stack of list nodes. This mainly involves three steps.
#Traverse the given list from head to tail and push every visited node to stack.
#Traverse the list again. For every visited node, pop a node from the stack and compare data of popped node with the currently visited node.
#If all nodes matched, then return true, else false.
#Below is the implementation of the above approach : 



# Python3 program to check if linked
# list is palindrome using stack
 
 
class Node:
    def __init__(self, data):
 
        self.data = data
        self.ptr = None
 
# Function to check if the linked list
# is palindrome or not
 
 
def ispalindrome(head):
 
    # Temp pointer
    slow = head
 
    # Declare a stack
    stack = []
 
    ispalin = True
 
    # Push all elements of the list
    # to the stack
    while slow != None:
        stack.append(slow.data)
 
        # Move ahead
        slow = slow.ptr
 
    # Iterate in the list again and
    # check by popping from the stack
    while head != None:
 
        # Get the top most element
        i = stack.pop()
 
        # Check if data is not
        # same as popped element
        if head.data == i:
            ispalin = True
        else:
            ispalin = False
            break
 
        # Move ahead
        head = head.ptr
 
    return ispalin
 
# Driver Code
 
 
# Addition of linked list
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(3)
six = Node(2)
seven = Node(1)
 
# Initialize the next pointer
# of every current pointer
one.ptr = two
two.ptr = three
three.ptr = four
four.ptr = five
five.ptr = six
six.ptr = seven
seven.ptr = None
 
# Call function to check palindrome or not
result = ispalindrome(one)
 
print("isPalindrome:", result)
 
# This code is contributed by Nishtha Goel

#isPalindrome is true
#Time complexity: O(N), Iterating over the linked list of size N.
#Auxiliary Space: O(N), Using an auxiliary stack


#Check if a Singly Linked List is Palindrome by Reversing the Linked List:
#The idea is to first reverse the second half part of the linked list and then check whether the list is palindrome or not.

#Follow the steps below to solve the problem:

#Get the middle of the linked list. 
#Reverse the second half of the linked list. 
#Check if the first half and second half are identical. 
#Construct the original linked list by reversing the second half again and attaching it back to the first half
#Below is the implementation of the above approach:


# Python3 program to check if
# linked list is palindrome
 
# Node class
 
 
class Node:
 
    # Constructor to initialize
    # the node object
    def __init__(self, data):
 
        self.data = data
        self.next = None
 
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
 
        self.head = None
 
    # Function to check if given
    # linked list is palindrome or not
    def isPalindrome(self, head):
 
        slow_ptr = head
        fast_ptr = head
        prev_of_slow_ptr = head
 
        # To handle odd size list
        midnode = None
 
        # Initialize result
        res = True
 
        if (head != None and head.next != None):
 
            # Get the middle of the list.
            # Move slow_ptr by 1 and
            # fast_ptr by 2, slow_ptr
            # will have the middle node
            while (fast_ptr != None and
                   fast_ptr.next != None):
 
                # We need previous of the slow_ptr
                # for linked lists  with odd
                # elements
                fast_ptr = fast_ptr.next.next
                prev_of_slow_ptr = slow_ptr
                slow_ptr = slow_ptr.next
 
            # fast_ptr would become NULL when
            # there are even elements in the
            # list and not NULL for odd elements.
            # We need to skip the middle node for
            # odd case and store it somewhere so
            # that we can restore the original list
            if (fast_ptr != None):
                midnode = slow_ptr
                slow_ptr = slow_ptr.next
 
            # Now reverse the second half
            # and compare it with first half
            second_half = slow_ptr
 
            # NULL terminate first half
            prev_of_slow_ptr.next = None
 
            # Reverse the second half
            second_half = self.reverse(second_half)
 
            # Compare
            res = self.compareLists(head, second_half)
 
            # Construct the original list back
            # Reverse the second half again
            second_half = self.reverse(second_half)
 
            if (midnode != None):
 
                # If there was a mid node (odd size
                # case) which was not part of either
                # first half or second half.
                prev_of_slow_ptr.next = midnode
                midnode.next = second_half
            else:
                prev_of_slow_ptr.next = second_half
        return res
 
    # Function to reverse the linked list
    # Note that this function may change
    # the head
    def reverse(self, second_half):
 
        prev = None
        current = second_half
        next = None
 
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
 
        second_half = prev
        return second_half
 
    # Function to check if two input
    # lists have same data
    def compareLists(self, head1, head2):
 
        temp1 = head1
        temp2 = head2
 
        while (temp1 and temp2):
            if (temp1.data == temp2.data):
                temp1 = temp1.next
                temp2 = temp2.next
            else:
                return 0
 
        # Both are empty return 1
        if (temp1 == None and temp2 == None):
            return 1
 
        # Will reach here when one is NULL
        # and other is not
        return 0
 
    # Function to insert a new node
    # at the beginning
    def push(self, new_data):
 
        # Allocate the Node &
        # Put in the data
        new_node = Node(new_data)
 
        # Link the old list of the new one
        new_node.next = self.head
 
        # Move the head to point to new Node
        self.head = new_node
 
    # A utility function to print
    # a given linked list
    def printList(self):
 
        temp = self.head
 
        while(temp):
            print(temp.data, end="->")
            temp = temp.next
 
        print("NULL")
 
 
# Driver code
if __name__ == '__main__':
 
    l = LinkedList()
    s = ['a', 'b', 'a', 'c', 'a', 'b', 'a']
 
    for i in range(7):
        l.push(s[i])
    if (l.isPalindrome(l.head) != False):
        print("Is Palindrome\n")
    else:
        print("Not Palindrome\n")
 

#Is Palindrome
#Time Complexity: O(N),  
#Auxiliary Space: O(1)

#Check if a Singly Linked List is Palindrome using Recursion: 
#The idea is to use the function call stack as a container. Recursively traverse till the end of the list. When returning from the last NULL, will be at the last node. The last node is to be compared with the first node of the list.

#Follow the steps below to solve the problem:

#First make a recursive call to the next node of linked till it reach the last node.
#After returning from last node start checking from start of the linked list then move to the next node.
#Repeat these steps till reach the last node.
#Below is the implementation of above approach:

# Python program for the above approach
 
# Head of the list
head = None
left = None
 
 
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
 
# Initial parameters to this function are
# &head and head
 
 
def isPalindromeUtil(right):
    global head, left
 
    left = head
 
    # Stop recursion when right becomes null
    if (right == None):
        return True
 
    # If sub-list is not palindrome then no need to
    # check for the current left and right, return
    # false
    isp = isPalindromeUtil(right.next)
    if (isp == False):
        return False
 
    # Check values at current left and right
    isp1 = (right.data == left.data)
 
    left = left.next
 
    # Move left to next node;
    return isp1
 
# A wrapper over isPalindrome(Node head)
 
 
def isPalindrome(head):
    result = isPalindromeUtil(head)
    return result
 
# Push a node to linked list. Note that
# this function changes the head
 
 
def push(new_data):
    global head
 
    # Allocate the node and put in the data
    new_node = Node(new_data)
 
    # Link the old list of the new one
    new_node.next = head
 
    # Move the head to point to new node
    head = new_node
 
# A utility function to print a
# given linked list
 
 
def printList(ptr):
    while (ptr != None):
        print(ptr.data, end="->")
        ptr = ptr.next
 
    print("Null ")
 
 
# Driver Code
str = ['a', 'b', 'a', 'c', 'a', 'b', 'a']
 
for i in range(0, 7):
    push(str[i])
 
if (isPalindrome(head) and i != 0):
    print("Is Palindrome\n")
else:
    print("Not Palindrome\n")
 
# This code is contributed by saurabh_jaiswal.


#Output
#Is Palindrome
#Time Complexity: O(N), Traversing over the linked list of size N.
#Auxiliary Space: O(N) if Function Call Stack size is considered, otherwise O(1).