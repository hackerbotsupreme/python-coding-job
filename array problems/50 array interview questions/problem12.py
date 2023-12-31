#Program to cyclically rotate an array by one

#Difficulty Level : Basic
#------------------------------------------------------------------------
#Given an array, cyclically rotate the array clockwise by one. 

#Examples:  

#Input:  arr[] = {1, 2, 3, 4, 5}
#Output: arr[] = {5, 1, 2, 3, 4}
#----------------------------------------------------------------------
#Following are steps. 
#1) Store last element in a variable say x. 
#2) Shift all elements one position ahead. 
#3) Replace first element of array with x.
 

# Python3 code for program to 
# cyclically rotate an array by one
  
# Method for rotation
def rotate(arr, n):
    x = arr[n - 1]
      
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1];
          
    arr[0] = x;
  
  
# Driver function
arr= [1, 2, 3, 4, 5]
n = len(arr)
print ("Given array is")
for i in range(0, n):
    print (arr[i], end = ' ')
  
rotate(arr, n)
  
print ("\nRotated array is")
for i in range(0, n):
    print (arr[i], end = ' ')
  
# This article is contributed 
# by saloni1297
#Output

#Given array is 
#1 2 3 4 5 

#Rotated array is
#5 1 2 3 4 
#Time Complexity: O(n), as we need to iterate through all the elements. Where n is the number of elements in the array.
#Auxiliary Space: O(1), as we are using constant space.
#The above question can also be solved by using reversal algorithm.
#-----------------------------------------------------------------
#Another approach:

#We can use two pointers, say i and j which point to first and last element of array respectively. As we know in cyclic rotation we will bring last element to first and shift rest in forward direction, so start swapping arr[i] and arr[j] and keep j fixed and i moving towards j.  Repeat till i is not equal to j.



def rotate(arr, n):
    i = 0 
    j = n - 1
    while i != j:
      arr[i], arr[j] = arr[j], arr[i]
      i = i + 1
    pass
  
  
# Driver function
arr= [1, 2, 3, 4, 5]
n = len(arr)
print ("Given array is")
for i in range(0, n):
    print (arr[i], end = ' ')
  
rotate(arr, n)
  
print ("\nRotated array is")
for i in range(0, n):
    print (arr[i], end = ' ')
#Output
#Given array is 
#1 2 3 4 5 
#Rotated array is
#5 1 2 3 4 
#Time Complexity: O(n), as we need to iterate through all the elements. Where n is the number of elements in the array.
#Auxiliary Space: O(1), as we are using constant space.
#-----------------------------------------------------------------------

#Another approach(Using Slicing ):

#We can also solve this problem using slicing in python.  

#Implementation for the above approach:-

def rotateArray(array):
    '''
    array[-1:] taking last element
    array[:-1] taking elements from start to last second element
    array[:] changing array from starting to end
    '''
    array[:] = array[-1:]+array[:-1]
  
  
# create array
array = [1, 2, 3, 4, 5]
# send array to rotateArray function
rotateArray(array)
  
print(*array)  # 5 1 2 3 4
 
#Output
#5 1 2 3 4
#Time Complexity: O(n), as we are reversing the array. Where n is the number of elements in the array.
#Auxiliary Space: O(1), as we are using constant space.
