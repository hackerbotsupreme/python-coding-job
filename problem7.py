#Aho-Corasick Algorithm for Pattern Searching

#Difficulty Level : Expert
#Last Updated : 14 Jun, 2022
#Read
#Discuss(20+)
#Courses
#Practice
#Video
#Given an input text and an array of k words, arr[], find all occurrences of all words in the input text. Let n be the length of text and m be the total number characters in all words, i.e. m = length(arr[0]) + length(arr[1]) + … + length(arr[k-1]). Here k is total numbers of input words.

#Example:  

#Input: text = "ahishers"    
#       arr[] = {"he", "she", "hers", "his"}

#Output:
#   Word his appears from 1 to 3
#3   Word he appears from 4 to 5
#   Word she appears from 3 to 5
#   Word hers appears from 4 to 7
#If we use a linear time searching algorithm like KMP, then we need to one by one search all words in text[]. This gives us total time complexity as O(n + length(word[0]) + O(n + length(word[1]) + O(n + length(word[2]) + … O(n + length(word[k-1]). This time complexity can be written as O(n*k + m). 

#Aho-Corasick Algorithm finds all words in O(n + m + z) time where z is total number of occurrences of words in text. The Aho–Corasick string matching algorithm formed the basis of the original Unix command fgrep. 


#Preprocessing : Build an automaton of all words in arr[] The automaton has mainly three functions:
#Go To :   This function simply follows edges
#          of Trie of all words in arr[]. It is
#          represented as 2D array g[][] where
#          we store next state for current state 
#          and character.

#Failure : This function stores all edges that are
#          followed when current character doesn't
#          have edge in Trie.  It is represented as
#          1D array f[] where we store next state for
#          current state. 

#Output :  Stores indexes of all words that end at 
#          current state. It is represented as 1D 
#          array o[] where we store indexes
#          of all matching words as a bitmap for 
#          current state.
#Matching : Traverse the given text over built automaton to find all matching words.
#Preprocessing: 

#We first Build a Trie (or Keyword Tree) of all words. 
 
#Building an automaton of all words in array in Aho-Corasick Algorithm
#Trie

#This part fills entries in goto g[][] and output o[].
#Next we extend Trie into an automaton to support linear time matching. 
 
#Extending the Trie into an automaton to support linear time matching

#This part fills entries in failure f[] and output o[].
#Go to : 
#We build Trie. And for all characters which don’t have an edge at root, we add an edge back to root.
#Failure : 
#For a state s, we find the longest proper suffix which is a proper prefix of some pattern. This is done using Breadth First Traversal of Trie.
#Output : 
#For a state s, indexes of all words ending at s are stored. These indexes are stored as bitwise map (by doing bitwise OR of values). This is also computing using Breadth First Traversal with Failure.



#Below is the implementation of Aho-Corasick Algorithm 


# Python program for implementation of
# Aho-Corasick algorithm for string matching
 
# defaultdict is used only for storing the final output
# We will return a dictionary where key is the matched word
# and value is the list of indexes of matched word
from collections import defaultdict
 
# For simplicity, Arrays and Queues have been implemented using lists.
# If you want to improve performance try using them instead
class AhoCorasick:
    def __init__(self, words):
 
        # Max number of states in the matching machine.
        # Should be equal to the sum of the length of all keywords.
        self.max_states = sum([len(word) for word in words])
 
        # Maximum number of characters.
        # Currently supports only alphabets [a,z]
        self.max_characters = 26
 
        # OUTPUT FUNCTION IS IMPLEMENTED USING out []
        # Bit i in this mask is 1 if the word with
        # index i appears when the machine enters this state.
        # Lets say, a state outputs two words "he" and "she" and
        # in our provided words list, he has index 0 and she has index 3
        # so value of out[state] for this state will be 1001
        # It has been initialized to all 0.
        # We have taken one extra state for the root.
        self.out = [0]*(self.max_states+1)
 
        # FAILURE FUNCTION IS IMPLEMENTED USING fail []
        # There is one value for each state + 1 for the root
        # It has been initialized to all -1
        # This will contain the fail state value for each state
        self.fail = [-1]*(self.max_states+1)
 
        # GOTO FUNCTION (OR TRIE) IS IMPLEMENTED USING goto [[]]
        # Number of rows = max_states + 1
        # Number of columns = max_characters i.e 26 in our case
        # It has been initialized to all -1.
        self.goto = [[-1]*self.max_characters for _ in range(self.max_states+1)]
         
        # Convert all words to lowercase
        # so that our search is case insensitive
        for i in range(len(words)):
          words[i] = words[i].lower()
           
        # All the words in dictionary which will be used to create Trie
        # The index of each keyword is important:
        # "out[state] & (1 << i)" is > 0 if we just found word[i]
        # in the text.
        self.words = words
 
        # Once the Trie has been built, it will contain the number
        # of nodes in Trie which is total number of states required <= max_states
        self.states_count = self.__build_matching_machine()
 
 
    # Builds the String matching machine.
    # Returns the number of states that the built machine has.
    # States are numbered 0 up to the return value - 1, inclusive.
    def __build_matching_machine(self):
        k = len(self.words)
 
        # Initially, we just have the 0 state
        states = 1
 
        # Convalues for goto function, i.e., fill goto
        # This is same as building a Trie for words[]
        for i in range(k):
            word = self.words[i]
            current_state = 0
 
            # Process all the characters of the current word
            for character in word:
                ch = ord(character) - 97 # Ascii value of 'a' = 97
 
                # Allocate a new node (create a new state)
                # if a node for ch doesn't exist.
                if self.goto[current_state][ch] == -1:
                    self.goto[current_state][ch] = states
                    states += 1
 
                current_state = self.goto[current_state][ch]
 
            # Add current word in output function
            self.out[current_state] |= (1<<i)
 
        # For all characters which don't have
        # an edge from root (or state 0) in Trie,
        # add a goto edge to state 0 itself
        for ch in range(self.max_characters):
            if self.goto[0][ch] == -1:
                self.goto[0][ch] = 0
         
        # Failure function is computed in
        # breadth first order using a queue
        queue = []
 
        # Iterate over every possible input
        for ch in range(self.max_characters):
 
            # All nodes of depth 1 have failure
            # function value as 0. For example,
            # in above diagram we move to 0
            # from states 1 and 3.
            if self.goto[0][ch] != 0:
                self.fail[self.goto[0][ch]] = 0
                queue.append(self.goto[0][ch])
 
        # Now queue has states 1 and 3
        while queue:
 
            # Remove the front state from queue
            state = queue.pop(0)
 
            # For the removed state, find failure
            # function for all those characters
            # for which goto function is not defined.
            for ch in range(self.max_characters):
 
                # If goto function is defined for
                # character 'ch' and 'state'
                if self.goto[state][ch] != -1:
 
                    # Find failure state of removed state
                    failure = self.fail[state]
 
                    # Find the deepest node labeled by proper
                    # suffix of String from root to current state.
                    while self.goto[failure][ch] == -1:
                        failure = self.fail[failure]
                     
                    failure = self.goto[failure][ch]
                    self.fail[self.goto[state][ch]] = failure
 
                    # Merge output values
                    self.out[self.goto[state][ch]] |= self.out[failure]
 
                    # Insert the next level node (of Trie) in Queue
                    queue.append(self.goto[state][ch])
         
        return states
 
 
    # Returns the next state the machine will transition to using goto
    # and failure functions.
    # current_state - The current state of the machine. Must be between
    #             0 and the number of states - 1, inclusive.
    # next_input - The next character that enters into the machine.
    def __find_next_state(self, current_state, next_input):
        answer = current_state
        ch = ord(next_input) - 97 # Ascii value of 'a' is 97
 
        # If goto is not defined, use
        # failure function
        while self.goto[answer][ch] == -1:
            answer = self.fail[answer]
 
        return self.goto[answer][ch]
 
 
    # This function finds all occurrences of all words in text.
    def search_words(self, text):
        # Convert the text to lowercase to make search case insensitive
        text = text.lower()
 
        # Initialize current_state to 0
        current_state = 0
 
        # A dictionary to store the result.
        # Key here is the found word
        # Value is a list of all occurrences start index
        result = defaultdict(list)
 
        # Traverse the text through the built machine
        # to find all occurrences of words
        for i in range(len(text)):
            current_state = self.__find_next_state(current_state, text[i])
 
            # If match not found, move to next state
            if self.out[current_state] == 0: continue
 
            # Match found, store the word in result dictionary
            for j in range(len(self.words)):
                if (self.out[current_state] & (1<<j)) > 0:
                    word = self.words[j]
 
                    # Start index of word is (i-len(word)+1)
                    result[word].append(i-len(word)+1)
 
        # Return the final result dictionary
        return result
 
# Driver code
if __name__ == "__main__":
    words = ["he", "she", "hers", "his"]
    text = "ahishers"
 
    # Create an Object to initialize the Trie
    aho_chorasick = AhoCorasick(words)
 
    # Get the result
    result = aho_chorasick.search_words(text)
 
    # Print the result
    for word in result:
        for i in result[word]:
            print("Word", word, "appears from", i, "to", i+len(word)-1)
             
# This code is contributed by Md Azharuddin

#Word his appears from 1 to 3
#Word he appears from 4 to 5
#Word she appears from 3 to 5
#Word hers appears from 4 to 7
#Time Complexity: O(n + l + z), where ‘n’ is the length of the text, ‘l’ is the length of keywords, and ‘z’ is the number of matches.

#Auxiliary Space: O(l * q), where ‘q’ is the length of the alphabet since that is the maximum number of children a node can have.

#Source: 
#http://www.cs.uku.fi/~kilpelai/BSA05/lectures/slides04.pdf
#This article is contributed by Ayush Govil. Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above
 

#Recommended
#Solve DSA problems on GfG Practice.

#Solve Problems




#Like
#25
#Previous
#Wildcard Pattern Matching
#Next
#Search a Word in a 2D Grid of characters
#Related Articles
#1.
#Z algorithm (Linear time pattern searching Algorithm)
#2.
#KMP Algorithm for Pattern Searching
#3.
#Rabin-Karp Algorithm for Pattern Searching
#34.
#Optimized Algorithm for Pattern Searching
#5.
#Finite Automata algorithm for Pattern Searching
#6.
#Boyer Moore Algorithm for Pattern Searching
#7.
#Real time optimized KMP Algorithm for Pattern Searching
#8.
#Naive algorithm for Pattern Searching
#9.
#Introduction to Pattern Searching - Data Structure and Algorithm Tutorial
#10.
#Pattern Searching | Set 6 (Efficient Construction of Finite Automata)
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
#PawelWolowiec
#2001guljain
#princi singh
#amit143katiyar
#mdAzharuddin
#adnanirshad158
#arorakashish0911
#unmeshkamleshkumar
#surindertarika1234
#sanskar84
#Article Tags :
#Pattern Searching
#Practice Tags :
#Pattern Searching