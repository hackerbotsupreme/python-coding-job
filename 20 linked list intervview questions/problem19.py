#XOR Linked List: Remove last node of the Linked List

#Last Updated : 03 Nov, 2022
Given an XOR linked list, the task is to delete the node at the end of the XOR Linked List.

Examples:

Input: 4<–>7<–>9<–>7
Output: 4<–>7<–>9
Explanation: Deleting a node from the end modifies the given XOR Linked List to 4<–>7<–>9

Input: 10
Output: List is empty
Explanation: After deleting the only node present in the XOR Linked List, the list becomes empty.


Approach: The idea to solve this problem is to traverse the XOR linked list until the last node is reached and update the address of its previous node. Follow the steps below to solve the problem:

If the XOR linked list is empty, then print “List is empty“.
Traverse the XOR Linked List until the last node of the Linked List is reached.
Update the address of its previous node.
Delete the last node from memory.
If the list becomes empty after deleting the last node, then print “List is empty”. Otherwise, print the remaining nodes of the linked list.
Below is the implementation of the above approach:

C++
// C++ program for the above approach
#include <bits/stdc++.h>
using namespace std;
 
// Structure of a node in XOR linked list
struct Node
{
   
    // Stores data value of a node
    int data;
   
    // Stores XOR of previous pointer and next pointer
    struct Node* nxp;
};
 
// Function to find the XOR of two nodes
struct Node* XOR(struct Node* a, struct Node* b) {
    return (struct Node*)((uintptr_t)(a) ^ (uintptr_t)(b));
}
 
// Function to insert a node with given value at given position
struct Node* insert(struct Node** head, int value)
{
   
    // If XOR linked list is empty
    if (*head == NULL)
    {
       
        // Initialize a new Node
        struct Node* node = new Node;
       
        // Stores data value in the node
        node->data = value;
       
        // Stores XOR of previous and next pointer
        node->nxp = XOR(NULL, NULL);
       
        // Update pointer of head node
        *head = node;
    }
 
    // If the XOR linked list is not empty
    else
    {
       
        // Stores the address of current node
        struct Node* curr = *head;
       
        // Stores the address of previous node
        struct Node* prev = NULL;
       
        // Initialize a new Node
        struct Node* node = new Node;
       
        // Update curr node address
        curr->nxp = XOR(node, XOR(NULL, curr->nxp));
       
        // Update new node address
        node->nxp = XOR(NULL, curr);
       
        // Update head
        *head = node;
       
        // Update data value of current node
        node->data = value;
    }
    return *head;
}
 
// Function to print elements of the XOR Linked List
void printList(struct Node** head)
{
    // Stores XOR pointer in current node
    struct Node* curr = *head;
   
    // Stores XOR pointer of in previous Node
    struct Node* prev = NULL;
    // Stores XOR pointer of in next node
    struct Node* next;
    // Traverse XOR linked list
    while (curr != NULL) {
        // Print current node
        cout << curr->data << " ";
        // Forward traversal
        next = XOR(prev, curr->nxp);
        // Update prev
        prev = curr;
        // Update curr
        curr = next;
    }
}
 
// Function to delete the last node present in the XOR Linked List
struct Node* delEnd(struct Node** head)
{
    // Base condition
    if (*head == NULL)
        cout << "List is empty";
    else
    {
       
        // Stores XOR pointer in current node
        struct Node* curr = *head;
       
        // Stores XOR pointer of in previous Node
        struct Node* prev = NULL;
       
        // Stores XOR pointer of in next node
        struct Node* next;
       
        // Traverse XOR linked list
        while (XOR(curr->nxp, prev) != NULL)
        {
            // Forward traversal
            next = XOR(prev, curr->nxp);
           
            // Update prev
            prev = curr;
           
            // Update curr
            curr = next;
        }
        // If the Linked List contains more than 1 node
        if (prev != NULL) {
            prev->nxp = XOR(XOR(prev->nxp, curr), NULL);
        }
        // Otherwise
        else {
            *head = NULL;
        }
 
        // Delete the last node from memory
        delete(curr);
    }
 
    // Returns head of new linked list
    return *head;
}
 
// Driver Code
int main()
{
 
    /* Create the XOR Linked List
    head-->40<-->30<-->20<-->10 */
    struct Node* head = NULL;
    insert(&head, 10);
    insert(&head, 20);
    insert(&head, 30);
    insert(&head, 40);
 
    delEnd(&head);
 
    // If the list had a single node
    if (head == NULL)
        cout << "List is empty";
    else
        // Print the list after deletion
        printList(&head);
 
    return (0);
}
 
// This code is contributed by ajaymakvana
C
Output:


40 30 20
Time Complexity: O(N)
Auxiliary Space: O(1)