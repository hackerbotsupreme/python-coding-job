#python program to convert set into list.

#Approach #1 : Using list(set_name). Typecasting to list can be done by simply using list(set_name). 
# Python3 program to convert a
# set into a list
my_set = {'Geeks', 'for', 'geeks'}
 
s = list(my_set)
print(s)



# Python3 program to convert a
# set into a list
def convert(set):
    return list(set)
 
# Driver function
s = set({1, 2, 3})
print(convert(s))




#Approach #2 : using sorted() method Using sorted() 
# function will convert the set into list in a defined 
# order. The only drawback of this method is that the
# elements of the set need to be sortable. 


# Python3 program to convert a
# set into a list
def convert(set):
    return sorted(set)
 
# Driver function
my_set = {1, 2, 3}
 
s = set(my_set)
print(convert(s))





#Approach #3 : Using [*set, ] This essentially unpacks
# the set s inside a list literal which is created due to 
# the presence of the single comma (, ). This approach is
# a bit faster but suffers from readability. 



# Python3 program to convert a
# set into a list
def convert(set):
    return [*set, ]
 
# Driver function
s = set({1, 2, 3})
print(convert(s))



 #Approach #4 : Using the map() function: You can 
 # use the map() function to convert the set to a list 
 # by passing the set as an argument to the map() function
 # and returning a list of the results. For example:

 
# Python3 program to convert a
# set into a list
def convert(s):
    return list(map(lambda x: x, s))
# Driver function
s = {1, 2, 3}
print(convert(s))



#Approach #5: Using the list comprehension: You can use a list comprehension to create a new list from the elements in the set.

def convert(s):
    # Use a list comprehension to create a new list from the elements in the set
    return [elem for elem in s]
 
s = {1, 2, 3}
print(convert(s))


