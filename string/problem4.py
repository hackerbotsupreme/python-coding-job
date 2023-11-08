#find length of a string in python


#note: strings in python are immutable.immutable means uniqueness that cannot be
# changed like you cannot interchange interchange iems,you can not remove or place anothe item by removing an item. 

#as always we will look for the in built functions that can make our joobs easy
#in this case it is len(str)  
#attempt 1
str="aloke"
print(len(str))

#lenth finding
#we can do this using loops and in operator
def findlen(str):
    counter=0
    for i in str:
        counter+=1
    return counter
str="aloke"
print(findlen(str))

#length finding
# we can do using while and slicing
def findlen(str):
    counter=0
    while str[counter:]:
        counter+=1
    return counter
str="aloke"
print(findlen(str))


#length finding
#using join and count
def findlen(str):
    if not str:
        return 0
    else :
        some_random_str='py'
    return((some_random_str).join(str).count(some_random_str)+1)
str="aloke"
print(findlen(str))
#what is .reduce() method?
#reduce(function, iterable[, initial]) -> value

#Apply a function of two arguments cumulatively to the items of a sequence or iterable, from left to right, so as to reduce the iterable to a single
#value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). If initial is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty.


#lenngth finding 
#reduce method

import functools
def findlen(str):
    return functools.reduce(lambda x,y:x+1,string,0)
string="geeks"
print(findlen(str))


#length finding
#length is a number right so  we can think like length is either a addition of numbers or total count of numbers 
##for addition case we do something like sum method 
#using sum()method

def findlen(string):
    return sum(i for i in string )
string='geeks'
print(findlen(string))











