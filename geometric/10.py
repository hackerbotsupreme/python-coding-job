Code to Generate the Map of India (With Explanation)

Difficulty Level : Expert
Last Updated : 22 May, 2022
Read
Discuss
Courses
Practice
Video
Given an obfuscated code that generates the map of India, explain its working. The following code when executed generates the map of India.

#include "stdio.h"

int main()

ding Posts

int a, b, c;

for (b-c-18; a="Hello! Welcome to Geeks ForGeeks.\

TFy!QJu ROo TNn (ROO) SLq SLq ULO+

UHS UJq TNn*RPn/QPbEWS_JSWQAIJO^\

NBELPEHBFHT}TnALVIBLOFAKHFOUFETp\

HCSTHAUFAgcEAelclcn^r^r\\tZvYXXy\

T|S~Pn SPM SOn TNn ULOGULO#ULO-W\

er menu

et

Hq!WFs XDt!" [b+++21]; )

ents 850

dot menu

gs

for (; a-- &gt; 64; )

putchar (++C == 'Z' ? c = c/ 9:33^b&amp;1);

ar Ads Widget

ub menu

et

return 0;

se menu

}
The above code is a typical example of obfuscated code i.e. code that is difficult for humans to understand.

How does it work?
Basically, the string is a run-length encoding of the map of India. Alternating characters in the string store how many times to draw space, and how many times to draw an exclamation mark consecutively. Here is an analysis of the different elements of this program –

The encoded string

"Hello!Welcome to GeeksForGeeks."
"TFy!QJu ROo TNn(ROo)SLq SLq ULo+UHs UJq TNn*RPn/QPbEWS_JSWQAIJO^NBELPeHBFHT}TnALVlBL"
"OFAkHFOuFETpHCStHAUFAgcEAelclcn^r^r\\tZvYxXyT|S~Pn SPm SOn TNn ULo0ULo#ULo-WHq!WFs XDt!";
Notice [b+++21] at the end of the encoded string. As b+++21 is equivalent to (b++ + 21) which will evaluate to 31 (10 + 21), the first 31 characters of this string are ignored and do not contribute to anything. The remaining encoded string contains instructions for drawing the map. The individual characters determine how many spaces or exclamation marks to draw consecutively.

Outer for loop: This loop goes over the characters in the string. Each iteration increases the value of b by one and assigns the next character in the string to a.
Inner for loop: This loop draws individual characters, and a new line whenever it reaches the end of the line. Consider this putchar statement 

putchar(++c=='Z' ? c = c/9 : 33^b&1);
As ‘Z’ represents the number 90 in ASCII, 90/9 will give us 10 which is a newline character. Decimal 33 is ASCII for ‘!’. Toggling the low-order bit of 33 gives you 32, which is ASCII for a space. This causes! to be printed if b is odd, and a blank space to be printed if b is even. 

Below is a less obfuscated version of the above code:

C++
C
Java
Python3
# Python3 program to print map of India
a = 10
b = 0
c = 10
 
# The encoded string after removing first
# 31 characters. Its individual characters
# determine how many spaces or exclamation
# marks to draw consecutively.
s = ("TFy!QJu ROo TNn(ROo)SLq SLq ULo+UHs"
     " UJq TNn*RPn/QPbEWS_JSWQAIJO^NBELPe"
     "HBFHT}TnALVlBLOFAkHFOuFETpHCStHAUFA"
     "gcEAelclcn^r^r\\tZvYxXyT|S~Pn SPm S"
     "On TNn ULo0ULo#ULo-WHq!WFs XDt!")
 
# Read each character of encoded string
a = ord(s[b])
 
while a != 0:
    if b < 170:
        a = ord(s[b])
        b += 1
         
        while a > 64:
            a -= 1
            c += 1
             
            if c == 90:
                c = c // 9
                print(end = chr(c))
            else:
                print(chr(33 ^ (b & 0X01)), end = '')
    else:
        break
 
# The code is contributed by aayush_chouhan
C#
PHP
Output: 

Console printing India's Map

This article is contributed by Aditya Goel. If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks. Please write comments if you find anything incorrect, or if you want to share more information about the topic discussed above.



Like
Previous
kbhit in C language
Next
Operators in C
Related Articles
1.
Searching in a map using std::map functions in C++
2.
map::at() and map::swap() in C++ STL
3.
How to create the boilerplate code in VS Code?
4.
Descending Order in Map and Multimap of C++ STL
5.
Inserting elements in std::map (insert, emplace and operator [])
6.
Different ways to delete elements in std::map (erase() and clear())
7.
Map of pairs in STL
8.
Traversing a map (or unordered_map) in C++ STL
9.
Operator overloading in C++ to print contents of vector, map, pair, ..
10.
Check if a key is present in a C++ map or unordered_map
Article Contributed By :
https://media.geeksforgeeks.org/auth/avatar.png
GeeksforGeeks
Vote for difficulty
Current difficulty : Expert
Easy
Normal
Medium
Hard
Expert
Improved By :
Mithun Kumar
aayush009
SHUBHAMSINGH10
jeevanyasa
sackshamsharmaintern
Article Tags :
computer-graphics
pattern-printing
C Language
C++
Practice Tags :
CPP
pattern-printing
Report Issue