#Union and Intersection of two sorted arrays

#Difficulty Level : Easy
#-------------------------------------------------------------
#Given two sorted arrays, find their union and intersection.
#Example:

#Input: arr1[] = {1, 3, 4, 5, 7}
#        arr2[] = {2, 3, 5, 6} 
#Output: Union : {1, 2, 3, 4, 5, 6, 7} 
#         Intersection : {3, 5}

#Input: arr1[] = {2, 5, 6}
#        arr2[] = {4, 6, 8, 10} 
#Output: Union : {2, 4, 5, 6, 8, 10} 
#         Intersection : {6}
#------------------------------------------------------------------
#Union of arrays arr1[] and arr2[]


#To find union of two sorted arrays, follow the following merge procedure : 

#1) Use two index variables i and j, initial values i = 0, j = 0 
#2) If arr1[i] is smaller than arr2[j] then print arr1[i] and increment i. 
#3) If arr1[i] is greater than arr2[j] then print arr2[j] and increment j. 
#4) If both are same then print any of them and increment both i and j. 
#5) Print remaining elements of the larger array.

#Below is the implementation of the above approach : 



# Python program to find union of
# two sorted arrays
# Function prints union of arr1[] and arr2[]
# m is the number of elements in arr1[]
# n is the number of elements in arr2[]
def printUnion(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            print(arr1[i],end=" ")
            i += 1
        elif arr2[j] < arr1[i]:
            print(arr2[j],end=" ")
            j+= 1
        else:
            print(arr2[j],end=" ")
            j += 1
            i += 1
 
    # Print remaining elements of the larger array
    while i < m:
        print(arr1[i],end=" ")
        i += 1
 
    while j < n:
        print(arr2[j],end=" ")
        j += 1
 
# Driver program to test above function
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
m = len(arr1)
n = len(arr2)
printUnion(arr1, arr2, m, n)
 
# This code is contributed by Pratik Chhajer
#Output
#1 2 3 4 5 6 7 
#Time Complexity : O(m + n)
#Auxiliary Space: O(1)
#---------------------------------------------------------------

Handling duplicates in any of the arrays: Above code does not handle duplicates in any of the arrays. To handle the duplicates, just check for every element whether adjacent elements are equal. 

Below is the implementation of this approach. 

# Python3 program to find union of two
# sorted arrays (Handling Duplicates)
def union_array(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    i = 0
    j = 0
     
    # keep track of last element to avoid duplicates
    prev = None
     
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            if arr1[i] != prev:
                print(arr1[i], end=' ')
                prev = arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            if arr2[j] != prev:
                print(arr2[j], end=' ')
                prev = arr2[j]
            j += 1
        else:
            if arr1[i] != prev:
                print(arr1[i], end=' ')
                prev = arr1[i]
            i += 1
            j += 1
             
    while i < m:
        if arr1[i] != prev:
            print(arr1[i], end=' ')
            prev = arr1[i]
        i += 1
 
    while j < n:
        if arr2[j] != prev:
            print(arr2[j], end=' ')
            prev = arr2[j]
        j += 1
     
# Driver Code
if __name__ == "__main__":
    arr1 = [1, 2, 2, 2, 3]
    arr2 = [2, 3, 4, 5]
         
    union_array(arr1, arr2)
 
# This code is contributed by Sanjay Kumar
#Output
#1 2 3 4 5 
#Time Complexity: O(l1 + l2) 
#Auxiliary Space: O(n)
#---------------------------------------------------------------
#Another Approach using TreeSet in Java: The idea of the approach is to build a TreeSet and insert all the elements from both arrays into it. As a tree set stores only unique values, it will only keep all the unique values of both arrays.

#Below is the implementation of the approach.

#// Java code to implement the approach
 
import java.io.*;
import java.util.*;
 
class GFG {
 
    // Function to return the union of two arrays
    public static ArrayList<Integer>
    Unionarray(int arr1[], int arr2[],
               int n, int m)
    {
        TreeSet<Integer> set = new TreeSet<>();
         
        // Remove the duplicates from arr1[]
        for (int i : arr1)
            set.add(i);
       
        // Remove duplicates from arr2[]
        for (int i : arr2)
            set.add(i);
       
        // Loading set to array list
        ArrayList<Integer> list
            = new ArrayList<>();
        for (int i : set)
            list.add(i);
 
        return list;
    }
   
    // Driver code
    public static void main(String[] args)
    {
        int arr1[] = { 1, 2, 2, 2, 3 };
        int arr2[] = { 2, 3, 3, 4, 5, 5 };
        int n = arr1.length;
        int m = arr2.length;
       
        // Function call
        ArrayList<Integer> uni
            = Unionarray(arr1, arr2, n, m);
        for (int i : uni) {
            System.out.print(i + " ");
        }
    }
}
 
#//  Contributed by ARAVA SAI TEJA
#Output
#1 2 3 4 5 
#Time Complexity: O(m + n) where ‘m’ and ‘n’ are the size of the arrays
#Auxiliary Space: O(m*log(m)+n*log(n)) because adding element into TreeSet takes O(logn) time adding n elements will take (nlogn)