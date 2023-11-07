#Longest Consecutive Subsequence
#
#Difficulty Level : Medium

#-----------------------------------------------------------------------------
#Given an array of integers, find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order. 

#Examples:  

#Input: arr[] = {1, 9, 3, 10, 4, 20, 2}
#Output: 4
#Explanation: The subsequence 1, 3, 4, 2 is the longest subsequence of consecutive elements

#Input: arr[] = {36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42}
#Output: 5
#Explanation: The subsequence 36, 35, 33, 34, 32 is the longest subsequence of consecutive elements.


#Recommended Problem
#Longest consecutive subsequence
#Hash
#Data Structures
#Amazon
#Microsoft
#+1 more
#Solve Problem
#Submission count: 2.1L
#Naive Approach:
#The idea is to first sort the array and find the longest subarray with consecutive elements. After sorting the array and removing the multiple occurrences of elements, run a loop and keep a count and max (both initially zero). Run a loop from start to end and if the current element is not equal to the previous (element+1) then set the count to 1 else increase the count. Update max with a maximum of count and max. 

 
 #Illustration:

#Input: arr[] = {1, 9, 3, 10, 4, 20, 2}



#First sort the array to arrange them in a consecutive fashion.
#arr[] = {1, 2, 3, 4, 9, 10, 20}

#Now, store the distinct elements from the sorted array.
#dist[] = {1, 2, 3, 4, 9, 10, 20}

#Initialize countConsecutive with 0 which will increment when arr[i] == arr[i – 1] + 1 is true otherwise countConsecutive will re-initialize by 1.

#Maintain a variable ans to store the maximum count of consecutive elements so far.

#At i = 0:

#as i is 0 then re-initialize countConsecutive by 1.
#ans = max(ans, countConsecutive) = max(0, 1) = 1
#At i = 1:


#check if (dist[1] == dist[0] + 1) = (2 == 1 + 1) = true
#as the above condition is true, therefore increment countConsecutive by 1
#countConsecutive = countConsecutive + 1 = 1 + 1 = 2
#ans = max(ans, countConsecutive) = max(1, 2) = 1
#At i = 2:

#check if (dist[2] == dist[1] + 1) = (3 == 2 + 1) = true
#as the above condition is true, therefore increment countConsecutive by 1
#countConsecutive = countConsecutive + 1 = 2 + 1 = 3
#ans = max(ans, countConsecutive) = max(2, 3) = 3
#At i = 3:

#check if (dist[3] == dist[2] + 1) = (4 == 3 + 1) = true
#as the above condition is true, therefore increment countConsecutive by 1
#countConsecutive = countConsecutive + 1 = 3 + 1 = 4
#ans = max(ans, countConsecutive) = max(3, 4) = 4
#At i = 4:

#check if (dist[4] == dist[3] + 1) = (9 != 4 + 1) = false
#as the above condition is false, therefore re-initialize countConsecutive by 1
#countConsecutive = 1
#ans = max(ans, countConsecutive) = max(4, 1) = 4
#At i = 5:

#check if (dist[5] == dist[4] + 1) = (10 == 9 + 1) = true
#as the above condition is true, therefore increment countConsecutive by 1
##countConsecutive = countConsecutive + 1 = 1 + 1 = 2
#ans = max(ans, countConsecutive) = max(4, 2) = 4
#At i = 6:

#check if (dist[6] == dist[5] + 1) = (20 != 10 + 1) = false
#as the above condition is false, therefore re-initialize countConsecutive by 1
#countConsecutive = 1
#ans = max(ans, countConsecutive) = max(4, 1) = 4
#Therefore the longest consecutive subsequence is {1, 2, 3, 4}
#Hence, ans is 4.

#Follow the steps below to solve the problem:

#Initialize ans and countConsecutive with 0.
#Sort the arr[].
#Store the distinct elements in dist[] array by traversing over the arr[].
#Now, traverse on the dist[] array to find the count of consecutive elements.
#Simultaneously maintain the answer variable.
#Below is the implementation of the above approach:

# Python3 program to find longest
# contiguous subsequence
  
# Returns length of the longest
# contiguous subsequence
  
  
def findLongestConseqSubseq(arr, n):
  
    ans = 0
    count = 0
  
    # Sort the array
    arr.sort()
  
    v = []
  
    v.append(arr[0])
  
    # Insert repeated elements only
    # once in the vector
    for i in range(1, n):
        if (arr[i] != arr[i - 1]):
            v.append(arr[i])
  
    # Find the maximum length
    # by traversing the array
    for i in range(len(v)):
  
        # Check if the current element is
        # equal to previous element +1
        if (i > 0 and v[i] == v[i - 1] + 1):
            count += 1
  
        # Reset the count
        else:
            count = 1
  
        # Update the maximum
        ans = max(ans, count)
  
    return ans
  
  
# Driver code
arr = [1, 2, 2, 3]
n = len(arr)
  
print("Length of the Longest contiguous subsequence is",
      findLongestConseqSubseq(arr, n))
  
# This code is contributed by avanitrachhadiya2155
#Output
#Length of the Longest contiguous subsequence is 3
#Time complexity: O(Nlog(N)), Time to sort the array is O(Nlog(N)).
#Auxiliary space: O(N). Extra space is needed for storing distinct elements.
#--------------------------------------------------------------------------------

#Longest Consecutive Subsequence using Hashing:
#The idea is to use Hashing. We first insert all elements in a Set. Then check all the possible starts of consecutive subsequences.

#Illustration:

#Below image is the dry run, for example, arr[] = {1, 9, 3, 10, 4, 20, 2}:



#Follow the steps below to solve the problem:

#Create an empty hash.
#Insert all array elements to hash.
#Do the following for every element arr[i]
#Check if this element is the starting point of a subsequence. To check this, simply look for arr[i] – 1 in the hash, if not found, then this is the first element of a subsequence.
#If this element is the first element, then count the number of elements in the consecutive starting with this element. Iterate from arr[i] + 1 till the last element that can be found.
#If the count is more than the previous longest subsequence found, then update this.
#Below is the implementation of the above approach: 

# Python program to find longest contiguous subsequence
  
  
def findLongestConseqSubseq(arr, n):
  
    s = set()
    ans = 0
  
    # Hash all the array elements
    for ele in arr:
        s.add(ele)
  
    # check each possible sequence from the start
    # then update optimal length
    for i in range(n):
  
         # if current element is the starting
        # element of a sequence
        if (arr[i]-1) not in s:
  
            # Then check for next elements in the
            # sequence
            j = arr[i]
            while(j in s):
                j += 1
  
            # update  optimal length if this length
            # is more
            ans = max(ans, j-arr[i])
    return ans
  
  
# Driver code
if __name__ == '__main__':
    n = 7
    arr = [1, 9, 3, 10, 4, 20, 2]
    print("Length of the Longest contiguous subsequence is ",
          findLongestConseqSubseq(arr, n))
  
# Contributed by: Harshit Sidhwa
#Output
#Length of the Longest contiguous subsequence is 4
#Time complexity: O(N), Only one traversal is needed and the time complexity is O(n) under the assumption that hash insert and search takes O(1) time.
#Auxiliary space: O(N), To store every element in the hashmap O(n) space is needed
#----------------------------------------------------------------

#Longest Consecutive Subsequence using Priority Queue:
#The Idea is to use Priority Queue. Using priority queue it will sort the elements and eventually it will help to find consecutive elements.

#Illustration:

#Input: arr[] = {1, 9, 3, 10, 4, 20, 2}

#Insert all the elements in the Priority Queue:

#1	2	3	4	9	10	20
#Initialise variable prev with first element of priority queue, prev will contain last element has been picked and it will help to check whether the current element is contributing for consecutive sequence or not.

#prev = 1, countConsecutive = 1, ans = 1

#Run the algorithm till the priority queue becomes empty.

#2	3	4	9	10	20
#current element is 2
#prev + 1 == 2, therefore increment countConsecutive by 1
#countConsecutive = countConsecutive + 1 = 1 + 1 = 2
#update prev with current element, prev = 2
#pop the current element
#ans = max(ans, countConsecutive) = (1, 2) = 2
#3	4	9	10	20
#current element is 3
#prev + 1 == 3, therefore increment countConsecutive by 1
#countConsecutive = countConsecutive + 1 = 2 + 1 = 3
#update prev with current element, prev = 3
#pop the current element
#ans = max(ans, countConsecutive) = (2, 3) = 3
#4	9	10	20
#current element is 4
#prev + 1 == 4, therefore increment countConsecutive by 1
#countConsecutive = countConsecutive + 1 = 3 + 1 = 4
#update prev with current element, prev = 4
#pop the current element
#ans = max(ans, countConsecutive) = (3, 4) = 4
#9	10	20
#current element is 9
#prev + 1 != 9, therefore re-initialise countConsecutive by 1
#countConsecutive = 1
#update prev with current element, prev = 9
#pop the current element
#ans = max(ans, countConsecutive) = (4, 1) = 4
##10	20
#current element is 10
#prev + 1 == 10, therefore increment countConsecutive by 1
#countConsecutive = countConsecutive + 1 = 1 + 1 = 2
#update prev with current element, prev = 10
#pop the current element
#ans = max(ans, countConsecutive) = (4, 2) =4
#20
#current element is 20
#prev + 1 != 20, therefore re-initialise countConsecutive by 1
#countConsecutive = 1
#update prev with current element, prev = 20
#pop the current element
#ans = max(ans, countConsecutive) = (4, 1) = 4
#Hence, the longest consecutive subsequence is 4.

#Follow the steps below to solve the problem:

#Create a Priority Queue to store the element
#Store the first element in a variable
#Remove it from the Priority Queue
#Check the difference between this removed first element and the new peek element
#If the difference is equal to 1 increase the count by 1 and repeats step 2 and step 3
#If the difference is greater than 1 set counter to 1 and repeat step 2 and step 3
#if the difference is equal to 0 repeat step 2 and 3
#if counter greater than the previous maximum then store counter to maximum
#Continue step 4 to 7 until we reach the end of the Priority Queue
#Return the maximum value
#Below is the implementation of the above approach: 

# Python program for the above approach
import bisect
  
  
def findLongestConseqSubseq(arr, N):
    pq = []
    for i in range(N):
  
        # adding element from
        # array to PriorityQueue
        bisect.insort(pq, arr[i])
  
    # Storing the first element
    # of the Priority Queue
    # This first element is also
    # the smallest element
    prev = pq[0]
    pq.pop(0)
  
    # Taking a counter variable with value 1
    c = 1
  
    # Storing value of max as 1
    # as there will always be
    # one element
    max = 1
    while(len(pq)):
        # check if current peek
        # element minus previous
        # element is greater than
        # 1 This is done because
        # if it's greater than 1
        # then the sequence
        # doesn't start or is broken here
        if(pq[0] - prev > 1):
            # Store the value of counter to 1
            # As new sequence may begin
            c = 1
  
            # Update the previous position with the
            # current peek And remove it
            prev = pq[0]
            pq.pop(0)
  
        # Check if the previous
        # element and peek are same
        elif(pq[0] - prev == 0):
            # Update the previous position with the
            # current peek And remove it
            prev = pq[0]
            pq.pop(0)
  
        # If the difference
        # between previous element and peek is 1
        else:
            # Update the counter
            # These are consecutive elements
            c = c + 1
            # Update the previous position
            # with the current peek And remove it
            prev = pq[0]
            pq.pop(0)
  
        # Check if current longest
        # subsequence is the greatest
        if(max < c):
            # Store the current subsequence count as
            # max
            max = c
    return max
  
  
# Driver Code
arr = [1, 9, 3, 10, 4, 20, 2]
n = 7
print("Length of the Longest consecutive subsequence is {}".format(
    findLongestConseqSubseq(arr, n)))
  
  
# This code is contributed by Pushpesh Raj
#Output
#Length of the Longest consecutive subsequence is 4
#Time Complexity: O(N*log(N)), Time required to push and pop N elements is logN for each element.
#Auxiliary Space: O(N), Space required by priority queue to store N elements.
