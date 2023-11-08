#Given a sequence of words, print all anagrams together | Set 1

#Given an array of words, print all anagrams together. For example, if the given array is {“cat”, “dog”, “tac”, “god”, “act”}, then output may be “cat tac act dog god”.
#------------------------------------------------------------------------
#A simple method is to create a Hash Table. Calculate the hash value of each word in such a way that all anagrams have the same hash value. Populate the Hash Table with these hash values. Finally, print those words together with the same hash values. A simple hashing mechanism can be modulo sum of all characters. With modulo sum, two non-anagram words may have the same hash value. This can be handled by matching individual characters.

#Following is another method to print all anagrams together. Take two auxiliary arrays, index array, and word array. Populate the word array with the given sequence of words. Sort each individual word of the word array. Finally, sort the word array and keep track of the corresponding indices. After sorting, all the anagrams cluster together. Use the index array to print the strings from the original array of strings.

#Let us understand the steps with the following input Sequence of Words: 
#"cat", "dog", "tac", "god", "act"

#1) Create two auxiliary arrays index[] and words[]. Copy all given words to words[] and store the original indexes in index[] 

#index[]:  0   1   2   3   4
#words[]: cat dog tac god act
#2) Sort individual words in words[]. Index array doesn’t change.

#index[]:   0    1    2    3    4
#words[]:  act  dgo  act  dgo  act
#3) Sort the words array. Compare individual words using strcmp() to sort



#index:     0    2    4    1    3
#words[]:  act  act  act  dgo  dgo
#4) All anagrams come together. But words are changed in the words array. To print the original words, take the index from the index array and use it in the original array. We get 

#"cat tac act dog god"
#Following are the implementations of the above algorithm. In the following program, an array of structure “Word” is used to store both index and word arrays. Dupray is another structure that stores an array of structure “Word”.
# A Python program to print all anagrams together

# structure for each word of duplicate array


class Word(object):
	def __init__(self, string, index):
		self.string = string
		self.index = index

# Create a DupArray object that contains an array
# of Words


def createDupArray(string, size):
	dupArray = []

	# One by one copy words from the given wordArray
	# to dupArray
	for i in xrange(size):
		dupArray.append(Word(string[i], i))

	return dupArray

# Given a list of words in wordArr[]


def printAnagramsTogether(wordArr, size):
	# Step 1: Create a copy of all words present in
	# given wordArr.
	# The copy will also have original indexes of words
	dupArray = createDupArray(wordArr, size)

	# Step 2: Iterate through all words in dupArray and sort
	# individual words.
	for i in xrange(size):
		dupArray[i].string = ''.join(sorted(dupArray[i].string))

	# Step 3: Now sort the array of words in dupArray
	dupArray = sorted(dupArray, key=lambda k: k.string)

	# Step 4: Now all words in dupArray are together, but
	# these words are changed. Use the index member of word
	# struct to get the corresponding original word
	for word in dupArray:
		print wordArr[word.index],


# Driver program
wordArr = ["cat", "dog", "tac", "god", "act"]
size = len(wordArr)
printAnagramsTogether(wordArr, size)

# This code is contributed by BHAVYA JAIN
#Output: 

#cat tac act dog god 
#Time Complexity: Let there be N-words and each word has a maximum of M characters. The upper bound is O(NMLogM + MNLogN). 
#Step 2 takes O(NMLogM) time. Sorting a word takes maximum O(MLogM) time. So sorting N-words takes O(NMLogM) time. step 3 takes O(MNLogN) Sorting array of words takes NLogN comparisons. A comparison may take maximum O(M) time. So time to sort an array of words will be O(MNLogN).
#-------------------------------------------------------------------------------------
#Using vector of pair :

#The problem can easily be solved with the use of a vector of pairs. The pair will be of string and int. The string will require to store the input string and int will require to store their respective indexes. 

#here is the implementation of the above approach:
from typing import List, Tuple
def create_duplicate_array(wordAr: List[str]) -> List[Tuple[str, int]]:
	dup_array = []
	# Iterate through the original list of words
	for i, word in enumerate(wordAr):
		# Append each word along with its index in the original list to the duplicate array
		dup_array.append((word, i))
	return dup_array

# Function to print out all the words that are anagrams of each other next to each other
def print_anagrams_together(wordArr: List[str]):
	# Create a duplicate array containing the words and their indices
	dup_array = create_duplicate_array(wordArr)

	# Iterate through the duplicate array and sort each word alphabetically
	for i in range(len(wordArr)):
		dup_array[i] = (sorted(dup_array[i][0]), dup_array[i][1])
	# Sort the duplicate array based on the sorted words
	dup_array.sort()

	# Iterate through the sorted duplicate array and print out the original words using their indices
	for i in range(len(wordArr)):
		print(wordArr[dup_array[i][1]], end=' ')

# Test the function with an example list of words
wordArr = ["cat", "dog", "tac", "god", "act"]
print_anagrams_together(wordArr)

# This code is contributed by Shivam Tiwari


#Output
#cat tac act dog god 
#Time complexity: 

#Let there be N-words and each word has a maximum of M characters.

# O(NMLogM + MNLogN). 
#--------------------------------------------------------------------------------------
#Using hashmap
#Here, we first sort each word, use the sorted word as a key and then put an original word on a map. The value of the map will be a list containing all the words which have the same word after sorting. 
#Lastly, we will print all values from the hashmap where the size of values will be greater than 1.
from collections import defaultdict


def printAnagramsTogether(words):
	groupedWords = defaultdict(list)

	# Put all anagram words together in a dictionary
	# where key is sorted word
	for word in words:
		groupedWords["".join(sorted(word))].append(word)

	# Print all anagrams together
	for group in groupedWords.values():
		print(" ".join(group))


if __name__ == "__main__":
	arr = ["cat", "dog", "tac", "god", "act"]
	printAnagramsTogether(arr)
#Output
#[dog, god][cat, tac, act]
#Time Complexity :  O(M+N). 

#Auxiliary space: O(M x N). 
#---------------------------------------------------------------------------
#HashMap with O(NM) Solution
#In the previous approach, we were sorting every string in order to maintain a similar key, but that cost extra time in this approach will take the advantage of another hashmap to maintain the frequency of the characters which will generate the same hash function for different string having same frequency of characters.
#Here, we will take HashMap<HashMap, ArrayList>, the inner hashmap will count the frequency of the characters of each string and the outer HashMap will check whether that hashmap is present or not if present then it will add that string to the corresponding list. 
# Python code to print all anagrams together
from collections import Counter, defaultdict
user_input = ["cat", "dog", "tac", "edoc", "god", "tacact",
			"act", "code", "deno", "node", "ocde", "done", "catcat"]


def solve(words: list) -> list:
	# defaultdict will create a new list if the key is not found in the dictionary
	m = defaultdict(list)

	# loop over all the words
	for word in words:
		# Counter('cat') :
		# counts the frequency of the characters present in a string
		# >>> Counter({'c': 1, 'a': 1, 't': 1})

		# frozenset(dict(Counter('cat')).items()) :
		# frozenset takes an iterable object as input and makes them immutable.
		# So that hash(frozenset(Counter('cat'))) is equal to
		# hash of other 'cat' anagrams
		# >>> frozenset({('c', 1), ('a', 1), ('t', 1)})
		m[frozenset(dict(Counter(word)).items())].append(word)
	return [v for k, v in m.items()]


print(solve(user_input))

# This code is contributed by
# Rohan Kumar(@r0hnx)
#Output
#[cat, atc, ][dog, ogd, god, ]