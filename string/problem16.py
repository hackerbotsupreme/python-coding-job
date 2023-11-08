#Program to validate an IP address
#Write a program to Validate an IPv4 Address. 
#According to Wikipedia, IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots, e.g., 172.16.254.1


-----------------------------------------------------
#Following are steps to check whether a given string is a valid IPv4 address or not:

#step 1) Parse string with “.” as delimiter using “strtok()” function. 

#e.g.ptr = strtok(str, DELIM);


#step 2) 
#A) If ptr contains any character which is not digit then return 0 
#B) Convert “ptr” to decimal number say ‘NUM’ 
#C) If NUM is not in range of 0-255 return 0 
#D) If NUM is in range of 0-255 and ptr is non-NULL increment “dot_counter” by 1 
#E) if ptr is NULL goto step 3 else goto step 1
#step 3) if dot_counter != 3 return 0 else return 1


#// Program to check if a given
#// string is valid IPv4 address or not
#include <bits/stdc++.h>
#using namespace std;
#define DELIM "."
 
#/* function to check whether the
#   string passed is valid or not */
#bool valid_part(char* s)
{
    int n = strlen(s);
     
    // if length of passed string is
    // more than 3 then it is not valid
    if (n > 3)
        return false;
     
    // check if the string only contains digits
    // if not then return false
    for (int i = 0; i < n; i++)
        if ((s[i] >= '0' && s[i] <= '9') == false)
            return false;
    string str(s);
     
    // if the string is "00" or "001" or
    // "05" etc then it is not valid
    if (str.find('0') == 0 && n > 1)
        return false;
    stringstream geek(str);
    int x;
    geek >> x;
     
    // the string is valid if the number
    // generated is between 0 to 255
    return (x >= 0 && x <= 255);
}
 
/* return 1 if IP string is
valid, else return 0 */
int is_valid_ip(char* ip_str)
{
    // if empty string then return false
    if (ip_str == NULL)
        return 0;
    int i, num, dots = 0;
    int len = strlen(ip_str);
    int count = 0;
     
    // the number dots in the original
    // string should be 3
    // for it to be valid
    for (int i = 0; i < len; i++)
        if (ip_str[i] == '.')
            count++;
    if (count != 3)
        return false;
     
    // See following link for strtok()
   
    char *ptr = strtok(ip_str, DELIM);
    if (ptr == NULL)
        return 0;
 
    while (ptr) {
 
        /* after parsing string, it must be valid */
        if (valid_part(ptr))
        {
            /* parse remaining string */
            ptr = strtok(NULL, ".");
            if (ptr != NULL)
                ++dots;
        }
        else
            return 0;
    }
 
    /* valid IP string must contain 3 dots */
    // this is for the cases such as 1...1 where
    // originally the no. of dots is three but
    // after iteration of the string we find
    // it is not valid
    if (dots != 3)
        return 0;
    return 1;
}
 
// Driver code
int main()
{
    char ip1[] = "128.0.0.1";
    char ip2[] = "125.16.100.1";
    char ip3[] = "125.512.100.1";
    char ip4[] = "125.512.100.abc";
    is_valid_ip(ip1) ? cout<<"Valid\n" : cout<<"Not valid\n";
    is_valid_ip(ip2) ? cout<<"Valid\n" : cout<<"Not valid\n";
    is_valid_ip(ip3) ? cout<<"Valid\n" : cout<<"Not valid\n";
    is_valid_ip(ip4) ? cout<<"Valid\n" : cout<<"Not valid\n";
    return 0;
}
#Output
#Valid
#Valid
#Not valid
#Not valid
#Time complexity : O(n) 
#Auxiliary Space : O(1)
---------------------------------------------------------------------

#Python Solution :-

#Approach:- We will check all the cases where ip address may be invalid

#1. First we will split the given input  using split() function then check if it has a length of 4  or not .If length  is not equal to 4 then we will directly return 0.

#2. in second step we will check if any split element contains any leading zero or not .if it is then we will return zero.

#3.If any of the split does not contain any number then it is not a valid ip address .so we will return 0

#4. Then we will check if all the splits are in the range of  0-255 or not .If not we will return 0.

#5.Finally if none of the above condition is true we can finally say that it is a valid ip address.And we will return True.

#Here is the code for above approach .


def in_range(n):   #check if every split is in range 0-255
    if n >= 0 and n<=255:
        return True
    return False
     
def has_leading_zero(n): # check if every split has leading zero or not.
    if len(n)>1:
        if n[0] == "0":
            return True
    return False
def isValid(s):
     
    s = s.split(".")
    if len(s) != 4:  #if number of splitting element is not 4 it is not a valid ip address
        return 0
    for n in s:
         
        if has_leading_zero(n):
            return 0
        if len(n) == 0:
            return 0
        try:  #if int(n) is not an integer it raises an error
            n = int(n)
 
            if not in_range(n):
                return 0
        except:
            return 0
    return 1
         
   
if __name__=="__main__":
     
     
    ip1 = "222.111.111.111"
    ip2 = "5555..555"
    ip3 = "0000.0000.0000.0000"
    ip4 = "1.1.1.1"
    print(isValid(ip1))
    print(isValid(ip2))
    print(isValid(ip3))
    print(isValid(ip4))
 
     
 # this code is contributed by Vivek Maddeshiya.
#Output
1
0
0
1
#Time complexity : O(n) 
#Auxiliary Space : O(1)
