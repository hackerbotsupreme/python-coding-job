#string is a data type in python which is nothing but a sequence of charecters 
#string is represented using 3 type of quotes.
#that are single , double,and triple quote 
#triple quote is used when we need to write more than  one line 
#string slicing that main concept of slicing starts with that strings are stored through indexing means 
#aloke
#01234- the indexing starts from the left and from 0  and vice versa like (-5)(-4)(-3)(-2)(-1) . we slice strings to use a part of them .
name="aloke"   # in order to slice the string
print(name[-3:-1])# (-3) to (-1)->very imp :start- index always start ffrom  the left and the item of end-index will not be printed so the 
               #print(name[-1:-3])---is not valid bcz stat-index is not starting from the left for name =a(-5)l(-4)o(-3)k(-2)e(-1)
print(name[0])
               #notice that the format is --------name[index of the digit ]---------
print(name[2])
print(name[0:3])
print(name[:3])#is same as [0:3] , 0123 - four index- printed 012- end index will not print so then how we will print the item of the last index well that is why the negative 
               #numbering is used but also the indexing  starts from the left in this case too
print(name[3:])#is same as [3:5] and as always indexing starts from the left and the end-index will not print.
               #that's how we slice a string ,syntax-name[start-index:end-index] if start inndex is missing the program will assume start-index to be 0.

               #lets try to change the item in index 2 
name[3]=5
               # error:'str' object does not support item assignment means we can not change items in string 


#concatinating two strings 
#greet the user using concatination 
greeting="good  morning"
name="aloke"
c=greeting+name
print(c)




