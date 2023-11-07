#python program to convert  set into tuple into set



#Let’s see how to convert the set into tuple and tuple into the set. For performing the task we are use some methods like tuple(), set(), type().

#tuple(): tuple method is used to convert into a tuple. This method accepts other type values as an argument and returns a tuple type value.
#set(): set method is to convert other type values to set this method is also accepted other type values as an argument and return a set type value.
#type(): type method helps the programmer to check the data type of value. This method accepts a value as an argument and it returns type of the value.

#   program to convert set to tuple
# create set
s = {'a', 'b', 'c', 'd', 'e'}
 
# print set
print(type(s), " ", s)
 
# call tuple() method
# this method convert set to tuple
t = tuple(s)
 
# print tuple
print(type(t), " ", t)






#Method2: Using list comprehension

s = {'a', 'b', 'c', 'd', 'e'}
x=[i for i in s]
print(tuple(x))


#Method3: Using enumerate function
s = {'a', 'b', 'c', 'd', 'e'}
x=[i for a,i in enumerate(s)]
print(tuple(x))


#Example 2: tuple into the set.
#program to convert tuple into set
 
# create tuple
t = ('x', 'y', 'z')
 
# print tuple
print(type(t), "  ", t)
 
# call set() method
s = set(t)
 
# print set
print(type(s), "  ", s)


