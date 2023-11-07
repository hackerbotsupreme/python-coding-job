#Online algorithm for checking palindrome in a stream

#Difficulty Level : Expert
#Last Updated : 10 Jan, 2023
#Read
#Discuss(80)
#Courses
#Practice
#Video
#Given a stream of characters (characters are received one by one), write a function that prints ‘Yes’ if a character makes the complete string palindrome, else prints ‘No’. 

#Examples:

#Input: str[] = "abcba"
#Output: a Yes   // "a" is palindrome
#        b No    // "ab" is not palindrome
#        c No    // "abc" is not palindrome
##        b No    // "abcb" is not palindrome
#        a Yes   // "abcba" is palindrome

#Input: str[] = "aabaacaabaa"
#Output:  a Yes   // "a" is palindrome
#         a Yes   // "aa" is palindrome
#         b No    // "aab" is not palindrome 
#        a No    // "aaba" is not palindrome  
#         a Yes   // "aabaa" is palindrome  
#         c No    // "aabaac" is not palindrome  
#         a No    // "aabaaca" is not palindrome  
#         a No    // "aabaacaa" is not palindrome  
#         b No    // "aabaacaab" is not palindrome  
#         a No    // "aabaacaaba" is not palindrome  
#         a Yes   // "aabaacaabaa" is palindrome  
#Let input string be str[0..n-1]. 

#A Simple Solution is to do following for every character str[i] in input string. Check if substring str[0…i] is palindrome, then print yes, else print no. 

#A Better Solution is to use the idea of Rolling Hash used in Rabin Karp algorithm. The idea is to keep track of reverse of first half and second half (we also use first half and reverse of second half) for every index. Below is complete algorithm.

#  1) The first character is always a palindrome, so print yes for 
#     first character.

#  2) Initialize reverse of first half as "a" and second half as "b".  
#     Let the hash value of first half reverse be 'firstr' and that of 
#     second half be 'second'.

#  3) Iterate through string starting from second character, do following
#      for every character str[i], i.e., i varies from 1 to n-1.
#     a) If 'firstr' and 'second' are same, then character by character 
#        check the substring ending with current character and print 
#        "Yes" if palindrome.
#        Note that if hash values match, then strings need not be same.
#        For example, hash values of "ab" and "ba" are same, but strings
#        are different. That is why we check complete string after hash.
#
#     b) Update 'firstr' and 'second' for next iteration.  
#           If 'i' is even, then add next character to the beginning of 
#                           'firstr' and end of second half and update 
#                            hash values.
#           If 'i' is odd,  then keep 'firstr' as it is, remove leading 
#                           character from second and append a next 
#                           character at end.
#Let us see all steps for example 

#string “abcba” Initial values of ‘firstr’ and ‘second’      



#firstr’ = hash(“a”), ‘second’ = hash(“b”) Start from second character, i.e., i = 1      

#Compare ‘firstr’ and ‘second’, they don’t match, so print no.     
#Calculate hash values for next iteration, i.e., i = 2      
#Since i is odd, ‘firstr’ is not changed and ‘second’ becomes hash(“c”) i = 2      

#Compare ‘firstr’ and ‘second’, they don’t match, so print no.     
3#Calculate hash values for next iteration, i.e., i = 3      
#Since i is even, ‘firstr’ becomes hash(“ba”) and ‘second’ becomes hash(“cb”) i = 3      

#Compare ‘first’ and ‘second’, they don’t match, so print no.      
#Calculate hash values for next iteration, i.e., i = 4      
#Since i is odd, ‘firstr’ is not changed and ‘second’ becomes hash(“ba”) i = 4     

#‘firstr’ and ‘second’ match, compare the whole strings, they match, so print yes      
#We don’t need to calculate next hash values as this is last index The idea of using rolling hashes is, next hash value can be calculated from previous in O(1) time by just doing some constant number of arithmetic operations. Below are the implementations of above approach. 
#C
#Java
#Python
# Python program Online algorithm for checking palindrome
# in a stream
 
# d is the number of characters in input alphabet
d = 256
 
# q is a prime number used for evaluating Rabin Karp's
# Rolling hash
q = 103
 
def checkPalindromes(string):
 
    # Length of input string
    N = len(string)
 
    # A single character is always a palindrome
    print string[0] + " Yes"
 
    # Return if string has only one character
    if N == 1:
        return
 
    # Initialize first half reverse and second half for
    # as firstr and second characters
    firstr = ord(string[0]) % q
    second = ord(string[1]) % q
 
    h = 1
    i = 0
    j = 0
 
    # Now check for palindromes from second character
    # onward
    for i in xrange(1,N):
 
        # If the hash values of 'firstr' and 'second'
        # match, then only check individual characters
        if firstr == second:
 
            # Check if str[0..i] is palindrome using
            # simple character by character match
            for j in xrange(0,i/2):
                if string[j] != string[i-j]:
                    break
            j += 1
            if j == i/2:
                print string[i] + " Yes"
            else:
                print string[i] + " No"
        else:
            print string[i] + " No"
 
        # Calculate hash values for next iteration.
        # Don't calculate hash for next characters if
        # this is the last character of string
        if i != N-1:
 
            # If i is even (next i is odd)
            if i % 2 == 0:
 
                # Add next character after first half at
                # beginning of 'firstr'
                h = (h*d) % q
                firstr = (firstr + h*ord(string[i/2]))%q
 
                # Add next character after second half at
                # the end of second half.
                second = (second*d + ord(string[i+1]))%q
            else:
                # If next i is odd (next i is even) then we
                # need not to change firstr, we need to remove
                # first character of second and append a
                # character to it.
                second = (d*(second + q - ord(string[(i+1)/2])*h)%q
                            + ord(string[i+1]))%q
 
# Driver program
txt = "aabaacaabaa"
checkPalindromes(txt)
# This code is contributed by Bhavya Jain

#Output
#a Yes
#a Yes
#b No
#a No
#a Yes
#c No
#a No
#a No
#b No
#a No
#a Yes
#The worst case time complexity of the above solution remains O(n*n), but in general, it works much better than simple approach as we avoid complete substring comparison most of the time by first comparing hash values. 

#The worst case occurs for input strings with all same characters like “aaaaaa”. 

#Space Complexity: O(1)
#The algorithm uses a fixed number of variables (which is independent of the size of the input string). Hence, the space complexity of the algorithm is O(1).

#Recommended
#Solve DSA problems on GfG Practice.

#Solve Problems




#Like
#13
#Previous
#Optimized Algorithm for Pattern Searching
#Next
#Generalized Suffix Tree
#Related Articles
#1.
#C++ Program For Checking Linked List With A Loop Is Palindrome Or Not
#2.
#Java Program For Checking Linked List With A Loop Is Palindrome Or Not
#3.
#Python Program For Checking Linked List With A Loop Is Palindrome Or Not
#4.
#Javascript Program For Checking Linked List With A Loop Is Palindrome Or Not
#5.
#Sentence Palindrome (Palindrome after removing spaces, dots, .. etc)
#6.
#Count all palindrome which is square of a palindrome
#7.
#Using Set() in Python Pangram Checking
#8.
#Anagram checking in Python using collections.Counter()
#9.
#Z algorithm (Linear time pattern searching Algorithm)
#10.
#Karatsuba algorithm for fast multiplication using Divide and Conquer algorithm
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
#shrikanth13
#_shinchancode
#hardikkoriintern
#surajrasr7277
#Article Tags :
#array-stream
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
