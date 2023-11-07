#Find the row with maximum number of 1s

#Difficulty Level : Medium
#---------------------------------------------------------------------------
#Example:  

#Input matrix : 0 1 1 1
#                        0 0 1 1
#                        1 1 1 1  // this row has maximum 1s
#                        0 0 0 0
#Output: 2
#-------------------------------------------------------------
#A simple method is to do a row-wise traversal of the matrix, count the number of 1s in each row, and compare the count with the max. Finally, return the index of the row with a maximum of 1s. The time complexity of this method is O(m*n) where m is the number of rows and n is the number of columns in the matrix.

#Implementation:

# Python implementation of the approach
R,C = 4,4
 
# Function to find the index of first index
# of 1 in a boolean array arr
def first(arr , low , high):
 
    if(high >= low):
 
        # Get the middle index
        mid = low + (high - low)//2
     
        # Check if the element at middle index is first 1
        if ( ( mid == 0 or arr[mid-1] == 0) and arr[mid] == 1):
            return mid
     
        # If the element is 0, recur for right side
        elif (arr[mid] == 0):
            return first(arr, (mid + 1), high);
         
        # If element is not first 1, recur for left side
        else:
            return first(arr, low, (mid -1));
 
    return -1
 
# Function that returns index of row
# with maximum number of 1s.
def rowWithMax1s(mat):
 
    # Initialize max values
    max_row_index,Max = 0,-1
 
    # Traverse for each row and count number of 1s
    # by finding the index of first 1
    for i in range(R):
 
        index = first (mat[i], 0, C-1)
        if (index != -1 and C-index > Max):
            Max = C - index;
            max_row_index = i
 
    return max_row_index
 
# Driver Code
mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]
print("Index of row with maximum 1s is " + str(rowWithMax1s(mat)))
 
# This code is contributed by shinjanpatra
#Output
#Index of row with maximum 1s is 2
#Time Complexity:  O(m*n)
#Auxiliary Space:  O(1)



#We can do better. Since each row is sorted, we can use Binary Search to count 1s in each row. We find the index of the first instance of 1 in each row. The count of 1s will be equal to the total number of columns minus the index of the first 1.

#Implementation: See the following code for the implementation of the above approach.  

# Python3 program to find the row
# with maximum number of 1s
 
# Function to find the index
# of first index of 1 in a
# boolean array arr[]
def first( arr, low, high):
    if high >= low:
         
        # Get the middle index
        mid = low + (high - low)//2
 
        # Check if the element at
        # middle index is first 1
        if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1:
            return mid
 
        # If the element is 0,
        # recur for right side
        elif arr[mid] == 0:
            return first(arr, (mid + 1), high)
     
        # If element is not first 1,
        # recur for left side
        else:
            return first(arr, low, (mid - 1))
    return -1
 
# Function that returns
# index of row with maximum
# number of 1s.
def rowWithMax1s( mat):
     
    # Initialize max values
    R = len(mat)
    C = len(mat[0])
    max_row_index = 0
    max = -1
     
    # Traverse for each row and
    # count number of 1s by finding
    #  the index of first 1
    for i in range(0, R):
        index = first (mat[i], 0, C - 1)
        if index != -1 and C - index > max:
            max = C - index
            max_row_index = i
 
    return max_row_index
 
# Driver Code
mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]
print ("Index of row with maximum 1s is",
      rowWithMax1s(mat))
 
# This code is contributed
# by shreyanshi_arun
#Output
#Index of row with maximum 1s is 2
#Time Complexity: O(m log n) where m is the number of rows and n is the number of columns in the matrix.
#-------------------------------------------------------------------
#The above solution can be optimized further. Instead of doing a binary search in every row, we first check whether the row has more 1s than max so far. If the row has more 1s, then only count 1s in the row. Also, to count 1s in a row, we don’t do a binary search in a complete row, we do a search before the index of the last max. 

#Implementation: Following is an optimized version of the above solution.  

# The main function that returns index
# of row with maximum number of 1s.
def rowWithMax1s(mat) : 
 
    # Initialize max using values from first row.
    max_row_index = 0;
    max = first(mat[0], 0, C - 1)
 
    # Traverse for each row and count number of 1s
    # by finding the index of first 1
    for i in range(1, R):
       
        # Count 1s in this row only if this row
        # has more 1s than max so far
 
        # Count 1s in this row only if this row
        # has more 1s than max so far
        if (max != -1 and mat[i][C - max - 1] == 1):
           
            # Note the optimization here also
            index = first (mat[i], 0, C - max)
 
            if (index != -1 and C - index > max):
                max = C - index
                max_row_index = i
        else:
            max = first(mat[i], 0, C - 1)
           
    return max_row_index;
 
# This code is contributed by Dharanendra L V
# Time complexity: O(m log n), 
#Auxiliary Space:  O(log n)

#Thanks to Naveen Kumar Singh for suggesting the above solution. 

#The worst case of the above solution occurs for a matrix like following. 
#0 0 0 … 0 1 
#0 0 0 ..0 1 1 
#0 … 0 1 1 1 
#….0 1 1 1 1

#Following method works in O(m+n) time complexity in worst case. 

#Step1: Get the index of first (or leftmost) 1 in the first row.
#Step2: Do following for every row after the first row 
#…IF the element on left of previous leftmost 1 is 0, ignore this row. 
#…ELSE Move left until a 0 is found. Update the leftmost index to this index and max_row_index to be the current row.
#The time complexity is O(m+n) because we can possibly go as far left as we came ahead in the first step.
#Implementation: Following is the implementation of this method.
#----------------------------------------------------------------------
#Implementation: Following is the implementation of this method.

# Python3 program to find the row
# with maximum number of 1s
 
# Function that returns
# index of row with maximum
# number of 1s.
def rowWithMax1s( mat):
     
    # Initialize max values
    R = len(mat)
    C = len(mat[0])
    max_row_index = 0
    index=C-1;
    # Traverse for each row and
    # count number of 1s by finding
    # the index of first 1
    for i in range(0, R):
      flag=False #to check whether a row has more 1's than previous
      while(index >=0 and mat[i][index]==1):
        flag=True #present row has more 1's than previous
        index-=1
        if(flag): #if the present row has more 1's than previous
          max_row_index = i
      if max_row_index==0 and mat[0][C-1]==0:
        return 0;
    return max_row_index
 
# Driver Code
mat = [[0, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]]
print ("Index of row with maximum 1s is",
    rowWithMax1s(mat))
 
# This code is contributed
# by Rishabh Chauhan
#Output
#Index of row with maximum 1s is 2
#Time Complexity: O(m+n) where m is the number of rows and n is the number of columns in the matrix.
#Auxiliary Space:  O(1)