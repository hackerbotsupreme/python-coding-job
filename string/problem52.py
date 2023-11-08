#Length of the longest valid substring
#Difficulty Level : Medium
#Given a string consisting of opening and closing parenthesis, find the length of the longest valid parenthesis substring.

#Examples: 

#Input : ((()
#Output : 2
#Explanation : ()

#Input: )()())
#Output : 4
#Explanation: ()() 

#Input:  ()(()))))
#Output: 6


#A Simple Approach is to find all the substrings of given string. For every string, check if it is a valid string or not. If valid and length is more than maximum length so far, then update maximum length. We can check whether a substring is valid or not in linear time using a stack (See this for details). Time complexity of this solution is O(n2.

#An Efficient Solution can solve this problem in O(n) time. The idea is to store indexes of previous starting brackets in a stack. The first element of the stack is a special element that provides index before the beginning of valid substring (base for next valid string). 
#------------------------------------------------------------------------
#1) Create an empty stack and push -1 to it. 
#   The first element of the stack is used 
#   to provide a base for the next valid string. 

#2) Initialize result as 0.

#3) If the character is '(' i.e. str[i] == '('), 
#   push index'i' to the stack. 
   
#2) Else (if the character is ')')
#   a) Pop an item from the stack (Most of the 
#      time an opening bracket)
#   b) If the stack is not empty, then find the
#      length of current valid substring by taking 
#      the difference between the current index and
#      top of the stack. If current length is more 
#      than the result, then update the result.
#   c) If the stack is empty, push the current index
#      as a base for the next valid substring.

#3) Return result.
#Below is the implementation of the above algorithm. 


# Python program to find length of the longest valid
# substring
 
 
def findMaxLen(string):
    n = len(string)
 
    # Create a stack and push -1
    # as initial index to it.
    stk = []
    stk.append(-1)
 
    # Initialize result
    result = 0
 
    # Traverse all characters of given string
    for i in range(n):
 
        # If opening bracket, push index of it
        if string[i] == '(':
            stk.append(i)
         
        # If closing bracket, i.e., str[i] = ')'
        else:
 
            # Pop the previous opening bracket's index
            if len(stk) != 0:
                stk.pop()
 
            # Check if this length formed with base of
            # current valid substring is more than max
            # so far
            if len(stk) != 0:
                result = max(result,
                            i - stk[len(stk)-1])
 
            # If stack is empty. push current index as
            # base for next valid substring (if any)
            else:
                stk.append(i)
 
    return result
 
 
# Driver code
string = "((()()"
 
# Function call
print (findMaxLen(string))
 
string = "()(()))))"
 
# Function call
print (findMaxLen(string))
 
# This code is contributed by Bhavya Jain
 
# This code is modified by Susobhan Akhuli
#Output
#4
#6
#Time Complexity: O(N), here N is the length of string.
#Auxiliary Space: O(N)





#Explanation with example: 

#Input: str = "(()()"

#Initialize result as 0 and stack with one item -1.

#For i = 0, str[0] = '(', we push 0 in stack

#For i = 1, str[1] = '(', we push 1 in stack

#For i = 2, str[2] = ')', currently stack has 
#[-1, 0, 1], we pop from the stack and the stack
#now is [-1, 0] and length of current valid substring 
#becomes 2 (we get this 2 by subtracting stack top from 
#current index).

#Since the current length is more than the current result, 
#we update the result.

#For i = 3, str[3] = '(', we push again, stack is [-1, 0, 3].
#For i = 4, str[4] = ')', we pop from the stack, stack 
#becomes [-1, 0] and length of current valid substring 
##becomes 4 (we get this 4 by subtracting stack top from 
#current index). 
#Since current length is more than current result,
#we update result. 
#Another Efficient Approach can solve the problem in O(n) time. The idea is to maintain an array that stores the length of the longest valid substring ending at that index. We iterate through the array and return the maximum value.

#1) Create an array longest of length n (size of the input
#   string) initialized to zero.
#   The array will store the length of the longest valid 
#   substring ending at that index.

#2) Initialize result as 0.

#3) Iterate through the string from second character
#   a) If the character is '(' set longest[i]=0 as no 
#      valid sub-string will end with '('.
#   b) Else
#      i) if s[i-1] = '('
#            set longest[i] = longest[i-2] + 2
#      ii) else
#            set longest[i] = longest[i-1] + 2 + 
#            longest[i-longest[i-1]-2]

#4) In each iteration update result as the maximum of 
#   result and longest[i]

#5) Return result.
#Below is the implementations of the above algorithm.


# Python3 program to find length of
# the longest valid substring
 
 
def findMaxLen(s):
    if (len(s) <= 1):
        return 0
 
    # Initialize curMax to zero
    curMax = 0
 
    longest = [0] * (len(s))
 
    # Iterate over the string starting
    # from second index
    for i in range(1, len(s)):
        if ((s[i] == ')'
             and i - longest[i - 1] - 1 >= 0
             and s[i - longest[i - 1] - 1] == '(')):
             
            longest[i] = longest[i - 1] + 2
            if (i - longest[i - 1] - 2 >= 0):
                longest[i] += (longest[i -
                                       longest[i - 1] - 2])
            else:
                longest[i] += 0
            curMax = max(longest[i], curMax)
    return curMax
 
 
# Driver Code
if __name__ == '__main__':
    Str = "((()()"
     
    # Function call
    print(findMaxLen(Str))
 
    Str = "()(()))))"
     
    # Function call
    print(findMaxLen(Str))
 
# This code is contributed by PranchalK
#Output
#4
#6
#Time Complexity: O(N), here N is the length of string.
##Auxiliary Space: O(N)
#Thanks to Gaurav Ahirwar and Ekta Goel for suggesting above approach.

#Another approach in O(1) auxiliary space and O(N) Time complexity: 

#The idea to solve this problem is to traverse the string on and keep track of the count of open parentheses and close parentheses with the help of two counters left and right respectively.
#First, the string is traversed from the left towards the right and for every “(” encountered, the left counter is incremented by 1 and for every “)” the right counter is incremented by 1.
#Whenever the left becomes equal to right, the length of the current valid string is calculated and if it greater than the current longest substring, then value of required longest substring is updated with current string length.
#If the right counter becomes greater than the left counter, then the set of parentheses has become invalid and hence the left and right counters are set to 0.
#After the above process, the string is similarly traversed from right to left and similar procedure is applied.
#Below is the implementation of the above approach: 


# Python3 program to implement the above approach
 
# Function to return the length of
# the longest valid substring
 
 
def solve(s, n):
 
    # Variables for left and right counter.
    # maxlength to store the maximum length found so far
    left = 0
    right = 0
    maxlength = 0
 
    # Iterating the string from left to right
    for i in range(n):
 
        # If "(" is encountered,
        # then left counter is incremented
        # else right counter is incremented
        if (s[i] == '('):
            left += 1
        else:
            right += 1
 
        # Whenever left is equal to right, it signifies
        # that the subsequence is valid and
        if (left == right):
            maxlength = max(maxlength, 2 * right)
 
        # Resetting the counters when the subsequence
        # becomes invalid
        elif (right > left):
            left = right = 0
 
    left = right = 0
 
    # Iterating the string from right to left
    for i in range(n - 1, -1, -1):
 
        # If "(" is encountered,
        # then left counter is incremented
        # else right counter is incremented
        if (s[i] == '('):
            left += 1
        else:
            right += 1
 
        # Whenever left is equal to right, it signifies
        # that the subsequence is valid and
        if (left == right):
            maxlength = max(maxlength, 2 * left)
 
        # Resetting the counters when the subsequence
        # becomes invalid
        elif (left > right):
            left = right = 0
    return maxlength
 
 
# Driver code
# Function call
print(solve("((()()()()(((())", 16))
 
# This code is contributed by shubhamsingh10
#Output
#8
#Time Complexity: O(N), here N is the length of string.
#Auxiliary Space: O(1)

