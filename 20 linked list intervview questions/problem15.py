#Why Quick Sort preferred for Arrays and Merge Sort for Linked Lists?

#Difficulty Level : Easy
#Why is Quick Sort preferred for arrays?

#Below are recursive and iterative implementations of Quick Sort and Merge Sort for arrays.

#Recursive Quick Sort for array.
#Iterative Quick Sort for arrays.
#Recursive Merge Sort for arrays
#Iterative Merge Sort for arrays

#Quick Sort in its general form is an in-place sort (i.e. it doesn’t require any extra storage) whereas merge sort requires O(N) extra storage, N denoting the array size which may be quite expensive. Allocating and de-allocating the extra space used for merge sort increases the running time of the algorithm.
#Comparing average complexity we find that both type of sorts have O(NlogN) average complexity but the constants differ. For arrays, merge sort loses due to the use of extra O(N) storage space.
#Most practical implementations of Quick Sort use randomized version. The randomized version has expected time complexity of O(nLogn). The worst case is possible in randomized version also, but worst case doesn’t occur for a particular pattern (like sorted array) and randomized Quick Sort works well in practice.
#Quick Sort is also a cache friendly sorting algorithm as it has good locality of reference when used for arrays.
#Quick Sort is also tail recursive, therefore tail call optimizations is done.
#Why is Merge Sort preferred for Linked Lists?


#Below are implementations of Quicksort and Mergesort for singly and doubly linked lists.

#Quick Sort for Doubly Linked List
#Quick Sort for Singly Linked List
#Merge Sort for Singly Linked List
#Merge Sort for Doubly Linked List

#In case of linked lists the case is different mainly due to difference in memory allocation of arrays and linked lists. Unlike arrays, linked list nodes may not be adjacent in memory.
#Unlike array, in linked list, we can insert items in the middle in O(1) extra space and O(1) time if we are given reference/pointer to the previous node. Therefore merge operation of merge sort can be implemented without extra space for linked lists.
#In arrays, we can do random access as elements are continuous in memory. Let us say we have an integer (4-byte) array A and let the address of A[0] be x then to access A[i], we can directly access the memory at (x + i*4). Unlike arrays, we can not do random access in linked list.
#uick Sort requires a lot of this kind of access. In linked list to access i’th index, we have to travel each and every node from the head to i’th node as we don’t have continuous block of memory. Therefore, the overhead increases for quick sort. Merge sort accesses data sequentially and the need of random access is low.
#Related Articles:



#Why quicksort is better than mergesort ?
#Know Your Sorting Algorithm | Set 1 (Sorting Weapons used by Programming Languages)
#Iterative Merge Sort
#Iterative Quick Sort
#Thanks to Sayan Mukhopadhyay for providing initial draft for above article. Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.
