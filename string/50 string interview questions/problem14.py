#Check if a string can be obtained by rotating another string 2 places
#Given two strings, the task is to find if a string can be obtained by rotating another string by two places. 

#Examples: 

#Input: string1 = “amazon”, string2 = “azonam” 
#Output: Yes 
#Explanation: Rotating string1 by 2 places in anti-clockwise gives the string2.

#Input: string1 = “amazon”, string2 = “onamaz” 
#Output: Yes 
#Explanation: Rotating string1 by 2 places in clockwise gives the string2.


#Asked in: Amazon Interview

#Recommended Problem
#----------------------------------------------
#Approach 1 (by Rotating String Clockwise and Anti-clockwise):
#The idea is to Rotate the String1 in both clockwise and ant-clockwise directions. Then if this rotated string is equal to String2.

#Illustration:



#str1 = “amazon”
#str2 = “azonam”

#Initialise: clock_rot = “”, anticlock_rot = “”

#str1 after 2 places clockwise rotation:
#clock_rot = “onamaz”

#str1 after 2 places anti-clockwise rotation:
#anticlock_rot = “azonam”

#Therefore, anticlock_rot and str2 are same.

#Hence, str2 can be achieved from str1

#Follow the steps below to solve the problem:

#Initialize two empty strings which keep the clockwise and anticlockwise strings respectively.
#After rotating the str1 compare both clockwise and anticlockwise strings with str2.
#If any of them matches the str2 return true, otherwise false.
#Below is the implementation of the above approach.


# Python 3 program to check if a string
# is two time rotation of another string.
 
# Function to check if string2 is
# obtained by string 1
def isRotated(str1, str2):
 
    if (len(str1) != len(str2)):
        return False
     
    if(len(str1) < 2):
        return str1 == str2
    clock_rot = ""
    anticlock_rot = ""
    l = len(str2)
 
    # Initialize string as anti-clockwise rotation
    anticlock_rot = (anticlock_rot + str2[l - 2:] +
                                     str2[0: l - 2])
     
    # Initialize string as clock wise rotation
    clock_rot = clock_rot + str2[2:] + str2[0:2]
 
    # check if any of them is equal to string1
    return (str1 == clock_rot or
            str1 == anticlock_rot)
 
# Driver code
if __name__ == "__main__":
     
    str1 = "geeks"
    str2 = "eksge"
if isRotated(str1, str2):
    print("Yes") 
else:
    print("No")
 
# This code is contributed by ita_c
#Output
#Yes
#Time Complexity: O(n), Time is taken to rotate the string and then compare the string.
#Auxiliary Space: O(n), Space for storing clockwise and anticlockwise strings.

#-------------------------------
#Approach 2(Without Using auxiliary space):
#We could check directly if the string is rotated or not by comparing the two strings. 

#Illustration:

#WSteps –

#Check if the string is rotated in clockwise manner.
#Check if the string is rotated in anticlockwise manner. 
#Return true if any one of the above is true
#We compare for clockwise and anticlockwise by using for loops and the modulo operator-

#Note that – 

#For clockwise – str1[i] == str2[(i + 2) % n]

#For anticlockwise – str1[(i + 2) % n] == str2[i]

#Here n is length of string 

#Check using the above two conditions and the problem will be solved!

#Below is the implementation of the above approach:


#// C++ code to find if string is rotated by 2 positions
 
#include <iostream>
using namespace std;
 
bool isRotated(string str1, string str2)
{
    // Your code here
    // clockwise direction check
    int n = str1.length();
    bool clockwise = true, anticlockwise = true;
    for (int i = 0; i < n; i++)
    {
        if (str1[i] != str2[(i + 2) % n])
        {
            clockwise = false; // not rotated clockwise
            break;
        }
    }
 
    for (int i = 0; i < n; i++)
    {
        if (str1[(i + 2) % n] != str2[i])
        {
            anticlockwise = false; // not rotated anticlockwise
            break;
        }
    }
 
    return clockwise or anticlockwise; // if any of both is true, return true
}
int main()
{
    string str1 = "geeks";
    string str2 = "eksge";
 
    isRotated(str1, str2) ? cout << "Yes"
                          : cout << "No";
    return 0;
}
 
#//code contributed by Anshit Bansal
#Output
#Yes
