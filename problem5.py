#Finite Automata algorithm for Pattern Searching

#Difficulty Level : Hard
#Last Updated : 15 Jun, 2022
#Read
#Discuss
#Courses
#Practice
#Video
#Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.
#Examples: 

#Input:  txt[] = "THIS IS A TEST TEXT"
#        pat[] = "TEST"
#Output: Pattern found at index 10

#Input:  txt[] =  "AABAACAADAABAABA"
#        pat[] =  "AABA"
#Output: Pattern found at index 0
#        Pattern found at index 9
#        Pattern found at index 12
#Pattern

 
#Pattern searching is an important problem in computer science. When we do search for a string in notepad/word file or browser or database, pattern searching algorithms are used to show the search results. 
#We have discussed the following algorithms in the previous posts:
#Naive Algorithm 
#KMP Algorithm 
#Rabin Karp Algorithm
#In this post, we will discuss Finite Automata (FA) based pattern searching algorithm. In FA based algorithm, we preprocess the pattern and build a 2D array that represents a Finite Automata. Construction of the FA is the main tricky part of this algorithm. Once the FA is built, the searching is simple. In search, we simply need to start from the first state of the automata and the first character of the text. At every step, we consider next character of text, look for the next state in the built FA and move to a new state. If we reach the final state, then the pattern is found in the text. The time complexity of the search process is O(n). 
#Before we discuss FA construction, let us take a look at the following FA for pattern ACACAGA. 
 

#Finite Automata algorithm for Pattern Searching 1

 

#Finite Automata algorithm for Pattern Searching 2

#The above diagrams represent graphical and tabular representations of pattern ACACAGA.
#Number of states in FA will be M+1 where M is length of the pattern. The main thing to construct FA is to get the next state from the current state for every possible character. Given a character x and a state k, we can get the next state by considering the string “pat[0..k-1]x” which is basically concatenation of pattern characters pat[0], pat[1] … pat[k-1] and the character x. The idea is to get length of the longest prefix of the given pattern such that the prefix is also suffix of “pat[0..k-1]x”. The value of length gives us the next state. For example, let us see how to get the next state from current state 5 and character ‘C’ in the above diagram. We need to consider the string, “pat[0..4]C” which is “ACACAC”. The length of the longest prefix of the pattern such that the prefix is suffix of “ACACAC”is 4 (“ACAC”). So the next state (from state 5) is 4 for character ‘C’. 
#In the following code, computeTF() constructs the FA. The time complexity of the computeTF() is O(m^3*NO_OF_CHARS) where m is length of the pattern and NO_OF_CHARS is size of alphabet (total number of possible characters in pattern and text). The implementation tries all possible prefixes starting from the longest possible that can be a suffix of “pat[0..k-1]x”. There are better implementations to construct FA in O(m*NO_OF_CHARS) (Hint: we can use something like lps array construction in KMP algorithm). We have covered the better implementation in our next post on pattern searching.
 




# Python program for Finite Automata
# Pattern searching Algorithm
 
NO_OF_CHARS = 256
 
def getNextState(pat, M, state, x):
    '''
    calculate the next state
    '''
 
    # If the character c is same as next character
      # in pattern, then simply increment state
 
    if state < M and x == ord(pat[state]):
        return state+1
 
    i=0
    # ns stores the result which is next state
 
    # ns finally contains the longest prefix
     # which is also suffix in "pat[0..state-1]c"
 
     # Start from the largest possible value and
      # stop when you find a prefix which is also suffix
    for ns in range(state,0,-1):
        if ord(pat[ns-1]) == x:
            while(i<ns-1):
                if pat[i] != pat[state-ns+1+i]:
                    break
                i+=1
            if i == ns-1:
                return ns
    return 0
 
def computeTF(pat, M):
    '''
    This function builds the TF table which
    represents Finite Automata for a given pattern
    '''
    global NO_OF_CHARS
 
    TF = [[0 for i in range(NO_OF_CHARS)]\
          for _ in range(M+1)]
 
    for state in range(M+1):
        for x in range(NO_OF_CHARS):
            z = getNextState(pat, M, state, x)
            TF[state][x] = z
 
    return TF
 
def search(pat, txt):
    '''
    Prints all occurrences of pat in txt
    '''
    global NO_OF_CHARS
    M = len(pat)
    N = len(txt)
    TF = computeTF(pat, M)   
 
    # Process txt over FA.
    state=0
    for i in range(N):
        state = TF[state][ord(txt[i])]
        if state == M:
            print("Pattern found at index: {}".\
                   format(i-M+1))
 
# Driver program to test above function           
def main():
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    search(pat, txt)
 
if __name__ == '__main__':
    main()
 
# This code is contributed by Atul Kumar

#Output: 
 

#  Pattern found at index 0
#  Pattern found at index 9
#  Pattern found at index 13
#Time Complexity: O(m2)

#Auxiliary Space: O(m)

#References: 
#Introduction to Algorithms by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein
#Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.
 
#
#Recommended
#Solve DSA problems on GfG Practice.

#Solve Problems




#Like
#24
#Previous
#Nth Even length Palindrome
#Next
#Boyer Moore Algorithm for Pattern Searching
#Related Articles
#1.
#Pattern Searching | Set 6 (Efficient Construction of Finite Automata)
#2.
#Z algorithm (Linear time pattern searching Algorithm)
#3.
#KMP Algorithm for Pattern Searching
#4.
#Rabin-Karp Algorithm for Pattern Searching
#5.
#Optimized Algorithm for Pattern Searching
#6.
#Boyer Moore Algorithm for Pattern Searching
#7.
#Aho-Corasick Algorithm for Pattern Searching
##8.
#Real time optimized KMP Algorithm for Pattern Searching
#9.
#Naive algorithm for Pattern Searching
#10.
#Introduction to Pattern Searching - Data Structure and Algorithm Tutorial
#Article Contributed By :
#https://media.geeksforgeeks.org/auth/avatar.png
#GeeksforGeeks
#Vote for difficulty
#Current difficulty : Hard
#Easy
#Normal
#Medium
#Hard
#Expert
#Improved By :
#debjitdbb
#shrikanth13
#rathbhupendra
#avanitrachhadiya2155
#amartyaghoshgfg
#geekygirl2001
#Article Tags :
#Pattern Searching
#Practice Tags :
#Pattern Searching