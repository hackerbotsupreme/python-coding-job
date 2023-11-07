#python program to convert  a set to string .

#Syntax : str(object, encoding = ’utf-8?, errors = ’strict’)

#Parameters :


#object : The object whose string representation is to be returned.
#encoding : Encoding of the given object.
#errors : Response when decoding fails.
#Returns : String version of the given object


#we will discuss how to convert a set to a string in Python. It can done using two ways –

#Method 1: Using str()
#We will convert a Set into a String in Python using the str() function.
s = {'a', 'b', 'c', 'd'}
print("Initially")
print("The datatype of s : " + str(type(s)))
print("Contents of s : ", s)
  
# convert Set to String
s = str(s)
print("\nAfter the conversion")
print("The datatype of s : " + str(type(s)))
print("Contents of s : " + s)




#Example 2 :

# create a set
s = {'g', 'e', 'e', 'k', 's'}
print("Initially")
print("The datatype of s : " + str(type(s)))
print("Contents of s : ", s)
  
# convert Set to String
s = str(s)
print("\nAfter the conversion")
print("The datatype of s : " + str(type(s)))
print("Contents of s : " + s)




#Method 2: Using Join()

#The join() method is a string method and returns a string in which the elements of sequence have been joined by str separator.

#Syntax:

#string_name.join(iterable) 
# create a set
s = {'a', 'b', 'c', 'd'}
print("Initially")
print("The datatype of s : " + str(type(s)))
print("Contents of s : ", s)
   
# convert Set to String
S = ', '.join(s)
print("The datatype of s : " + str(type(S)))
print("Contents of s : ", S)