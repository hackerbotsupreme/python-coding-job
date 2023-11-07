#Suffix Array | Set 1 (Introduction)

#Difficulty Level : Medium
#Last Updated : 24 Jan, 2023
#Read
#Discuss(40+)
#Courses
#Practice
#Video
#We strongly recommend to read following post on suffix trees as a pre-requisite for this post.
#Pattern Searching | Set 8 (Suffix Tree Introduction)
#A suffix array is a sorted array of all suffixes of a given string. The definition is similar to Suffix Tree which is compressed trie of all suffixes of the given text. Any suffix tree based algorithm can be replaced with an algorithm that uses a suffix array enhanced with additional information and solves the same problem in the same time complexity (Source Wiki). 
#A suffix array can be constructed from Suffix tree by doing a DFS traversal of the suffix tree. In fact Suffix array and suffix tree both can be constructed from each other in linear time. 
#Advantages of suffix arrays over suffix trees include improved space requirements, simpler linear time construction algorithms (e.g., compared to Ukkonen’s algorithm) and improved cache locality (Source: Wiki)
#Example: 
# ##

##Let the given string be "banana".#

#0 banana                          5 a
#1 anana     Sort the Suffixes     3 ana
#2 nana      ---------------->     1 anana  
#3 ana        alphabetically       0 banana  
#4 na                              4 na   
#5 a                               2 nana

#So the suffix array for "banana" is {5, 3, 1, 0, 4, 2}
#Naive method to build Suffix Array 
#A simple method to construct suffix array is to make an array of all suffixes and then sort the array. Following is implementation of simple method.
 

#CPP
#Java
#Javascript
#Python3
# Naive algorithm for building suffix array of a given text
import sys
 
# Structure to store information of a suffix
class Suffix:
    def __init__(self, index, suff):
        self.index = index
        self.suff = suff
 
# A comparison function used by sort() to compare two suffixes
def cmp(a, b):
    return (a.suff < b.suff) - (a.suff > b.suff)
 
# This is the main function that takes a string 'txt' of size n as an
# argument, builds and return the suffix array for the given string
def build_suffix_array(txt, n):
    # A structure to store suffixes and their indexes
    suffixes = [Suffix(i, txt[i:]) for i in range(n)]
 
    # Sort the suffixes using the comparison function
    # defined above.
    suffixes.sort(key=cmp)
 
    # Store indexes of all sorted suffixes in the suffix array
    suffix_arr = [suffixes[i].index for i in range(n)]
 
    # Return the suffix array
    return suffix_arr
 
# A utility function to print an array of given size
def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
# Driver program to test above functions
def main():
    txt = "banana"
    n = len(txt)
    suffix_arr = build_suffix_array(txt, n)
    print("Following is suffix array for", txt)
    print_arr(suffix_arr)
 
if __name__ == "__main__":
    main()
#Output
#Following is suffix array for banana
#5 3 1 0 4 2 
#Time Complexity: O(n*k*Logn). if we consider a O(nLogn)) algorithm used for sorting. The sorting step itself takes O(n*k*Logn) time as every comparison is a comparison of two strings and the comparison takes O(K) time where K is max length of string in given array. 
#Auxiliary Space: O(n)

#There are many efficient algorithms to build suffix array. We will soon be covering them as separate posts.
#Search a pattern using the built Suffix Array 
#To search a pattern in a text, we preprocess the text and build a suffix array of the text. Since we have a sorted array of all suffixes, Binary Search can be used to search. Following is the search function. Note that the function doesn’t report all occurrences of pattern, it only report one of them.
 

#CPP
#// This code only contains search() and main. To make it a complete running
#// above code or see https://ide.geeksforgeeks.org/oY7OkD
 
#// A suffix array based search function to search a given pattern
#// 'pat' in given text 'txt' using suffix array suffArr[]
#void search(char *pat, char *txt, int *suffArr, int n)
{
    int m = strlen(pat);  // get length of pattern, needed for strncmp()
 
    // Do simple binary search for the pat in txt using the
    // built suffix array
    int l = 0, r = n-1;  // Initialize left and right indexes
    while (l <= r)
    {
        // See if 'pat' is prefix of middle suffix in suffix array
        int mid = l + (r - l)/2;
        int res = strncmp(pat, txt+suffArr[mid], m);
 
        // If match found at the middle, print it and return
        if (res == 0)
        {
            cout << "Pattern found at index " << suffArr[mid];
            return;
        }
 
        // Move to left half if pattern is alphabetically less than
        // the mid suffix
        if (res < 0) r = mid - 1;
 
        // Otherwise move to right half
        else l = mid + 1;
    }
 
    // We reach here if return statement in loop is not executed
    cout << "Pattern not found";
}
 
// Driver program to test above function
int main()
{
    char txt[] = "banana";  // text
    char pat[] = "nan";   // pattern to be searched in text
 
    // Build suffix array
    int n = strlen(txt);
    int *suffArr = buildSuffixArray(txt, n);
 
    // search pat in txt using the built suffix array
    search(pat, txt, suffArr, n);
 
    return 0;
}
#Javascript
#Output: 
 

#Pattern found at index 2
#Time Complexity: O(mlogn)
#Auxiliary Space: O(m+n) 



# There are more efficient algorithms to search pattern once the suffix array is built. In fact there is a O(m) suffix array based algorithm to search a pattern. We will soon be discussing efficient algorithm for search.
#Applications of Suffix Array 
#Suffix array is an extremely useful data structure, it can be used for a wide range of problems. Following are some famous problems where Suffix array can be used. 
#1) Pattern Searching 
#2) Finding the longest repeated substring 
#3) Finding the longest common substring 
#4) Finding the longest palindrome in a string
 

#See this for more problems where Suffix arrays can be used.
#This post is a simple introduction. There is a lot to cover in Suffix arrays. We have discussed a O(nLogn) algorithm for Suffix Array construction here. We will soon be discussing more efficient suffix array algorithms.
#References: 
#http://www.stanford.edu/class/cs97si/suffix-array.pdf 
#http://en.wikipedia.org/wiki/Suffix_array
#Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above
 

#Recommended
#Solve DSA problems on GfG Practice.

#Solve Problems




#Like
#21
#Previous
#General Tree (Each node can have arbitrary number of children) Level Order Traversal
#Next
#Persistent data structures
#Related Articles
#1.
#Construct array B as last element left of every suffix array obtained by performing given operations on every suffix of given array
#2.
#Suffix Tree Application 4 - Build Linear Time Suffix Array
#3.
#Suffix Array | Set 2 (nLogn Algorithm)
#4.
­ #­kasai’s Algorithm for Construction of LCP array from Suffix Array
#5.
#Count indices where the maximum in the prefix array is less than that in the suffix array
#6.
#Find the longest sub-string which is prefix, suffix and also present inside the string | Set 2
#7.
#Count of distinct substrings of a string using Suffix Array
8#.
#Counting k-mers via Suffix Array
#9.
#Find position i to split Array such that prefix sum till i-1, i and suffix sum till i+1 are in GP with common ratio K
#10.
#Find the Suffix Array of given String with no repeating character
#Article Contributed By :
#h#ttps://media.geeksforgeeks.org/auth/avatar.png
##GeeksforGeeks
#Vote for difficulty
#Current difficulty : Medium
#Easy
#N#ormal
##Medium
#Hard
#Expert
#Improved By :
#s#weetyty
##devro3014
#rajeev0719singh
#ayush786113
#vivekanand1108
#s#atwiksuman
##Article Tags :
#Suffix-Array
#Advanced Data Structure
#Pattern Searching
#P#ractice Tags :
##Advanced Data Structure
#Pattern Searchin#g