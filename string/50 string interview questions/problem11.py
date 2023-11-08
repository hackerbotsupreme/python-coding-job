#Check if given String is Pangram or not
#Given a string Str. The task is to check if it is Pangram or not. 

#A pangram is a sentence containing every letter in the English Alphabet.

#Examples: 

#Input: “The quick brown fox jumps over the lazy dog” 
#Output: is a Pangram 
#Explanation: Contains all the characters from ‘a’ to ‘z’] 
#Input: “The quick brown fox jumps over the dog”
#Output: is not a Pangram 
#Explanation: Doesn’t contain all the characters from ‘a’ to ‘z’, as ‘l’, ‘z’, ‘y’ are missing

Strings
Data Structures
Solve Problem
Submission count: 29K
Approach: Below is the idea to solve the problem

Create a mark[] array of Boolean types and iterate through all the characters of the string and mark it as visited. Lowercase and Uppercase are considered the same. So ‘A’ and ‘a’ are marked in index 0 and similarly ‘Z’ and ‘z’ are marked in index 25.



After iterating through all the characters check whether all the characters are marked or not. If not then return false as this is not a pangram else return true. 

Follow the below steps to Implement the idea:

Create a bool vector mark[] of size 26.
Iterate through all characters of the string str and mark str[i] – ‘a’ or str[i] – ‘A’ as 1 for lower and upper characters respectively.
Iterate through all the indices of mark[] 
If all indices are marked visited then return is a Pangram 
Else return  is not a Pangram.
Below is the Implementation of above approach


# A Python Program to check if the given
# string is a pangram or not
 
 
def checkPangram(s):
    List = []
    # create list of 26 characters and set false each entry
    for i in range(26):
        List.append(False)
 
    # converting the sentence to lowercase and iterating
    # over the sentence
    for c in s.lower():
        if not c == " ":
 
            # make the corresponding entry True
            List[ord(c) - ord('a')] = True
 
    # check if any character is missing then return False
    for ch in List:
        if ch == False:
            return False
    return True
 
 
# Driver Program to test above functions
sentence = "The quick brown fox jumps over the little lazy dog"
 
if (checkPangram(sentence)):
    print('"'+sentence+'"')
    print("\nis a pangram")
else:
    print('"'+sentence+'"')
    print("\nis not a pangram")
 
# This code is contributed by Danish Mushtaq
#Output
# The quick brown fox jumps over the lazy dog 
#is a pangram
#Time Complexity: O(n), where n is the length of our string 
#Auxiliary Space: O(1), as 26 size Boolean vector is constant. 

#This article is contributed by Rachit Belwariar. If you like GeeksforGeeks and would like to contribute, you can also write an article and mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.
