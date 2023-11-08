#Find all distinct palindromic sub-strings of a given string
#Difficulty Level : Hard
#Given a string of lowercase ASCII characters, find all distinct continuous palindromic sub-strings of it. 

#Examples: 

#Input: str = "abaaa"
#Output:  Below are 5 palindrome sub-strings
#a
#aa
#aaa
#aba
#b


#Input: str = "geek"
##Output:  Below are 4 palindrome sub-strings
#e
#ee
#g
#k
#-------------------------------------------------------------------------

#Method 1:

#Step 1: Finding all palindromes using modified Manacher’s algorithm: 
#Considering each character as a pivot, expand on both sides to find the length of both even and odd length palindromes centered at the pivot character under consideration and store the length in the 2 arrays (odd & even). 
#Time complexity for this step is O(n^2)

#Step 2: Inserting all the found palindromes in a HashMap: 
#Insert all the palindromes found from the previous step into a HashMap. Also insert all the individual characters from the string into the HashMap (to generate distinct single letter palindromic sub-strings). 
#Time complexity of this step is O(n^3) assuming that the hash insert search takes O(1) time. Note that there can be at most O(n^2) palindrome sub-strings of a string. In below C++ code ordered hashmap is used where the time complexity of insert and search is O(Logn). In C++, ordered hashmap is implemented using Red Black Tree.

#Step 3: Printing the distinct palindromes and number of such distinct palindromes: 
#The last step is to print all values stored in the HashMap (only distinct elements will be hashed due to the property of HashMap). The size of the map gives the number of distinct palindromic continuous sub-strings.

#Below is the implementation of the above idea.




# Python program Find all distinct palindromic sub-strings
# of a given string
 
# Function to print all distinct palindrome sub-strings of s
def palindromeSubStrs(s):
    m = dict()
    n = len(s)
 
    # table for storing results (2 rows for odd-
    # and even-length palindromes
    R = [[0 for x in range(n+1)] for x in range(2)]
 
    # Find all sub-string palindromes from the given input
    # string insert 'guards' to iterate easily over s
    s = "@" + s + "#"
 
    for j in range(2):
        rp = 0    # length of 'palindrome radius'
        R[j][0] = 0
 
        i = 1
        while i <= n:
 
            # Attempt to expand palindrome centered at i
            while s[i - rp - 1] == s[i + j + rp]:
                rp += 1 # Incrementing the length of palindromic
                        # radius as and when we find valid palindrome
 
            # Assigning the found palindromic length to odd/even
            # length array
            R[j][i] = rp
            k = 1
            while (R[j][i - k] != rp - k) and (k < rp):
                R[j][i+k] = min(R[j][i-k], rp - k)
                k += 1
            rp = max(rp - k, 0)
            i += k
 
    # remove guards
    s = s[1:len(s)-1]
 
    # Put all obtained palindromes in a hash map to
    # find only distinct palindrome
    m[s[0]] = 1
    for i in range(1,n):
        for j in range(2):
            for rp in range(R[j][i],0,-1):
                m[s[i - rp - 1 : i - rp - 1 + 2 * rp + j]] = 1
        m[s[i]] = 1
 
    # printing all distinct palindromes from hash map
    print ("Below are " + str(len(m)) + " pali sub-strings")
    for i in m:
        print (i)
 
# Driver program
palindromeSubStrs("abaaa")
# This code is contributed by BHAVYA JAIN and ROHIT SIKKA
Output: 

#Below are 5 palindrome sub-strings
#a
#aa
#aaa
#aba
#b 



#-------------------------------------------------------------------
Method 2 :

String length – N

Step 1 : Find all the palindromic sub-strings

        First for every sub-string check if it is palindrome or not using dynamic programming like this – https://www.geeksforgeeks.org/count-palindrome-sub-strings-string/

        Time complexity – O(N2)   and   Space complexity – O(N2)

Step 2 : Remove duplicate palindromes

        For every index starting from index 0 we will use KMP algorithm and check if prefix and suffix is same and is palindrome then we will put 0 the dp array for that suffix sub-string

        Time complexity O(N2)    and   Space complexity O(N) for KMP array

Step 3 : Print the distinct palindromes and number of such palindromes

        For every sub-string check if it is present in dp array (i.e dp[i][j] == true) and print it.

        Time complexity O(N2)   and    Space complexity O(N)

Overall Time complexity – O(N2)

Overall Space complexity – O(N2)

Below is the implementation of the above idea.


# Python3 program to find all distinct palindrome sub-strings
# of a given string
def solve(s):
    n = len(s)
     
    # dp array to store whether a substring is palindrome
    # or not using dynamic programming we can solve this
    # in O(N^2)
    # dp[i][j] will be true (1) if substring (i, j) is
    # palindrome else false (0)
    dp = [[False for j in range(n)] for i in range(n)]
    for i in range(n):
       
        # base case every char is palindrome
        dp[i][i] = True
         
        # check for every substring of length 2
        if i < n-1 and s[i] == s[i+1]:
            dp[i][i+1] = True
             
    # check every substring of length greater than 2 for
    # palindrome
    for lenk in range(3, n+1):
        for i in range(n-lenk+1):
            if s[i] == s[i+lenk-1] and dp[i+1][i+lenk-2]:
                dp[i][i+lenk-1] = True
                 
    # here we will apply kmp algorithm for substrings
    # starting from i = 0 to n-1 when we will find prefix
    # and suffix of a substring to be equal and it is
    # palindrome we will make dp[i][j] for that suffix to be
    # false which means it is already added in the prefix
    # and we should not count it anymore.
    kmp = [0]*n
    for i in range(n):
       
        # starting kmp for every i from 0 to n-1
        j, k = 0, 1
        while k+i < n:
            if s[j+i] == s[k+i]:
               
                # make suffix to be false
                # if this suffix is palindrome then it is
                # already included in prefix
                dp[k+i-j][k+i] = False
                kmp[k] = j+1
                k += 1
                j += 1
            elif j > 0:
                j = kmp[j-1]
            else:
                kmp[k] = 0
                k += 1
    count = 0
    for i in range(n):
        str = ""
        for j in range(i, n):
            str += s[j]
            if dp[i][j]:
                # count number of resultant distinct
                # substrings and print  that substring
                count += 1
                print(str)
    print("Total number of distinct palindromes is", count)
    return 0
 
# Driver code starts
 
if __name__ == "__main__":
    s1 = "abaaa"
    s2 = "aaaaaaaaaa"
    solve(s1)
    solve(s2)
 
    # This code is contributed by lokeshpotta20.
Output
a
aba
b
aa
aaa
Total number of distinct palindromes is 5
a
aa
aaa
aaaa
aaaaa
aaaaaa
aaaaaaa
aaaaaaaa
aaaaaaaaa
aaaaaaaaaa
Total number of distinct palindromes is 10
Similar Problem: 
Count All Palindrome Sub-Strings in a String
This article is contributed by Vignesh Narayanan and Sowmya Sampath