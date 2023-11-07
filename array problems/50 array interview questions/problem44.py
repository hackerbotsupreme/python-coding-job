#Find the missing and repeating number

#Difficulty Level : Medium
#---------------------------------------------------------------------
#Given an unsorted array of size n. Array elements are in the range of 1 to n. One number from set {1, 2, …n} is missing and one number occurs twice in the array. Find these two numbers.

#Examples: 

#Input: arr[] = {3, 1, 3}
#Output: Missing = 2, Repeating = 3
#Explanation: In the array, 2 is missing and 3 occurs twice 

#Input: arr[] = {4, 3, 6, 2, 1, 1}
#Output: Missing = 5, Repeating = 1
#Below are various methods to solve the problems: 

#Method 1 (Use Sorting)
#Approach: 

#Sort the input array.
#Traverse the array and check for missing and repeating.
#Time Complexity: O(nLogn)
#----------------------------------------------------------------------
#Thanks to LoneShadow for suggesting this method.

#Method 2 (Use count array)
#Approach: 

#Create a temp array temp[] of size n with all initial values as 0.
#Traverse the input array arr[], and do the following for each arr[i] 
#if(temp[arr[i]] == 0) temp[arr[i]] = 1;
#if(temp[arr[i]] == 1) output “arr[i]” //repeating
#Traverse temp[] and output the array element having value as 0 (This is the missing element)
#Time Complexity: O(n)
#Auxiliary Space: O(n)

#Method 3 (Use elements as Index and mark the visited places)
#Approach: 
#Traverse the array. While traversing, use the absolute value of every element as an index and make the value at this index negative to mark it visited. If something is already marked negative then this is the repeating element. To find the missing, traverse the array again and look for a positive value.


# Python3 code to Find the repeating
# and the missing elements
 
def printTwoElements( arr, size):
    for i in range(size):
        if arr[abs(arr[i])-1] > 0:
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
        else:
            print("The repeating element is ", abs(arr[i]))
             
    for i in range(size):
        if arr[i]>0:
            print("and the missing element is ", i + 1)
 
# Driver program to test above function */
arr = [7, 3, 4, 5, 5, 6, 2]
n = len(arr)
printTwoElements(arr, n)
 
# This code is contributed by "Abhishek Sharma 44"
#Output
#The repeating element is 5
#and the missing element is 1
#Time Complexity: O(n)
#Auxiliary Space: O(1) as it is using constant variables
#Thanks to Manish Mishra for suggesting this method. 

#Method 4 (Make two equations)
#Approach:

#Let x be the missing and y be the repeating element.
#Get the sum of all numbers using formula S = n(n+1)/2 – x + y
#Get product of all numbers using formula P = 1*2*3*…*n * y / x
#The above two steps give us two equations, we can solve the equations and get the values of x and y.
#Time Complexity: O(n)
#Thanks to disappearedng for suggesting this solution. 

#Note: This method can cause arithmetic overflow as we calculate the product and sum of all array elements.
#------------------------------------------------------------------

#Method 5 (Use XOR)

#Approach:

#Let x and y be the desired output elements.
#Calculate the XOR of all the array elements.
#xor1 = arr[0]^arr[1]^arr[2]…..arr[n-1]

#XOR the result with all numbers from 1 to n
#xor1 = xor1^1^2^…..^n

#In the result xor1, all elements would nullify each other except x and y. All the bits that are set in xor1 will be set in either x or y. So if we take any set bit (We have chosen the rightmost set bit in code) of xor1 and divide the elements of the array in two sets – one set of elements with the same bit set and another set with the same bit not set. By doing so, we will get x in one set and y in another set. Now if we do XOR of all the elements in the first set, we will get x, and by doing the same in the other set we will get y. 
#Below is the implementation of the above approach: 


# Python3 program to find the repeating
# and missing elements
 
# The output of this function is stored
# at x and y
def getTwoElements(arr, n):
     
    global x, y
    x = 0
    y = 0
     
    # Will hold xor of all elements
    # and numbers from 1 to n
    xor1 = arr[0]
     
    # Get the xor of all array elements
    for i in range(1, n):
        xor1 = xor1 ^ arr[i]
         
    # XOR the previous result with numbers
    # from 1 to n
    for i in range(1, n + 1):
        xor1 = xor1 ^ i
     
    # Will have only single set bit of xor1
    set_bit_no = xor1 & ~(xor1 - 1)
     
    # Now divide elements into two
    # sets by comparing a rightmost set
    # bit of xor1 with the bit at the same
    # position in each element. Also,
    # get XORs of two sets. The two
    # XORs are the output elements.
    # The following two for loops
    # serve the purpose
    for i in range(n):
        if (arr[i] & set_bit_no) != 0:
             
            # arr[i] belongs to first set
            x = x ^ arr[i]
        else:
             
            # arr[i] belongs to second set
            y = y ^ arr[i]
             
    for i in range(1, n + 1):
        if (i & set_bit_no) != 0:
             
            # i belongs to first set
            x = x ^ i
        else:
             
            # i belongs to second set
            y = y ^ i
         
    # x and y hold the desired
    # output elements
     
# Driver code
arr = [ 1, 3, 4, 5, 5, 6, 2 ]
n = len(arr)
     
getTwoElements(arr, n)
 
print("The missing element is", x,
      "and the repeating number is", y)
     
# This code is contributed by stutipathak31jan
#Output
# The missing element is 7 and the repeating number is 5
#Time Complexity: O(n)
#Auxiliary Space: O(1) as it is using constant space if the input array is excluded
#This method doesn’t cause overflow, but it doesn’t tell which one occurs twice and which one is missing. We can add one more step that checks which one is missing and which one is repeating. This can be easily done in O(n) time.

#Method 6 (Use a Map)
#Approach: 
#This method involves creating a Hashtable with the help of Map. In this, the elements are mapped to their natural index. In this process, if an element is mapped twice, then it is the repeating element. And if an element’s mapping is not there, then it is the missing element.

#Below is the implementation of the above approach: 


# Python3 program to find the
# repeating and missing elements
# using Maps
def main():
     
    arr = [ 4, 3, 6, 2, 1, 1 ]
     
    numberMap = {}
     
    max = len(arr)
    for i in arr:
        if not i in numberMap:
            numberMap[i] = True
             
        else:
            print("Repeating =", i)
     
    for i in range(1, max + 1):
        if not i in numberMap:
            print("Missing =", i)
main()
 
# This code is contributed by stutipathak31jan
#Output
Repeating = 1
Missing = 5
#Time Complexity: O(N)
#Auxiliary Space: (N)

#Method 7 (Make two equations using sum and sum of squares)
#Approach:

#Let x be the missing and y be the repeating element.
#Let N is the size of the array.
#Get the sum of all numbers using the formula S = N(N+1)/2
#Get the sum of square of all numbers using formula Sum_Sq = N(N+1)(2N+1)/6
#Iterate through a loop from i=1….N
#S -= A[i]
#Sum_Sq -= (A[i]*A[i])
#It will give two equations 
#x-y = S – (1) 
#x^2 – y^2 = Sum_sq 
#x+ y = (Sum_sq/S) – (2) 

def repeatedNumber(A):
     
    length = len(A)
    Sum_N = (length * (length + 1)) // 2
    Sum_NSq = ((length * (length + 1) *
                     (2 * length + 1)) // 6)
     
    missingNumber, repeating = 0, 0
     
    for i in range(len(A)):
        Sum_N -= A[i]
        Sum_NSq -= A[i] * A[i]
         
    missingNumber = (Sum_N + Sum_NSq //
                             Sum_N) // 2
    repeating = missingNumber - Sum_N
     
    ans = []
    ans.append(repeating)
    ans.append(missingNumber)
     
    return ans
 
# Driver code
v = [ 4, 3, 6, 2, 1, 6, 7 ]
res = repeatedNumber(v)
 
for i in res:
    print(i, end = " ")
 
# This code is contributed by stutipathak31jan
#Output
#6  5  
#Time Complexity: O(n) 
#Auxiliary Space: O(1)

#Thanks to Anish Shaha for suggesting this method.

#Method 8 (Using OR Operator):

#Approach:

#Given an input array 

#Performing OR operation on input array.
#At the same time checking if that number has occurred before, by determining if the position is already set or not. We will get the repeating number in this step.
#To find missing value we have to check the bit containing 0 using OR again.

# Python code for the above approach
class GFG:
    def main(args):
        # Input:
        arr = [4, 3, 6, 2, 1, 1]
        n = len(arr)
         
        # Declaring output variables
        # Note : arr[i]-1 is used instead of arr[i] as we want to use all 64 bits
        bitOr = (1 << (arr[0] - 1))
        repeating = 0
        missing = 0
         
        # Performing XOR as well as Checking repeating number
        for i in range(1, n):
           
            # If OR operation with 1 gives same output
            # that means, we already have 1 at that position
            if ((bitOr | (1 << (arr[i] - 1))) == bitOr):
                repeating = arr[i]
                continue
            bitOr = (bitOr | (1 << (arr[i] - 1)))
             
        # Checking missing number
        for i in range(1, n):
           
            # property: OR with 0 yield 1 hence value of bitOr changes
            if ((bitOr | (1 << i)) != bitOr):
                missing = i + 1
                break
 
        print("Repeating : " + str(repeating) + "\nMissing : " + str(missing))
 
if __name__ == "__main__":
    GFG.main([])
 
# This code is contributed by Mukul Jatav (mukulsomukesh)
#Output
#Repeating : 1
#Missing : 5
#Time Complexity: O(n)
#Auxiliary Space  O(1)

#Limitations of the approach: it only works on the size of array <= 64 if we use long and size of array <= 32

#Method 9: (Placing every element in its correct position)
#Approach: It is clear from the observation that if we sort an array, then arr[i] == i+1. If all elements in an array satisfy this condition, means this is an ideal case. So the idea is to sort the given array and traverse on it and check if arr[i] == i + 1 if so then increment i (because this element is at its correct position), otherwise, place this element (arr[i]) at its correct position (arr[arr[i] – 1) by swapping the arr[i] and arr[arr[i] -1]. This swapping will put the element arr[i] at its correct position (i.e arr[arr[i]-1]). After doing this operation gets over for all elements of the given array then again traverse over the array and check if arr[i] != i + 1 if so, then this is the duplicate element and i + 1 is the missing element.

#Below is the implementation of the above approach.


# Python program to find the missing
# and repeating element
def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
 
def getTwoElements(arr, n):
    repeating = 0
    missing = 0
 
    i = 0
 
    # Traverse on the array
    while (i < n):
 
        # If the element is on its correct position
        if (arr[i] == arr[arr[i] - 1]):
            i += 1
        else:
          # If it is not at its correct position
            # then palce it to its correct position
          swap(arr, i, arr[i] - 1)
 
    # Find repeating and missing
    for i in range(n):
 
        # If any element is not in its correct position
        if (arr[i] != i + 1):
            repeating = arr[i]
            missing = i + 1
            break
 
    # Print answer
    print("Repeating:", repeating)
    print("Missing:", missing)
 
# Driver code
arr = [2, 3, 1, 5, 1]
n = len(arr)
getTwoElements(arr, n)
 
# This code is contributed by Tapesh (tapeshdua420)

