#Manacher’s Algorithm – Linear Time Longest Palindromic Substring – Part 4

#Difficulty Level : Expert
#Last Updated : 25 Jan, 2023
#Read
#Discuss
#Courses
#Practice
#Video
#In Manacher’s Algorithm Part 1 and Part 2, we gone through some of the basics, understood LPS length array and how to calculate it efficiently based on four cases. In Part 3, we implemented the same. 
#Here we will review the four cases again and try to see it differently and implement the same. 
#All four cases depends on LPS length value at currentLeftPosition (L[iMirror]) and value of (centerRightPosition – currentRightPosition), i.e. (R – i). These two information are known before which helps us to reuse previous available information and avoid unnecessary character comparison. 

#Manacher's Algorithm – Linear Time Longest Palindromic Substring

#If we look at all four cases, we will see that we 1st set minimum of L[iMirror] and R-i to L[i] and then we try to expand the palindrome in whichever case it can expand.
#Above observation may look more intuitive, easier to understand and implement, given that one understands LPS length array, position, index, symmetry property etc. 

#Implementation:

#C++
#Java
#Python3
# Python program to implement Manacher's Algorithm
  
def findLongestPalindromicString(text):
    N = len(text)
    if N == 0:
        return
    N = 2*N+1    # Position count
    L = [0] * N
    L[0] = 0
    L[1] = 1
    C = 1     # centerPosition
    R = 2     # centerRightPosition
    i = 0    # currentRightPosition
    iMirror = 0     # currentLeftPosition
    maxLPSLength = 0
    maxLPSCenterPosition = 0
    start = -1
    end = -1
    diff = -1
  
    # Uncomment it to print LPS Length array
    # printf("%d %d ", L[0], L[1]);
    for i in range(2,N):
      
        # get currentLeftPosition iMirror for currentRightPosition i
        iMirror = 2*C-i
        L[i] = 0
        diff = R - i
        # If currentRightPosition i is within centerRightPosition R
        if diff > 0:
            L[i] = min(L[iMirror], diff)
  
        # Attempt to expand palindrome centered at currentRightPosition i
        # Here for odd positions, we compare characters and
        # if match then increment LPS Length by ONE
        # If even position, we just increment LPS by ONE without
        # any character comparison
        try:
            while ((i + L[i]) < N and (i - L[i]) > 0) and \
                    (((i + L[i] + 1) % 2 == 0) or \
                    (text[(i + L[i] + 1) // 2] == text[(i - L[i] - 1) // 2])):
                L[i]+=1
        except Exception as e:
            pass
  
        if L[i] > maxLPSLength:        # Track maxLPSLength
            maxLPSLength = L[i]
            maxLPSCenterPosition = i
  
        # If palindrome centered at currentRightPosition i
        # expand beyond centerRightPosition R,
        # adjust centerPosition C based on expanded palindrome.
        if i + L[i] > R:
            C = i
            R = i + L[i]
  
    # Uncomment it to print LPS Length array
    # printf("%d ", L[i]);
    start = (maxLPSCenterPosition - maxLPSLength) // 2
    end = start + maxLPSLength - 1
    print ("LPS of string is " + text + " : ",text[start:end+1])
  
# Driver program
text1 = "babcbabcbaccba"
findLongestPalindromicString(text1)
  
text2 = "abaaba"
findLongestPalindromicString(text2)
  
text3 = "abababa"
findLongestPalindromicString(text3)
  
text4 = "abcbabcbabcba"
findLongestPalindromicString(text4)
  
text5 = "forgeeksskeegfor"
findLongestPalindromicString(text5)
  
text6 = "caba"
findLongestPalindromicString(text6)
  
text7 = "abacdfgdcaba"
findLongestPalindromicString(text7)
  
text8 = "abacdfgdcabba"
findLongestPalindromicString(text8)
  
text9 = "abacdedcaba"
findLongestPalindromicString(text9)
  
# This code is contributed by BHAVYA JAIN

#Output
#LPS of string is babcbabcbaccba : abcbabcba
#LPS of string is abaaba : abaaba
#LPS of string is abababa : abababa
#LPS of string is abcbabcbabcba : abcbabcbabcba
#LPS of string is forgeeksskeegfor : geeksskeeg
#LPS of string is caba : aba
#LPS of string is abacdfgdcaba : aba
#LPS of string is abacdfgdcabba : abba
#LPS of string is abacdedcaba : abacdedcaba
#Time Complexity: O(n)
#Auxiliary Space: O(n)

#Other Approaches:
#We have discussed two approaches here. One in Part 3 and other in current article. In both approaches, we worked on given string. Here we had to handle even and odd positions differently while comparing characters for expansion (because even positions do not represent any character in string).
#To avoid this different handling of even and odd positions, we need to make even positions also to represent some character (actually all even positions should represent SAME character because they MUST match while character comparison). One way to do this is to set some character at all even positions by modifying given string or create a new copy of given string. For example, if input string is “abcb”, new string should be “#a#b#c#b#” if we add # as unique character at even positions.
#The two approaches discussed already can be modified a bit to work on modified string where different handling of even and odd positions will not be needed. 
#We may also add two DIFFERENT characters (not yet used anywhere in string at even and odd positions) at start and end of string as sentinels to avoid bound check. With these changes string “abcb” will look like “^#a#b#c#b#$” where ^ and $ are sentinels. 
#This implementation may look cleaner with the cost of more memory.
#We are not implementing these here as it’s a simple change in given implementations.



#Implementation of approach discussed in current article on a modified string can be found at Longest Palindromic Substring Part II and a Java Translation of the same by Princeton. 

#Recommended
#Solve DSA problems on GfG Practice.

#Solve Problems




#Like
#29
#Previous
#Boyer Moore Algorithm for Pattern Searching
#Next
#Z algorithm (Linear time pattern searching Algorithm)
#Related Articles
#1.
#Manacher's Algorithm - Linear Time Longest Palindromic Substring - Part 1
#2.
#Manacher's Algorithm - Linear Time Longest Palindromic Substring - Part 2
#3.
#Manacher's Algorithm - Linear Time Longest Palindromic Substring - Part 3
#4.
#Longest Palindromic Substring using Palindromic Tree | Set 3
#5.
#Z algorithm (Linear time pattern searching Algorithm)
#6.
#Minimum length of substring whose rotation generates a palindromic substring
#7.
#Longest Non-palindromic substring
#8.
#Suffix Tree Application 6 - Longest Palindromic Substring
#9.
#Longest palindromic string possible after removal of a substring
#10.
#Rearrange string to obtain Longest Palindromic Substring
#Article Contributed By :
#https://media.geeksforgeeks.org/auth/avatar.png
#GeeksforGeeks
#Vote for difficulty
#Current difficulty : Expert
#Easy
#Normal
#Medium
#Hard
#Expert
#Improved By :
#sanjeev2552
#princiraj1992
#unknown2108
#amartyaghoshgfg
#geekygirl2001
#hardikkoriintern
#Article Tags :
#palindrome
#Pattern Searching
#Strings
#Practice Tags :
#palindrome
#Palindrome
#Pattern Searching
#Strings
#Improve Article
#Report Issue