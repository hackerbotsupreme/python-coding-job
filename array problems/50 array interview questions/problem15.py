#Find duplicates in O(n) time and O(1) extra space | Set 1

#Difficulty Level : Medium
#-----------------------------------------------------------------------
#Given an array of n elements that contains elements from 0 to n-1, with any of these numbers appearing any number of times. Find these repeating numbers in O(n) and using only constant memory space.

#Example: 

#Input : n = 7 and array[] = {1, 2, 3, 6, 3, 6, 1}
#Output: 1, 3, 6

#Explanation: The numbers 1 , 3 and 6 appears more
#than once in the array.

#Input : n = 5 and array[] = {1, 2, 3, 4 ,3}
#Output: 3

#Explanation: The number 3 appears more than once
#in the array.
#----------------------------------------------------------------------
#This problem is an extended version of the following problem. 
#Find the two repeating elements in a given array 
#Method 1 and Method 2 of the above link are not applicable as the question says O(n) time complexity and O(1) constant space. Also, Method 3 and Method 4 cannot be applied here because there can be more than 2 repeating elements in this problem. Method 5 can be extended to work for this problem. Below is the solution that is similar to Method 5.

#Complete Interview Preparation - GFG

#Efficient approach:

#Approach: The elements in the array is from 0 to n-1 and all of them are positive. So to find out the duplicate elements, a HashMap is required, but the question is to solve the problem in constant space. There is a catch, the array is of length n and the elements are from 0 to n-1 (n elements). The array can be used as a HashMap. 
#Problem in the below approach. This approach only works for arrays having at most 2 duplicate elements i.e It will not work if the array contains more than 2 duplicates of an element. For example: {1, 6, 3, 1, 3, 6, 6} it will give output as : 1 3 6 6.
#Note: The above program doesn’t handle 0 cases (If 0 is present in array). The program can be easily modified to handle that also. It is not handled to keep the code simple. (Program can be modified to handle 0 cases by adding plus One(+1) to all the values. also subtracting One from the answer and by writing { arr [abs(arr[i]) – 1] } in code)
#In other approach below, the discussed solution prints repeating elements only once.

#Approach: The basic idea is to use a HashMap to solve the problem. But there is a catch, the numbers in the array are from 0 to n-1, and the input array has length n. So, the input array can be used as a HashMap. While Traversing the array, if an element ‘a’ is encountered then increase the value of a%n‘th element by n. The frequency can be retrieved by dividing the a % n’th element by n.
#Algorithm: 
#Traverse the given array from start to end.
#For every element in the array increment the arr[i]%n‘th element by n.
#Now traverse the array again and print all those indexes i for which arr[i]/n is greater than 1. Which guarantees that the number n has been added to that index
#This approach works because all elements are in the range from 0 to n-1 and arr[i] would be greater than n only if a value “i” has appeared more than once.
#Below is the implementation of the above approach:



# Python3 code to find duplicates in O(n) time
numRay = [0, 4, 3, 2, 7, 8, 2, 3, 1]
arr_size = len(numRay)
for i in range(arr_size):
 
    x = numRay[i] % arr_size
    numRay[x] = numRay[x] + arr_size
 
print("The repeating elements are : ")
for i in range(arr_size):
    if (numRay[i] >= arr_size*2):
        print(i, " ")
 
# This code is contributed by 29AjayKumar
#Output
#The repeating elements are : 
#2 
#3 
#Complexity Analysis: 

#Time Complexity: O(n), Only two traversals are needed. So the time complexity is O(n).
#Auxiliary Space: O(1), No extra space is needed, so the space complexity is constant.
#-------------------------------------
#Another efficient approach: Modifying array by making visited elements -ve (visited once) or greater than n (visited twice or more)

#Approach:
#Increment the array elements by 1 (arr[i]+1) to handle occurrence of 0. Traverse the array and for every element that has been visited the first time, make the element at index equal to the value of the current element as negative. If element has already been visited before, add it (arr[i]-1) to result vector and make the element at index equal to the value of current element more than n (by multiplying it with (n+1)) to avoid adding it to result vector, incase it occurs again. 
#Algorithm:
#Traverse the array and increment each element  by 1. This is done to remove occurrence of 0 from the array. Later, while adding the duplicate elements in the result vector, we decrement elements by 1 to get actual value.
#Declare result vector.
#Declare a count variable to count the occurrence of (n-1)th element in the array. 
#For eg : array = [0,2,4,3,4], n=5, then we need the count variable to count the occurrence of 4. 
#In the algorithm, we need to access elements present at index equal to other element values, meaning we have to access values like array[array[i]]. For eg: if i=0, we access array[array[i]] = array[array[0]] = array[1] = 2. Similarly, we might need to access the element at index equal to largest value possible in the array, i.e., n-1 (array[array[n-1]]). However, we incremented each element by 1 and thus largest possible element in the array became n. In 0-based indexing array[n] returns garbage value  and thus our algorithm cannot calculate the occurrence of the largest possible element in the array. Hence we need the count variable to count its occurrence separately and later add it to result vector if found duplicate.
#Run a for loop from 0 to n and in each iteration of the loop:
#Calculate index value – 
#Since we need to access elements present at index equal to other element values, index is the absolute value of arr[i]. If abs(arr[i]) is greater than n, then index is equal to abs(arr[i])/(n+1) else abs(arr[i]). 
#If an element ‘x’ occurs twice in the array, we negate the element present at x, i.e., array[x] = -array[x], but if it occurs more than twice, then, to avoid it from getting pushed to result vector again, we make element at x equal to a number greater than n (a number that would never occur in the array). To do this, we multiply it by (n+1), i.e., array[x] = array[x]*(n+1). We cannot multiply with n as if array[x] = 1, then array[x]*n = n, which is the largest possible element and can occur in the array. 
#Thus, during traversal, if we come across array[x] which is greater than n, we need to calculate array[x]/(n+1) to get the original value of index.
 
#Check if obtained index value is equal to n, if so, increment the count variable and move to the next iteration, as we will calculate the occurrence of n separately.
 
#Get the value of element at calculated index in a variable and run the following else-if conditions:
#If this value is less than 0 (-ve), it means that element equal to its index has appeared twice, thus push the value of index-1 (as element values had been incremented earlier) in result vector. Going forward, as this index value has already been pushed to result vector, we don’t want a duplicate in result vector if it occurs again and thus, make the value of the element present at this index greater than n by multiplying it with (n+1).
#If this value is greater than n, it means that element equal to the index value has already been pushed to result vector and nothing needs to be done. So just continue to the next iteration.
#If this value is between 0 and n, it means that the element equal to the index value has appeared for the first time and thus make it negative.
 
#After exiting from the for loop, if the value of count variable is more than 1, it means that the largest possible element (n) has duplicates in the array and thus, push (n-1) to result vector.
#Check if size of result vector is 0, if so, push -1 as there are no duplicates. Otherwise, sort the result vector
#Return the result vector.
#Below is the implementation of the above approach:

# Python3 code for above approach
def duplicates(arr, n):
   
    # Increment array elements by 1
    for i in range(n):
        arr[i] = arr[i] + 1
         
    # result vector
    res = []
     
    # count variable for count of
    # largest element
    count = 0
    for i in range(n):
       
        # Calculate index value
        if(abs(arr[i]) > n):
            index = abs(arr[i])//(n+1)
        else:
            index = abs(arr[i])
             
        # Check if index equals largest element value
        if(index == n):
            count += 1
            continue
             
        # Get element value at index
        val = arr[index]
         
        # Check if element value is negative, positive
        # or greater than n
        if(val < 0):
            res.append(index-1)
            arr[index] = abs(arr[index]) * (n + 1)
        elif(val>n):
            continue
        else:
            arr[index] = -arr[index]
             
    # If largest element occurs more than once
    if(count > 1):
        res.append(n - 1)
    if(len(res) == 0):
        res.append(-1)
    else:
        res.sort()
    return res
   
# Driver Code
numRay = [ 0, 4, 3, 2, 7, 8, 2, 3, 1 ]
n = len(numRay)
ans = duplicates(numRay,n)
for i in ans:
    print(i)
     
 # This code is contributed by Vibhu Karnwal
#Output
#2 
#3 
#Complexity Analysis:

#Time Complexity: O(n), Only two traversals are needed. So the time complexity is O(n).
#Auxiliary Space: O(1). 
