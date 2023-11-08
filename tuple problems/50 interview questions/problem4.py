#Generate two output strings depending upon occurrence of character in input string in Python

#Last Updated : 28 Jul, 2022

#Given an input string str[], generate two output strings. One of which consists of those character which occurs only once in input string and second which consists of multi-time occurring characters. Output strings must be sorted. 

#Examples:

#Input : str = "geeksforgeeks"
#Output : String with characters occurring once:
#"for".
#String with characters occurring multiple times:
#"egks"

#Input : str = "geekspractice"
#Output : String with characters occurring once:
#"agikprst"
#String with characters occurring multiple times:
#"ce"
#We have existing solution for this problem please refer Generate two output strings depending upon occurrence of character in input string link. We can solve this problem quickly in python using Counter(iterable) method. Approach is simple,

#Convert string into dictionary having characters as keys and their frequencies as value using counter() method.
#Now separate out list of characters having frequency 1 and having frequency more than 1.
#Sort characters in both lists to get output strings.
#Implementation:

#Python3
# Function Generate two output strings depending upon
# occurrence of character in input string
 
from collections import Counter
 
def generateStrings(input):
     
    # convert string into dictionary
    # having characters as keys and frequency as value
    freqDict = Counter(input)
 
    # separate out characters having frequency 1 and more than 1
    freq1 = [ key for (key,count) in freqDict.items() if count==1]
    freqMore1 = [ key for (key,count) in freqDict.items() if count>1]
 
    # sort lists and concatenate characters
    # with out space to print resultant strings
    freq1.sort()
    freqMore1.sort()
 
    # print output strings
    print ('String with characters occurring once:')
    print (''.join(freq1))
    print ('String with characters occurring multiple times:')
    print (''.join(freqMore1))
 
# Driver program
if __name__ == "__main__":
    input = "geeksforgeeks"
    generateStrings(input)
#Output
#String with characters occurring once:
#for
#String with characters occurring multiple times:
#egks