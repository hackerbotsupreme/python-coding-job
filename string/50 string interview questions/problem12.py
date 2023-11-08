#Minimum number of deletions to make a string palindrome


#Given a string of size ‘n’. The task is to remove or delete the minimum number of characters from the string so that the resultant string is a palindrome. 

#Note: The order of characters should be maintained. 

#Examples : 

#Input : aebcbda
#Output : 2
#Remove characters 'e' and 'd'
#Resultant string will be 'abcba'
#which is a palindromic string

#Input : geeksforgeeks
Output : 8

#A simple solution is to remove all subsequences one by one and check if the remaining string is palindrome or not. The time complexity of this solution is exponential.
An efficient approach uses the concept of finding the length of the longest palindromic subsequence of a given sequence. 

Algorithm: 

1. str is the given string.



2. n length of str

3. len be the length of the longest 
  palindromic subsequence of str

4. minimum number of deletions 
  min = n – len

Below is the implementation of the above approach:


# Python3 implementation to find
# minimum number of deletions
# to make a string palindromic
  
# Returns the length of
# the longest palindromic
# subsequence in 'str'
def lps(str):
    n = len(str)
  
    # Create a table to store
    # results of subproblems
    L = [[0 for x in range(n)]for y in range(n)]
  
    # Strings of length 1
    # are palindrome of length 1
    for i in range(n):
        L[i][i] = 1
  
    # Build the table. Note that
    # the lower diagonal values
    # of table are useless and
    # not filled in the process.
    # c1 is length of substring
    for cl in range( 2, n+1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if (str[i] == str[j] and cl == 2):
                L[i][j] = 2
            elif (str[i] == str[j]):
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i][j - 1],L[i + 1][j])
  
    # length of longest
    # palindromic subseq
    return L[0][n - 1]
  
# function to calculate
# minimum number of deletions
def minimumNumberOfDeletions( str):
 
    n = len(str)
  
    # Find longest palindromic
    # subsequence
    l = lps(str)
  
    # After removing characters
    # other than the lps, we
    # get palindrome.
    return (n - l)
  
# Driver Code
if __name__ == "__main__":
     
    str = "geeksforgeeks"
    print( "Minimum number of deletions = "
         , minimumNumberOfDeletions(str))
Output
Minimum number of deletions = 8
Time Complexity: O(n^2),as the LPS subproblem is solved using dynamic programming.


Space complexity: O(n^2) as a 2D array of size nxn is used to store the subproblems.

Another Approach:

Take two indexes first as ‘i’ and last as a ‘j’
now compare the character at the index ‘i’ and ‘j’
if characters are equal, then 
recursively call the function by incrementing ‘i’ by ‘1’ and decrementing ‘j’ by ‘1’
else 
recursively call the two functions, the first increment ‘i’ by ‘1’ keeping ‘j’ constant, second decrement ‘j’ by ‘1’ keeping ‘i’ constant.
take a minimum of both and return by adding ‘1’
Below is the implementation of the above approach:


# Python3 program for above approach
 
# Utility function for calculating
# Minimum element to delete
def utility_fun_for_del(Str, i, j):
     
    if (i >= j):
        return 0
 
    # Condition to compare characters
    if (Str[i] == Str[j]):
         
        # Recursive function call
        return utility_fun_for_del(Str, i + 1,
                                        j - 1)
 
    # Return value, incrementing by 1
    # return minimum Element between two values   
    return (1 + min(utility_fun_for_del(Str, i + 1, j),
                    utility_fun_for_del(Str, i, j - 1)))
 
# Function to calculate the minimum
# Element required to delete for
# Making string palindrome
def min_ele_del(Str):
 
    # Utility function call
    return utility_fun_for_del(Str, 0,
                           len(Str) - 1)
 
# Driver code
Str = "abefbac"
 
print("Minimum element of deletions =",
       min_ele_del(Str))
 
# This code is contributed by avanitrachhadiya2155
Output
#Minimum element of deletions = 2
#Time complexity: O(2^n), the time complexity of this solution is exponential as it requires a recursive approach to solve the problem. There are two recursive calls in each step and hence the time complexity is O(2^n).
#Auxiliary Space: O(n), the space complexity of this solution is linear as the recursive calls are stored in the stack frames and the maximum depth of the recursion tree can be n.

#Approach: Top-down dynamic programming

#We will first define the DP table and initialize it with -1 throughout the table. Follow the below approach now,

#Define the function transformation to calculate the Minimum number of deletions and insertions to transform one string into another
#We write the condition for  base cases
#Checking the wanted condition
#If the condition is satisfied we increment the value and store the value in the table
#If the recursive call is being solved earlier than we directly utilize the value from the table
#Else store the max transformation from the subsequence
#We will continue the process till we reach the base condition
#Return the DP [-1][-1]
#Below is the implementation:


# function definition
def transformation(s1,s2,i,j,dp):
     
     # base cases
    if i>=len(s1) or j>=len(s2):
        return 0
     
    # checking the desired condition
    if s1[i]==s2[j]:
         
        # if yes increment the count
        dp[i][j]=1+transformation(s1,s2,i+1,j+1,dp)
         
    # if no   
    if dp[i][j]!=-1:
         
        #return the value form the table
        return dp[i][j]
     
    # else store the max transformation
    # from the subsequence
    else:
        dp[i][j]=max(transformation(s1,s2,i,j+i,dp),
                     transformation(s1,s2,i+1,j,dp))
         
    # return the dp [-1][-1]   
    return dp[-1][-1]
 
                      
 
s1 = "geeksforgeeks"
s2 = "geeks"
i=0
j=0
 
#initialize the array with -1
dp=[[-1 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
print("MINIMUM NUMBER OF DELETIONS: ",
      len(s1)-transformation(s1,s2,0,0,dp),
      end=" ")
print("MINIMUM NUMBER OF INSERTIONS: ",
      len(s2)-transformation(s1,s2,0,0,dp),
      end=" " )
print("LCS LENGTH: ",transformation(s1,s2,0,0,dp))
 
#code contributed by saikumar kudikala
#Output:

#MINIMUM NUMBER OF DELETIONS:  8 MINIMUM NUMBER OF INSERTIONS:  0 LCS LENGTH:  5


