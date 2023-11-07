#Trapping Rain Water

#Difficulty Level : Hard
#---------------------------------------------------------------------
#Given an array of N non-negative integers arr[] representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

#Examples:  

#Input: arr[] = {2, 0, 2}
#Output: 2
#Explanation: The structure is like below.
#We can trap 2 units of water in the middle gap.



#Input: arr[]   = {3, 0, 2, 0, 4}
#Output: 7
#Explanation: Structure is like below.
#We can trap “3 units” of water between 3 and 2,
#“1 unit” on top of bar 2 and “3 units” between 2 and 4.



#Input: arr[] = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
#Output: 6
#Explanation: The structure is like below.
#Trap “1 unit” between first 1 and 2, “4 units” between
#first 2 and 3 and “1 unit” between second last 1 and last 2
#----------------------------------------------------------------------

#Complete Interview Preparation - GFG
#Intuition: The basic intuition of the problem is as follows:

#An element of the array can store water if there are higher bars on the left and the right. 
#The amount of water to be stored in every position can be found by finding the heights of bars on the left and right sides. 
#The total amount of water stored is the summation of the water stored in each index.
#For example – Consider the array arr[] = {3, 0, 2, 0, 4}. 
#Three units of water can be stored in two indexes 1 and 3, and one unit of water at index 2.
#Water stored in each index = 0 + 3 + 1 + 3 + 0 = 7  



#Approach 1 (Brute Approach): This approach is the brute approach. The idea is to:

#Traverse every array element and find the highest bars on the left and right sides. Take the smaller of two heights. The difference between the smaller height and the height of the current element is the amount of water that can be stored in this array element.

#Follow the steps mentioned below to implement the idea:

#Traverse the array from start to end:
#For every element: 
#Traverse the array from start to that index and find the maximum height (a) and 
#Traverse the array from the current index to the end, and find the maximum height (b).
#The amount of water that will be stored in this column is min(a,b) – array[i], add this value to the total amount of water stored
#Print the total amount of water stored.
#Below is the implementation of the above approach.

# Python3 implementation of the approach
  
# Function to return the maximum
# water that can be stored
def maxWater(arr, n):
  
    # To store the maximum water
    # that can be stored
    res = 0
  
    # For every element of the array
    for i in range(1, n - 1):
  
        # Find the maximum element on its left
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])
  
        # Find the maximum element on its right
        right = arr[i]
  
        for j in range(i + 1, n):
            right = max(right, arr[j])
  
        # Update the maximum water
        res = res + (min(left, right) - arr[i])
  
    return res
  
  
# Driver code
if __name__ == "__main__":
  
    arr = [0, 1, 0, 2, 1, 0,
           1, 3, 2, 1, 2, 1]
    n = len(arr)
  
    print(maxWater(arr, n))
  
# This code is contributed by AnkitRai01
#Output
#6
#Complexity Analysis: 

#Time Complexity: O(N2). There are two nested loops traversing the array.
#Space Complexity: O(1). No extra space is required.
#----------------------------------------------------------------
#Approach 2 (Precalculation): This is an efficient solution based on the precalculation concept:

#In previous approach, for every element we needed to calculate the highest element on the left and on the right. 

#So, to reduce the time complexity: 

#For every element we can precalculate and store the highest bar on the left and on the right (say stored in arrays left[] and right[]). 
#Then iterate the array and use the precalculated values to find the amount of water stored in this index, 
#which is the same as ( min(left[i], right[i]) – arr[i] )
#Follow the below illustration for a better understanding:

#Illustration:

#Consider arr[] = {3, 0, 2, 0, 4}

#Therefore, left[] = {3, 3, 3, 3, 4} and right[] = {4, 4, 4, 4, 4}
#Now consider iterating using i from 0 to end

#For i = 0:
#        => left[0] = 3, right[0] = 4 and arr[0] = 3
#        => Water stored = min(left[0], right[0]) – arr[0] = min(3, 4) – 3 = 3 – 3 = 0
#        => Total = 0 + 0 = 0

#For i = 1:
#        => left[1] = 3, right[1] = 4 and arr[1] = 0
#        => Water stored = min(left[1], right[1]) – arr[1] = min(3, 4) – 0 = 3 – 0 = 3
#        => Total = 0 + 3 = 3

#For i = 2:
#        => left[2] = 3, right[2] = 4 and arr[2] = 2
#        => Water stored = min(left[2], right[2]) – arr[2] = min(3, 4) – 2 = 3 – 2 = 1
#        => Total = 3 + 1 = 4

#For i = 3:
#        => left[3] = 3, right[3] = 4 and arr[3] = 0
#        => Water stored = min(left[3], right[3]) – arr[3] = min(3, 4) – 0 = 3 – 0 = 3
#        => Total = 4 + 3 = 7

#For i = 4:
#        => left[4] = 4, right[4] = 4 and arr[4] = 4
#        => Water stored = min(left[4], right[4]) – arr[4] = min(4, 4) – 4 = 4 – 4 = 0
#        => Total = 7 + 0 = 7

#So total rain water trapped = 7

#Follow the steps mentioned below to implement the approach:

#Create two arrays left[] and right[] of size N. Create a variable (say max) to store the maximum found till a certain index during traversal.
#Run one loop from start to end: 
#In each iteration update max and also assign left[i] = max.
#Run another loop from end to start: 
#In each iteration update max found till now and also assign right[i] = max.
#Traverse the array from start to end.
#The amount of water that will be stored in this column is min(left[i], right[i]) – array[i]
#dd this value to the total amount of water stored
#Print the total amount of water stored.
#Below is the implementation of the above approach.

# Python program to find maximum amount of water that can
# be trapped within given set of bars.
  
  
def findWater(arr, n):
  
    # left[i] contains height of tallest bar to the
    # left of i'th bar including itself
    left = [0]*n
  
    # Right [i] contains height of tallest bar to
    # the right of ith bar including itself
    right = [0]*n
  
    # Initialize result
    water = 0
  
    # Fill left array
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i-1], arr[i])
  
    # Fill right array
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i + 1], arr[i])
  
    # Calculate the accumulated water element by element
    # consider the amount of water on i'th bar, the
    # amount of water accumulated on this particular
    # bar will be equal to min(left[i], right[i]) - arr[i] .
    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]
  
    return water
  
  
# Driver program
if __name__ == '__main__':
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    n = len(arr)
    print(findWater(arr, n))
  
# This code is contributed by
# Smitha Dinesh Semwal
#Output
#6
#Complexity Analysis:

#Time Complexity: O(N). Only one traversal of the array is needed, So time Complexity is O(N).
#Space Complexity: O(N). Two extra arrays are needed, each of size N.
#--------------------------------------------------------------------


#Approach 3 (Using Stack): The idea to solve the problem using stack is as follows:

#We can use a stack to track the bars that are bounded by the higher left and right bars. This can be done using only one iteration.

#For this we will keep pushing elements in stack, until an element with higher value than the stack top is found. This denotes that there is a chance of storing position on the left side of the current element with the current bar being an end.
#So remove the smaller element on left and find the left bar (which is the current top of stack) and the amount of water stored by the left end bar and the current bar being the right end. Continue this till the stack is not empty or a higher value element is found.
#Follow the below illustration for a better understanding.

#Illustration:

#Consider the array arr[] = {3, 0, 2, 0, 4} and an empty stack st.

#For i = 0:
#        => The stack is empty. So no elements with higher value on left.
#        => Push the index into the stack. st = {0} [to keep track of the distance in between]

#For i = 1:
#        => arr[1] is less than arr[stack top]. So arr[1] has a higher left bound.
#        => Push the index into stack. st = {0, 1}

#For i = 2:
#        => arr[2] is greater than arr[stack top]. So arr[2] is the higher right bound of current stack top.
#        => Calculate the water stored in between the left and right bound of the stack top. 
#        => The stack top is the base height in between the left and right bound.
#        => Pop the stack top. So st = {0}.
#        => Water stored in between when arr[0] and arr[2] are the bound= {min(arr[0], arr[2]) – arr[1]} * (2 – 0 – 1) = 2.
#        => arr[0] is greater than arr[2] Push the index into stack. st = {0, 2}.
#        => Total water stored = 0 + 2 = 2.

#For i = 3:
#        => arr[3] is less than arr[2]. So arr[3] has a higher left bound.
#        => Push the index into the stack. st = {0, 2, 3}.

#For i = 4:
#        => arr[4] is greater than arr[stack top]. So arr[4] is the higher right bound of current stack top.
#        => Calculate the water stored in same way as for i = 2. The base height is arr[3].
#        => Pop the stack top. So st = {0, 2}.
#        => Water stored in between when arr[4] and arr[2] are the bound= {min(arr[4], arr[2]) – arr[3]} * (4 – 2 – 1) = 2.
#        => arr[4] is greater than arr[2].
#        => Pop the stack. st = {0}.
#        => Water stored in between arr[0] and arr[4] when arr[2] is the base height = {min(3, 4) – 2} * (4 – 0 – 1) = 3
#        => arr[0] less than arr[4]. So pop stack. st = {}.
#        => As no element left in the stack push the index. st = {4}.
#        => Total water stored = 2 + 2 + 3 = 7.

#So the total amount of water stored  = 7.

#Follow the steps mentioned below to implement the idea:

#Loop through the indices of the bar array.
#For each bar, do the following:
#Loop while the Stack is not empty and the current bar has a height greater than the top bar of the stack,
#Store the index of the top bar in pop_height and pop it from the Stack.
#Find the distance between the left bar(current top) of the popped bar and the current bar.
#Find the minimum height between the top bar and the current bar.
#The maximum water that can be trapped is distance * min_height.
##The water trapped, including the popped bar, is (distance * min_height) – height[pop_height].
#Add that to the answer.
#Return the amount received as the total amount of water
#Below is the implementation of the above approach.

# Python implementation of the approach
  
# Function to return the maximum
# water that can be stored
  
  
def maxWater(height):
  
    # Stores the indices of the bars
    stack = []
  
    # size of the array
    n = len(height)
  
    # Stores the final result
    ans = 0
  
    # Loop through the each bar
    for i in range(n):
  
        # Remove bars from the stack
        # until the condition holds
        while(len(stack) != 0 and (height[stack[-1]] < height[i])):
  
            # store the height of the top
            # and pop it.
            pop_height = height[stack[-1]]
            stack.pop()
  
            # If the stack does not have any
            # bars or the popped bar
            # has no left boundary
            if(len(stack) == 0):
                break
  
            # Get the distance between the
            # left and right boundary of
            # popped bar
            distance = i - stack[-1] - 1
  
            # Calculate the min. height
            min_height = min(height[stack[-1]], height[i])-pop_height
  
            ans += distance * min_height
  
        # If the stack is either empty or
        # height of the current bar is less than
        # or equal to the top bar of stack
        stack.append(i)
  
    return ans
  
  
# Driver code
if __name__ == '__main__':
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(maxWater(arr))
  
# This code is contributed by rag2127
#Output
#6
#Time Complexity: O(N)
#Auxiliary Space: O(N)
#----------------------------------------------------------------------

#Approach 4 (Horizontal scan method): The idea is as follows:

#If max_height is the height of the tallest block, then it will be the maximum possible height for any trapped rainwater. 
#And if for each unit of height we find the leftmost and the rightmost boundary for that height, we can consider all the blocks in between contain that amount of water. 
#But this will consider the height of the bars also. So we have to subtract that from the total water trapped.
#This can be justified as follows. Say the sections for a certain height is {i1, i2}, {i2, i3}, . . ., {ik-1, ik}
#So the water stored in between for a single unit of height is the difference in between the indices
#= (i2 – i1 – 1) + (i3 – i2 – 1) + . . . + (ik – ik-1 -1}) = ik – i1 – (k-1) where k is the number of bars in between.

#But as we are considering all the blocks in between left and right boundary, it considers all the bars also.
#So the trapped water for a single unit becomes (ik – i1 + 1)

#Follow the below illustration for a better understanding.

#Illustration:

#Consider array arr[] = {3, 0, 2, 0, 4}.
#max_height = 4 and sum of all blocks = 2 + 3 + 4 = 9.

#For height = 1:
#        => leftmost boundary = 0 and rightmost boundary = 4.
#        => All blocks in between contain 1 height of water. 
#        => So amount of water trapped = (4 – 0 + 1) = 5
#        => Total trapped water = 0+5 = 5

# For height = 2:
#        => leftmost boundary = 0 and rightmost boundary = 4.
 #       => All blocks in between contain 2 height of water.
#        => Earlier we have considered water columns with height 1. So there is increase of 1 unit in height. 
#        => So amount of water trapped = (4 – 0 + 1) = 5
#        => Total trapped water = 5 + 5 = 10

#For height = 3:
#        => leftmost boundary = 0 and rightmost boundary = 4.
#        => All blocks in between contain 3 height of water.
#        => Earlier we have considered water columns with height 2. So there is increase of 1 unit in height. 
#        => So amount of water trapped = (4 – 0 + 1) = 5
#        => Total trapped water = 10 + 5 = 15

#For height = 4:
#        => leftmost boundary = 4 and rightmost boundary = 4.
#        => All blocks in between contain 4 height of water. 
#        => Earlier we have considered water columns with height 3. So there is increase of 1 unit in height. 
#        => So amount of water trapped = (4 – 4 + 1) = 1
#        => Total trapped water = 15 + 1 = 16

#So total water trapped  = 16 – total space taken by bars = 16 – 9 = 7.

#Follow the steps mentioned below to implement the idea:

#Find the total number of blocks, i.e., the sum of the heights array, num_blocks
#Find the maximum height, max_height
#Store total water in a variable, total = 0
#Keep two pointers, left = 0 and right = N -1, to store the leftmost and the rightmost boundaries for each unit of height
#For each height, i from 1 to max_height, do the following
#Find the leftmost and the rightmost boundary for the current height.
#As mentioned earlier we can consider all the blocks in between these to have at least i unit of water.
#Add this amount of water to the total trapped water.
#After the iteration is over, subtract num_blocks from total as we have considered them as water height during calculation.
#Below is the implementation of the above approach.

# Python code to implement the approach
  
def trappedWater(arr):
    num_blocks = 0
    n = 0
    max_height = float('-inf')
  
    # Find total blocks, max height and length of array
    for height in arr:
        num_blocks += height
        n += 1
        max_height = max(max_height, height)
  
    # Total water, left pointer and right pointer 
    # initialized to 0 and n - 1
    total = 0
    left = 0
    right = n - 1
  
    for i in range(1, max_height+1):
          
        # Find leftmost point greater than current row (i)
        while arr[left] < i:
            left += 1
          
        # Find rightmost point greater than current row (i)
        while arr[right] < i:
            right -= 1
          
        # Water in this row = right - left + 1
        total += (right - left + 1)
      
    total -= num_blocks
    return total
  
# Driver code
if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trappedWater(arr))
#Output
#6
#Time Complexity: O(max (max_height, N))
#Space Complexity: O(1)

#Approach 5 (Two Pointer Approach): The idea for this approach is as follows:

#At every index, The amount of rainwater stored is the difference between the current index height and a minimum of left max height and right max-height.

#Here we can use the two-pointer approach to find the minimum among the left-max and right-max of the probable outermost boundary for any index and iterate likewise.

#For example: 

#Say we have indices i, j and a boundary of (left, right). where i is the left pointer and j is the right pointer.
#If the minimum is arr[left], we can say that i is bounded in one side by left and no matter whatever the values are in between (i, right), the rightmost boundary of i will at  least have height arr[right] which is the probable outermost boundary for i. 
#So the water height of water column at index i is arr[left] – arr[i] and we can increment i then.
#Similar things happen for j also.
#Follow the below illustration for a better understanding:

#Illustration:

#Consider ar[] = {3, 0, 2, 0, 4}
#left = 0, right = 4, l_max = 0, r_max = 0.

#left = 0, right = 4:
#        => l_max = r_max.
#        => water added = 0
#        => r_max = 4, l_max = 0
#        => right = 3, left = 0

#left = 0, right = 3:
#        => l_max < r_max.
#        => water added = 0
#        => r_max = 4, l_max = 3
#        => right = 3, left = 1

#left = 1, right = 3:
#        => l_max < r_max.
#        => water added = 3 – 0 = 3
#        => r_max = 4, l_max = 3
#        => right = 3, left = 2
#        => Water trapped = 0 + 3 = 3

#left = 2, right = 3:
#        => l_max < r_max.
#        => water added = 3 – 2 = 1
#        => r_max = 4, l_max = 3
#        => right = 3, left = 2
#        => Water trapped = 3 + 1 = 4

#left = 3, right = 3:
#        => l_max < r_max.
#        => water added = 3 – 0 = 3
#        => r_max = 4, l_max = 3
#        => right = 3, left = 4
#        => Water trapped = 4 + 3 = 7

#So total water trapped = 7

#Follow the steps mentioned below to implement the idea:

#Take two pointers l and r. Initialize l to the starting index 0 and r to the last index N-1.
#Since l is the first element, left_max would be 0, and right_max for r would be 0.
#While l ≤ r, iterate the array. We have two possible conditions
#Condition1 : left_max <= right max
#Consider Element at index l
#Since we have traversed all elements to the left of l, left_max is known 
#For the right max of l, We can say that the right max would  always be >= current r_max here
#So, min(left_max,right_max) would always equal to left_max in this case
#Increment l.
#Condition2 : left_max > right max
#Consider Element at index r
#Since we have traversed all elements to the right of r, right_max is known
#For the left max of l, We can say that the left max would  always be >= current l_max here
#So, min(left_max,right_max) would always equal to right_max in this case
#Decrement r.
#Below is the implementation of the above approach.

# Python3 implementation of the approach
  
# Function to return the maximum
# water that can be stored
  
  
def maxWater(arr, n):
      
    # Indices to traverse the array
    left = 0
    right = n-1
  
    # To store Left max and right max 
    # for two pointers left and right
    l_max = 0
    r_max = 0
  
    # To store the total amount 
    # of rain water trapped
    result = 0
    while (left <= right):
          
        # We need check for minimum of left 
        # and right max for each element
        if r_max <= l_max:
              
            # Add the difference between 
            #current value and right max at index r
            result += max(0, r_max-arr[right])
              
            # Update right max
            r_max = max(r_max, arr[right])
              
            # Update right pointer
            right -= 1
        else:
              
            # Add the difference between 
            # current value and left max at index l
            result += max(0, l_max-arr[left])
              
            # Update left max
            l_max = max(l_max, arr[left])
              
            # Update left pointer
            left += 1
    return result
  
  
# Driver code
if __name__ == '__main__':
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    N = len(arr)
    print(maxWater(arr, N))
  
# This code is contributed by Nikhil Chatragadda
#Output
#6
#Time Complexity: O(N)
#Auxiliary Space: O(1) 

#Approach 6 (Similar to linear search): Here another efficient solution has been shown.

#The concept is that if there is a larger bar to the right, then the water can be retained with a height equal to the smaller bar on the left. 
#If there are no larger bars to the right, then start from the right. There must be a larger bar to the left now. 

#Follow the steps mentioned below to implement the idea:

#Loop from index 0 to the end of the given array.
#If a bar greater than or equal to the previous bar is encountered, then store the index of that bar (say prev_index).
#Keep adding the previous bar’s height minus the current (ith) bar to the final answer.
#Have a temporary variable to store the amount of water in the current segment.
#If no bar greater than or equal to the previous bar is found, then quit.
#If prev_index < size of the input array, then subtract the temporary variable from the answer, because we have considered the last segment that has no higher right bound.
#Loop from the end of the input array to prev_index.
#Find a bar greater than or equal to the previous bar (in this case, the last bar from backward).
#Below is the implementation of the above approach.

# Python3 implementation of the approach
  
# Function to return the maximum
# water that can be stored
  
  
def maxWater(arr, n):
    size = n - 1
  
    # Let the first element be stored as
    # previous, we shall loop from index 1
    prev = arr[0]
  
    # To store previous wall's index
    prev_index = 0
    water = 0
  
    # To store the water until a larger wall
    # is found, if there are no larger walls
    # then delete temp value from water
    temp = 0
    for i in range(1, size + 1):
  
        # If the current wall is taller than
        # the previous wall then make current
        # wall as the previous wall and its
        # index as previous wall's index
        # for the subsequent loops
        if (arr[i] >= prev):
            prev = arr[i]
            prev_index = i
  
            # Because larger or same height wall is found
            temp = 0
        else:
  
            # Since current wall is shorter than
            # the previous, we subtract previous
            # wall's height from the current wall's
            # height and add it to the water
            water += prev - arr[i]
  
            # Store the same value in temp as well
            # If we dont find any larger wall then
            # we will subtract temp from water
            temp += prev - arr[i]
  
    # If the last wall was larger than or equal
    # to the previous wall then prev_index would
    # be equal to size of the array (last element)
    # If we didn't find a wall greater than or equal
    # to the previous wall from the left then
    # prev_index must be less than the index
    # of the last element
    if (prev_index < size):
  
        # Temp would've stored the water collected
        # from previous largest wall till the end
        # of array if no larger wall was found then
        # it has excess water and remove that
        # from 'water' var
        water -= temp
  
        # We start from the end of the array, so previous
        # should be assigned to the last element
        prev = arr[size]
  
        # Loop from the end of array up to the 'previous index'
        # which would contain the "largest wall from the left"
        for i in range(size, prev_index - 1, -1):
  
            # Right end wall will be definitely smaller
            # than the 'previous index' wall
            if (arr[i] >= prev):
                prev = arr[i]
            else:
                water += prev - arr[i]
  
    # Return the maximum water
    return water
  
  
# Driver code
if __name__ == '__main__':
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    N = len(arr)
    print(maxWater(arr, N))
  
# This code is contributed by Mohit Kumar
Output
6
Time Complexity: O(N)
Auxiliary Space: O(1). 