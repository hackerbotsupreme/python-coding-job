#Boyer Moore Algorithm for Pattern Searching

#Difficulty Level : Hard
#Last Updated : 09 Nov, 2022
#Read
#Discuss
#Courses
#Practice
#Video
#Pattern searching is an important problem in computer science. When we do search for a string in a notepad/word file, browser, or database, pattern searching algorithms are used to show the search results. A typical problem statement would be- 
#Given a text txt[0..n-1] and a pattern pat[0..m-1] where n is the length of the text and m is the length of the pattern, write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m. 
#Examples: 

#Input:  txt[] = "THIS IS A TEST TEXT"
#        pat[] = "TEST"
#Output: Pattern found at index 10

#Input:  txt[] =  "AABAACAADAABAABA"
#        pat[] =  "AABA"
#Output: Pattern found at index 0
#        Pattern found at index 9
#        Pattern found at index 12


#In this post, we will discuss the Boyer Moore pattern searching algorithm. Like KMP and Finite Automata algorithms, Boyer Moore algorithm also preprocesses the pattern. 
#Boyer Moore is a combination of the following two approaches. 

#Bad Character Heuristic 
#Good Suffix Heuristic 
#Both of the above heuristics can also be used independently to search a pattern in a text. Let us first understand how two independent approaches work together in the Boyer Moore algorithm. If we take a look at the Naive algorithm, it slides the pattern over the text one by one. KMP algorithm does preprocessing over the pattern so that the pattern can be shifted by more than one. The Boyer Moore algorithm does preprocessing for the same reason. It processes the pattern and creates different arrays for each of the two heuristics. At every step, it slides the pattern by the max of the slides suggested by each of the two heuristics. So it uses greatest offset suggested by the two heuristics at every step. 

#Unlike the previous pattern searching algorithms, the Boyer Moore algorithm starts matching from the last character of the pattern.
#In this post, we will discuss the bad character heuristic and the Good Suffix heuristic in the next post. 

# Bad Character Heuristic

#The idea of bad character heuristic is simple. The character of the text which doesn’t match with the current character of the pattern is called the Bad Character. Upon mismatch, we shift the pattern until – 



#The mismatch becomes a match.
#Pattern P moves past the mismatched character.
#Case 1 – Mismatch become match 
#We will lookup the position of the last occurrence of the mismatched character in the pattern, and if the mismatched character exists in the pattern, then we’ll shift the pattern such that it becomes aligned to the mismatched character in the text T. 
 

#Boyer Moore Algorithm for Pattern Searching
#case 1

#Explanation: In the above example, we got a mismatch at position 3. Here our mismatching character is “A”. Now we will search for last occurrence of “A” in pattern. We got “A” at position 1 in pattern (displayed in Blue) and this is the last occurrence of it. Now we will shift pattern 2 times so that “A” in pattern get aligned with “A” in text.

#Case 2 – Pattern move past the mismatch character 
#We’ll lookup the position of last occurrence of mismatching character in pattern and if character does not exist we will shift pattern past the mismatching character. 
 

#Boyer Moore Algorithm for Pattern Searching
#case2

#Explanation: 

#Here we have a mismatch at position 7. The mismatching character “C” does not exist in pattern before position 7 so we’ll shift pattern past to the position 7 and eventually in above example we have got a perfect match of pattern (displayed in Green). We are doing this because “C” does not exist in the pattern so at every shift before position 7 we will get mismatch and our search will be fruitless.

#In the following implementation, we preprocess the pattern and store the last occurrence of every possible character in an array of size equal to alphabet size. If the character is not present at all, then it may result in a shift by m (length of pattern). Therefore, the bad character heuristic takes O(n/m)                      time in the best case. 
 

# Python3 Program for Bad Character Heuristic
# of Boyer Moore String Matching Algorithm
 
NO_OF_CHARS = 256
 
def badCharHeuristic(string, size):
    '''
    The preprocessing function for
    Boyer Moore's bad character heuristic
    '''
 
    # Initialize all occurrence as -1
    badChar = [-1]*NO_OF_CHARS
 
    # Fill the actual value of last occurrence
    for i in range(size):
        badChar[ord(string[i])] = i;
 
    # return initialized list
    return badChar
 
def search(txt, pat):
    '''
    A pattern searching function that uses Bad Character
    Heuristic of Boyer Moore Algorithm
    '''
    m = len(pat)
    n = len(txt)
 
    # create the bad character list by calling
    # the preprocessing function badCharHeuristic()
    # for given pattern
    badChar = badCharHeuristic(pat, m)
 
    # s is shift of the pattern with respect to text
    s = 0
    while(s <= n-m):
        j = m-1
 
        # Keep reducing index j of pattern while
        # characters of pattern and text are matching
        # at this shift s
        while j>=0 and pat[j] == txt[s+j]:
            j -= 1
 
        # If the pattern is present at current shift,
        # then index j will become -1 after the above loop
        if j<0:
            print("Pattern occur at shift = {}".format(s))
 
            '''   
                Shift the pattern so that the next character in text
                      aligns with the last occurrence of it in pattern.
                The condition s+m < n is necessary for the case when
                   pattern occurs at the end of text
               '''
            s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
        else:
            '''
               Shift the pattern so that the bad character in text
               aligns with the last occurrence of it in pattern. The
               max function is used to make sure that we get a positive
               shift. We may get a negative shift if the last occurrence
               of bad character in pattern is on the right side of the
               current character.
            '''
            s += max(1, j-badChar[ord(txt[s+j])])
 
 
# Driver program to test above function
def main():
    txt = "ABAAABCD"
    pat = "ABC"
    search(txt, pat)
 
if __name__ == '__main__':
    main()
 
# This code is contributed by Atul Kumar
# (www.facebook.com/atul.kr.007)

#Output
#pattern occurs at shift = 4
#Time Complexity : O(n x m)

#Auxiliary Space: O(1)

#The Bad Character Heuristic may take O(mn)                      time in worst case. The worst case occurs when all characters of the text and pattern are same. For example, txt[] = “AAAAAAAAAAAAAAAAAA” and pat[] = “AAAAA”. The Bad Character Heuristic may take O(n/m) in the best case. The best case occurs when all the characters of the text and pattern are different. 

#Boyer Moore Algorithm | Good Suffix heuristic

#This article is contributed by Aarti_Rathi. If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.
#Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.

#Recommended
#Solve DSA problems on GfG Practice.

#Solve Problems




#Like
#112
#Previous
#Finite Automata algorithm for Pattern Searching
##Next
#Manacher's Algorithm - Linear Time Longest Palindromic Substring - Part 4
#Related Articles
#1.
#Boyer Moore Algorithm | Good Suffix heuristic
#2.
#Z algorithm (Linear time pattern searching Algorithm)
#3.
#KMP Algorithm for Pattern Searching
#4.
#Rabin-Karp Algorithm for Pattern Searching
#5.
#Optimized Algorithm for Pattern Searching
#6.
#Finite Automata algorithm for Pattern Searching
#7.
#Aho-Corasick Algorithm for Pattern Searching
#8.
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
#ukasp
#princiraj1992
#rathbhupendra
#Kirti_Mangal
#nidhi_biet
#sandellfamily2013
#unknown2108
#adnanirshad158
#ayaankhan98
#sweetyty
#stryker27
#germanshephered48
#amartyaghoshgfg
#sumitgumber28
#hardikkoriintern
#codewithshinchan
#mitalibhola94
#mayanka5934
#Article Tags :
#Pattern Searching
#Strings
#Practice Tags :
#Pattern Searching
#String#s