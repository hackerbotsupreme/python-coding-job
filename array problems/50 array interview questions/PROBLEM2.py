#Write a program to reverse an array or string

#Difficulty Level : Basic

#--------------------------------------------------------------------
 
#Given an array (or string), the task is to reverse the array/string.
#Examples : 
 

#Input  : arr[] = {1, 2, 3}
#Output : arr[] = {3, 2, 1}

#Input :  arr[] = {4, 5, 1, 2}
#Output : arr[] = {2, 1, 5, 4}



 

#Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution. 
 
 

 
#Iterative way :
 


#1) Initialize start and end indexes as start = 0, end = n-1 
#2) In a loop, swap arr[start] with arr[end] and change start and end as follows : 
#start = start +1, end = end – 1

 
 

#reverse-a-number
#Another example to reverse a string:
 
#picture is avilable we can also check that out
#reverse-a-string
#-----------------------------------------------------------------------
# Iterative python program to reverse an array
 
# Function to reverse A[] from start to end
def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
 
# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)
# This program is contributed by Pratik Chhajer
#Output : 

#1 2 3 4 5 6 
#Reversed array is 
#6 5 4 3 2 1 
#----------------------------------------------------------------
#Time Complexity : O(n)
#Recursive Way :
 

#1) Initialize start and end indexes as start = 0, end = n-1 
#2) Swap arr[start] with arr[end] 
#3) Recursively call reverse for rest of the array.


#Below is the implementation of the above approach : 

# Recursive python program to reverse an array
 
# Function to reverse A[] from start to end
def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)
 
# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)
# This program is contributed by Pratik Chhajer
#Output : 

#1 2 3 4 5 6 
#Reversed array is 
#6 5 4 3 2 1 


#Time Complexity : O(n)
#-------------------------------------------------------------
def reverseList(A):
  print( A[::-1])
     
# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
print("Reversed list is")
reverseList(A) 
#Output:

#[1, 2, 3, 4, 5, 6]
#Reversed list is
#[6, 5, 4, 3, 2, 1]
































