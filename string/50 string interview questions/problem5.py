#Find the minimum distance between the given two words


#Given a list of words followed by two words, the task is to find the minimum distance between the given two words in the list of words.

#Examples:

#Input: S = { “the”, “quick”, “brown”, “fox”, “quick”}, word1 = “the”, word2 = “fox”
#Output: 3
#Explanation: Minimum distance between the words “the” and “fox” is 3

#Input: S = {“geeks”, “for”, “geeks”, “contribute”,  “practice”}, word1 = “geeks”, word2 = “practice”
#Output: 2
#Explanation: Minimum distance between the words “geeks” and “practice” is 2


------------------------------------------------------------
#Approach: Follow the steps to solve this problem:

#Initialize the variables d1 = -1, d2 = -1 and ans = INT_MAX.
#Traverse the string and check:
#If, s[i] is word1 then update d1 = i.
#If, s[i] is word2 then update d2 = i.
#If, d1 != -1 and d2 != -1, then update ans = min(ans, abs(d1-d2)).
#After traversing the string, return ans.
#Below is the implementation of the above approach.





# Python3 code to implement the approach

# Function to return shortest distance
def shortestDistance(s, word1, word2) :

    d1 = -1; d2 = -1;
    ans = 100000000;

    # Traverse the string
    for i in range(len(s)) :
        if (s[i] == word1) :
            d1 = i;
        if (s[i] == word2) :
            d2 = i;
        if (d1 != -1 and d2 != -1) :
            ans = min(ans, abs(d1 - d2));

    # Return the answer
    return ans;

# Driver Code
if __name__ == "__main__" :

    S = [ "the", "quick", "brown", "fox", "quick" ];

    word1 = "the"; word2 = "fox";

    # Function Call
    print(shortestDistance(S, word1, word2));

   # This code is contributed by AnkThon
#Output


#3
#Time Complexity: O(N)
#Auxiliary Space: O(1)



   
   





