#Program to generate all possible valid IP addresses from given string

#Difficulty Level : Hard
#Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#A valid IP address must be in the form of A.B.C.D, where A, B, C, and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

#Examples :

#Input: 25525511135
#Output: [“255.255.11.135”, “255.255.111.35”]
#Explanation:
#These are the only valid possible
#IP addresses.

#Input: "25505011535"
#Output: []
#Explanation: 
#We cannot generate a valid IP
#address with this string.
#First, we will place 3 dots in the given string and then try out all the possible combinations for the 3 dots. 
#Corner case for validity:

#For string "25011255255"
#25.011.255.255 is not valid as 011 is not valid.
#25.11.255.255 is not valid either as you are not
#allowed to change the string.
#250.11.255.255 is valid.


Approach: Split the string with ‘ . ‘ and then check for all corner cases. Before entering the loop, check the size of the string. Generate all the possible combinations using looping through the string. If IP is found to be valid then return the IP address, else simply return the empty list.
Below is the implementation of the above approach:

Implementation:

C++
Java
Python3
# Python3 code to check valid possible IP
 
# Function checks whether IP digits
# are valid or not.
def is_valid(ip):
 
    # Splitting by "."
    ip = ip.split(".")
     
    # Checking for the corner cases
    for i in ip:
        if (len(i) > 3 or int(i) < 0 or
                          int(i) > 255):
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if (len(i) > 1 and int(i) != 0 and
            i[0] == '0'):
            return False
             
    return True
 
# Function converts string to IP address
def convert(s):
     
    sz = len(s)
 
    # Check for string size
    if sz > 12:
        return []
    snew = s
    l = []
 
    # Generating different combinations.
    for i in range(1, sz - 2):
        for j in range(i + 1, sz - 1):
            for k in range(j + 1, sz):
                snew = snew[:k] + "." + snew[k:]
                snew = snew[:j] + "." + snew[j:]
                snew = snew[:i] + "." + snew[i:]
                 
                # Check for the validity of combination
                if is_valid(snew):
                    l.append(snew)
                     
                snew = s
                 
    return l
 
# Driver code        
A = "25525511135"
B = "25505011535"
 
print(convert(A))
print(convert(B))

#Output
#255.255.11.135
#255.255.111.35
#Complexity Analysis:



#Time Complexity: O(n^3), where n is the length of the string 
#Three nested traversal of the string is needed, where n is always less than 12.
#Auxiliary Space: O(n). 
#As extra space is needed.
#Another Efficient Approach (Dynamic Programming): There is a dp approach exist for this problem and can be solved in time complexity O(n*4*3)=O(12n)=O(n) and space complexity O(4n). 

#Approach: We know that there are only 4 parts of the IP. We start iterating from the end of string and goes to the start of string. We create a dp 2D-array of size (4 x N). There can be only 2 values in the dp array i.e. 1(true) or 0(false). dp[0][i] tells if we can create 1 part of IP from the substring starting from i to end of string. Similarly, dp[1][i] tells if we can create 2 parts of IP from the substring starting from i to end of string.

#After creating the dp array, we start creating the valid IP addresses. We start from the bottom left corner of the 2D dp array. We only iterate 12 times(worst case) but those also will be the valid IP addresses because we only form valid IP addresses. 

#Implementation:

#Java
#// Java Program to generate all possible
#// valid IP addresses from given string
import java.util.*;
 
class GFG
{
    public static ArrayList<String> list;
     
    // Function to restore Ip Addresses
    public static ArrayList<String>
    restoreIpAddresses(String s)
    {
        int n = s.length();
        list = new ArrayList<>();
        if (n < 4 || n > 12)
            return list;
       
         // initialize the dp array
        int dp[][] = new int[4][n];
        for (int i = 0; i < 4; i++)
        {
            for (int j = n - 1; j >= 0; j--)
            {
                if (i == 0)
                {
                    // take the substring
                    String sub = s.substring(j);
                    if (isValid(sub))
                    {
                        dp[i][j] = 1;
                    }
                    else if (j < n - 3)
                    {
                        break;
                    }
                }
                else
                {
                    if (j <= n - i)
                    {
                        for (int k = 1;
                             k <= 3 && j + k <= n;
                             k++)
                        {
                            String temp
                                = s.substring(j, j + k);
                            if (isValid(temp))
                            {
                                if (j + k < n
                                    && dp[i - 1][j + k]
                                           == 1)
                                {
                                    dp[i][j] = 1;
                                    break;
                                }
                            }
                        }
                    }
                }
            }
        }
         
        if (dp[3][0] == 0)
            return list;
       
       
        // Call function createIpfromDp
        createIpFromDp(dp, 3, 0, s, "");
        return list;
    }
   
    public static void createIpFromDp(int dp[][],
                                      int r,
                                      int c, String s,
                                      String ans)
    {
        if (r == 0)
        {
            ans += s.substring(c);
            list.add(ans);
            return;
        }
        for (int i = 1;
             i <= 3 && c + i < s.length();
             i++)
        {
            if (isValid(s.substring(c, c + i))
                && dp[r - 1] == 1)
            {
                createIpFromDp(dp, r - 1, c + i, s,
                               ans +
                               s.substring(c, c + i)
                               + ".");
            }
        }
    }
   
   
    private static boolean isValid(String ip)
    {
        String a[] = ip.split("[.]");
        for (String s : a)
        {
            int i = Integer.parseInt(s);
            if (s.length() > 3 || i < 0 || i > 255)
            {
                return false;
            }
            if (s.length() > 1 && i == 0)
                return false;
            if (s.length() > 1 && i != 0
                && s.charAt(0) == '0')
                return false;
        }
 
        return true;
    }
 
    // Driver Code
    public static void main(String[] args)
    {
        // Function call
        System.out.println(
            restoreIpAddresses("25525511135").toString());
    }
}
 
#// This code is contributed by Nidhi Hooda.
#C#
#Output
#[255.255.11.135, 255.255.111.35]
#Complexity Analysis:

#Time Complexity: O(n), where n is the length of the string. The dp array creation would take O(4*n*3) = O(12n) = O(n). Valid IP creation from dp array would take O(n).
#Auxiliary Space: O(n). As dp array has extra space of size (4 x n). It means O(4n).
#Another Approach: (Using Recursion)

#Implementation:

#C++
#Java
#Python3
# Python code for the above approach
def solve(s, i, j, level, temp, res):
 
    if (i == (j + 1) and level == 5):
        res.append(temp[1:])
 
    # Digits of a number ranging 0-255 can lie only between
    # 0-3
    k = i
    while(k < i + 3 and k <= j):
         
        ad = s[i: k + 1]
 
        # Return if string starting with '0' or it is
        # greater than 255.
        if ((s[i] == '0' and len(ad) > 1) or int(ad) > 255):
            return
 
        # Recursively call for another level.
        solve(s, k + 1, j, level + 1, temp + '.' + ad, res)   
 
        k += 1
 
# driver code
s = "25525511135"
n = len(s)
ans = []
solve(s, 0, n - 1, 1, "", ans)
for s in ans:
    print(s)
 
# This code is contributed by shinjanpatra
#Javascript
#Output
#255.255.11.135s
#255.255.111.35

