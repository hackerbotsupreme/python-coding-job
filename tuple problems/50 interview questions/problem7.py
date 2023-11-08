#Python | Remove empty tuples from a list

#Difficulty Level : Easy

#In this article, we will see how can we remove an empty tuple from a given list of tuples. We will find various ways, in which we can perform this task of removing tuples using various methods and ways in Python. 

#Examples:

#Input : tuples = [(), (‘ram’,’15’,’8′), (), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”,”),()]
#Output : [(‘ram’, ’15’, ‘8’), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”, ”)]

#Input : tuples = [(”,”,’8′), (), (‘0′, ’00’, ‘000’), (‘birbal’, ”, ’45’), (”), (),  (”,”),()]
#Output : [(”, ”, ‘8’), (‘0′, ’00’, ‘000’), (‘birbal’, ”, ’45’), (”, ”)]


#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#Method 1: Using the concept of List Comprehension 

#Python3
# Python program to remove empty tuples from a
# list of tuples function to remove empty tuples
# using list comprehension
def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples
 
# Driver Code
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]
print(Remove(tuples))
#Output
[('ram', '15', '8'), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('', '')]
#Method 2: Using the filter() method 

#Using the inbuilt method filter() in Python, we can filter out the empty elements by passing the None as the parameter. This method works in both Python 2 and Python 3 and above, but the desired output is only shown in Python 2 because Python 3 returns a generator. filter() is faster than the method of list comprehension. Let’s see what happens when we run the program in Python 2. 

#Python
# Python2 program to remove empty tuples
# from a list of tuples function to remove
# empty tuples using filter
def Remove(tuples):
    tuples = filter(None, tuples)
    return tuples
 
# Driver Code
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]
#print Remove(tuples)
#Output
#[('ram', '15', '8'), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('', '')]
#Now let’s see what happens when we try running the program in Python 3 and above. On running the program in Python 3, as mentioned a generator is returned. 

#Python3
# Python program to remove empty tuples from
# a list of tuples function to remove empty
# tuples using filter
 
 
def Remove(tuples):
    tuples = filter(None, tuples)
    return tuples
 
 
# Driver Code
tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('', ''), ()]
print(Remove(tuples))
#Output
#<filter object at 0x7fae9a596e90>
#Method #3 : Using len() method

#Python3
# Python program to remove empty tuples from a
# list of tuples function to remove empty tuples
# using len()
 
 
def Remove(tuples):
    for i in tuples:
        if(len(i) == 0):
            tuples.remove(i)
    return tuples
 
 
# Driver Code
tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('', ''), ()]
print(Remove(tuples))
#Output

[('ram', '15', '8'), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('', '')]
#Method #4 : Using == operator.Check whether the tuple is equal to empty tuple() and remove if equals.

#Python3
# Python program to remove empty tuples from a
# list of tuples function to remove empty tuples
def Remove(tuples):
    for i in tuples:
        if(i==()):
            tuples.remove(i)
    return tuples
# Driver Code
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
        ('krishna', 'akbar', '45'), ('',''),()]
print(Remove(tuples))
#Output
#[('ram', '15', '8'), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('', '')]
Method: Using enumerate function
#Python3
tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('', ''), ()]
res = [t for i, t in enumerate(tuples) if t]
print(res)
#Output
[('ram', '15', '8'), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('', '')]
#Time Complexity: O(n)
#Auxiliary Space: O(1)

#Method: Using while and in operator
#Python
# Python program to remove empty tuples from
# a list of tuples function to remove empty
# tuples using while loop and in operator  
def Remove(tuples):
    while () in tuples:
        tuples.remove(());
    return tuples
 
# Driver Code
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
        ('krishna', 'akbar', '45'), ('',''),()]
print (Remove(tuples))
#Output
[('ram', '15', '8'), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('', '')]
#Method : Using str(), len() and find() method
#Python3
# Python program to remove empty tuples from a
# list of tuples function to remove empty tuples
 
 
def Remove(tuples):
    for i in tuples:
        if(str(i).find("()") != -1 and len(str(i)) == 2):
            tuples.remove(i)
    return tuples
 
 
# Driver Code
tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('', ''), ()]
print(Remove(tuples))
#Output
[('ram', '15', '8'), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('', '')]
Method: Using lambda functions

#Python3
# Python program to remove empty tuples from
# a list of tuples function to remove empty
# tuples using lambda function
 
 
# Driver Code
tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('', ''), ()]
 
tuples = list(filter(lambda x: len(x) > 0, tuples))
print(tuples)
#Output
[('ram', '15', '8'), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('', '')]
#Method : Using  list comprehension , len() method:

#Python3
def remove_empty_tuples(tuples):
    return [t for t in tuples if len(t) > 0]
 
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]
print(remove_empty_tuples(tuples))
#This code is contributed by Edula Vinay Kumar Reddy
#Output
[('ram', '15', '8'), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('', '')]
#This method uses a list comprehension to iterate over the list of tuples and check the length of each tuple. If the length is greater than 0, it is included in the new list.

#Time complexity: O(n)
#Auxiliary Space: O(n)

#Method: Using Recursion method 

#Python3
#defining recursive function to remove empty tuples in a list
def remove_empty_tuples(start,oldlist,newlist):
  if start==len(oldlist):  #base condition
    return newlist
  if oldlist[start]==():  #checking the element is empty tuple or not
    pass
  else:
    newlist.append(oldlist[start])   #appending non empty tuple element to newlist
  return remove_empty_tuples(start+1,oldlist,newlist)  #recursive function call
 
 
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]
#print('The original list: ',tuples)
print(remove_empty_tuples(0,tuples,[]))
#This code is contributed by tvsk
#Output
#[('ram', '15', '8'), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('', '')]
#Time complexity: O(n)
#Auxiliary Space: O(n)