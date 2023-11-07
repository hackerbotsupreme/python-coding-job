#python dictionaries , set  and counter to check if freqencies if frequencies can become same .

#Given a string which contains lower alphabetic characters, we need to remove at most one character from this string in such a way that frequency of each distinct character becomes same in the string.

#Examples:

#Input  : str = “xyyz”
#Output : Yes
#We can remove character ’y’ from above 
#string to make the frequency of each 
#character same. 

#Input : str = “xyyzz” 
#Output : Yes
#We can remove character ‘x’ from above 
#string to make the frequency of each 
#character same.

#Input : str = “xxxxyyzz” 
#Output : No
#It is not possible to make frequency of 
#each character same just by removing at 
#most one character from above string.
#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#This problem has existing solution please refer Check if frequency of all characters can become same by one removal link. We will solve this problem quickly in Python. Approach is very simple,

#We need to count frequency of each letter in string, for this we will use Counter(input) method, it returns a dictionary having characters as keys and their respective frequencies as values.
#Now extract list of frequencies of each character and push these values in Set() data structure in python.
#Since set contains unique values, so if size of set is 1 that means frequencies of all characters were same, if size of set is 2 then check if value of first element is 1 or not ( if 1 then we can make same frequency by removing one character at most otherwise not possible ).
# Function to Check if frequency of all characters
# can become same by one removal
from collections import Counter
  
def allSame(input):
      
    # calculate frequency of each character
    # and convert string into dictionary
    dict=Counter(input)
  
    # now get list of all values and push it
    # in set
    same = list(set(dict.values()))
  
    if len(same)>2:
        print('No')
    elif len (same)==2 and same[1]-same[0]>1:
        print('No')
    else:
        print('Yes')
  
      
    # now check if frequency of all characters 
    # can become same
      
# Driver program
if __name__ == "__main__":
    input = 'xxxyyzzt'
    allSame(input)