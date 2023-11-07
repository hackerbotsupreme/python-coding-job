#python program to check order of charecter in string using ordered list.
#Given an input string and a pattern, check if characters in the input string follows the same order as determined by characters present in the pattern. Assume there won’t be any duplicate characters in the pattern.

#Examples:

#Input: 
#string = "engineers rock"
#pattern = "er";
#Output: true
#Explanation: 
#All 'e' in the input string are before all 'r'.


#Input: 
#string = "engineers rock"
#pattern = "gsr";
#Output: false
#Explanation:
#There are one 'r' before 's' in the input string.

#We have existing solution for this problem, please refer Check if string follows order of characters defined by a pattern or not | Set 1. Here we solve this problem quickly in python using OrderedDict(). Approach is very simple,

#Create an OrderedDict of input string which contains characters of input strings as Key only.
#Now set a pointer at the start of pattern string.
#Now traverse generated OrderedDict and match keys with individual character of pattern string, if key and character matches with each other then increment pointer by 1.
#If pointer of pattern reaches it’s end that means string follows order of characters defined by a pattern otherwise not.

# Function to check if string follows order of
# characters defined by a pattern
from collections import OrderedDict

def checkOrder(input, pattern):
	
	# create empty OrderedDict
	# output will be like {'a': None,'b': None, 'c': None}
	dict = OrderedDict.fromkeys(input)

	# traverse generated OrderedDict parallel with
	# pattern string to check if order of characters
	# are same or not
	ptrlen = 0
	for key,value in dict.items():
		if (key == pattern[ptrlen]):
			ptrlen = ptrlen + 1
		
		# check if we have traverse complete
		# pattern string
		if (ptrlen == (len(pattern))):
			return 'true'

	# if we come out from for loop that means
	# order was mismatched
	return 'false'

# Driver program
if __name__ == "__main__":
	input = 'engineers rock'
	pattern = 'er'
	print (checkOrder(input,pattern))



# Function to check if string follows order of 
# characters defined by a pattern 
from collections import OrderedDict 
  
def checkOrder(input, pattern): 
      
    # create empty OrderedDict 
    # output will be like {'a': None,'b': None, 'c': None} 
    dict = OrderedDict.fromkeys(input) 
  
    # traverse generated OrderedDict parallel with 
    # pattern string to check if order of characters 
    # are same or not 
    ptrlen = 0
    for key,value in dict.items(): 
        if (key == pattern[ptrlen]): 
            ptrlen = ptrlen + 1
          
        # check if we have traverse complete 
        # pattern string 
        if (ptrlen == (len(pattern))): 
            return 'true'
  
    # if we come out from for loop that means 
    # order was mismatched 
    return 'false'
  
# Driver program 
if __name__ == "__main__": 
    input = 'engineers rock'
    pattern = 'er'
    print (checkOrder(input,pattern)) 
#Output:

#true
#This article is contributed by Shashank Mishra (Gullu). If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.

#Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.





























