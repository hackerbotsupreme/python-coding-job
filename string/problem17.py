#License Key Formatting

#Given a string S that consists of only alphanumeric characters and dashes. The string is separated into N + 1 groups by N dashes. Also given an integer K.

#We want to reformat the string S, such that each group contains exactly K characters, except for the first group, which could be shorter than K but still must contain at least one character. Furthermore, a dash must be inserted between two groups, and you should convert all lowercase letters to uppercase.

#Return the reformatted string.
#Examples:


#Input: S = “5F3Z-2e-9-w”, K = 4
#Output: “5F3Z-2E9W”
#Explanation: The string S has been split into two parts,  
#each part has 4 characters. 
#Note that two extra dashes are not needed and can be removed.

#Input: S = “2-5g-3-J”, K = 2
#Output: “2-5G-3J”
#Explanation: The string s has been split into three parts,  
#each part has 2 characters except the first part 
#as it could be shorter as mentioned above


#---------------------------------------------------
#Naive Approach: To solve the problem follow the below idea:



#We will have a Greedy approach in which we will create a temporary string with only the alphanumeric characters(but in reverse) and then add the dashes after every K step.
#The reversal is necessary at the beginning because each group contains exactly K characters, except for the first group as mentioned in the problem.
#Follow the steps to solve the problem:

#Create an empty string temp and push only the characters (in upper-case) that are different than ‘-‘.
#Now reverse the string obtained. Also, create a string ‘ans’ to store the final string.
#Iterate over the string and whenever ‘K’ characters are pushed in ‘ans’ push a dash “-” into the string.
#Return ‘ans’ as the result.
#Below is the implementation to solve the problem:

# Python code for the above approach

# Function to compute the answer
def ReFormatStrings(s,k):

    # Create a temporary string to store the alphanumeric characters only
    temp = ""
    n = len(s)
    for i in range(0,n):
        if(s[i] != '-'):
            temp += s[i].upper()
    length = len(temp)
    
    # String ans is created to store the final string.
    ans = ""
    val = k

    # Iterate over the string from right to left and start pushing characters at an interval of K
    for i in range(length - 1,-1,-1):
        if(val == 0):
            val = k
            ans += '-'
        ans += temp[i]
        val -= 1

    # Reverse the final string and return it.
    ans = ans[::-1]
    return ans

# Driver code
if __name__ == "__main__":
    s = "5F3Z-2e-9-w"
    k = 4
    
    # Function call
    print(ReFormatStrings(s,k))
    
    # This code is contributed by ajaymakvana
#Output
#5F3Z-2E9W

#--------------------------------------------------------------------
#Efficient approach: To solve the problem follow the below idea:

#Without creating any other string we will move all the dashes to the front and remove them then we will make use of the mathematical formula to calculate the number of dashes at the right of all the alphanumeric characters.
#Number of Dashes=(Total alphanumeric elements)/(number of elements in every group)
#Formula:

#Number of Dashes at any step = (Total alphanumeric elements to the right of the current index) / (number of elements in every group)

#Follow the steps to solve the problem:

#Iterate from the back of the string and move all the alphanumeric characters to the back of the string.
#Delete all the dashes from the beginning.
#Calculate the number of dashes(rounded-up) that would be present in the final string and append free it to the original string.
#Iterate from the front and depending on the number of dashes that would be present up to that character, move the character by that amount in the left direction. 
#Delete all the extra dashes that would have accumulated in the front of the string
#Return the string after all the modifications as the answer.
#Below is the implementation for the above approach:

# Python3 code for the above approach
# Function to reverse a string
def reverse(string):
    string = string[::-1]
    return string

# Function to compute the answer
def ReFormatString( S, K):
    length = len(S)
    cnt = 0
    x = 0

    # Move the characters to the
    # back of the string.
    for i in range(length-1,-1,-1):
        if (S[i] == '-'):
            x+=1
        else:
            S = S[:i+x] + S[i].upper() + S[i+x+1:]

    # Calculate total number of
    # alphanumeric characters so
    # as to get the number of dashes
    # in the final string.
    slen = length - x
    step = slen / K

    # Remove x characterclss from the
    # start of the string

    S = reverse(S)
    val = x
    while (val>0):
        S = S[:len(S)-1]
        val-=1

    # Push the empty spaces in
    # the string (slen+step) to get
    # the final string length

    temp = step
    while (temp>0):
        S+=' '
        temp-=1
    S = reverse(S)
     
    length = len(S)

    # Using simple mathematics
    # to push the elements
    # in the string at the correct place.

    i = slen
    j = step
    f = 0
    while (j < length):

        # At every step calculate the
        # number of dashes that would be
        # present before the character
        step = int(i / K)
        if (f == 1):
            step-=1
        rem = i % K

        # If the remainder is zero it
        # implies that the character is a dash.
        if (rem == 0 and f == 0):
            step = int(step)
            j = int(j)
            S = S[:int(j-step)] + '-' + S[int(j-step)+1:]
            f = 1
            continue
        S = S[:int(j-step)] + S[int(j)] + S[int(j-step)+1:]
        i -= 1
        j += 1
        f = 0
    # Remove all the dashes that would have
    # accumulated in the beginning of the string.
    length = len(S)
    S = reverse(S)
    for char in reversed(S):
        if (char != '-'):
            break
        if (char == '-'):
            S = S[:len(S)-1]
    S = reverse(S)

    return S

# Driver code
s = "5F3Z-2e-9-w"
K = 4

# Function Call
print(ReFormatString(s, K))

# This code is contributed by akashish__
#Output
#5F3Z-2E9W
#Time Complexity: O(N)
#Auxiliary Space: O(1)