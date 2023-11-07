#python program to find missing keys in python dictionaries.

#In python, dictionaries are containers that map one key to its value with access time complexity to be O(1). But in many applications, the user doesn’t know all the keys present in the dictionaries. In such instances, if the user tries to access a missing key, an error is popped indicating missing keys. 
 


# Python code to demonstrate Dictionary and


# Python code to demonstrate Dictionary and
# missing value error

# initializing Dictionary
d = { 'a' : 1 , 'b' : 2 }

# trying to output value of absent key
print ("The value associated with 'c' is : ")
print (d['c'])

#Error : 
 

#Traceback (most recent call last):
#  File "46a9aac96614587f5b794e451a8f4f5f.py", line 9, in 
#    print (d['c'])
#KeyError: 'c'
#In the above example, no key named ‘c’ in the dictionary popped a runtime error. To avoid such conditions, and to make the aware user that a particular key is absent or to pop a default message in that place, there are several methods to handle missing keys.

#Method 1 : Using get()
#get(key,def_val) method is useful when we have to check for the key. If the key is present, the value associated with the key is printed, else the def_value passed in arguments is returned.
 

country_code = {'India' : '0091',
				'Australia' : '0025',
				'Nepal' : '00977'}

# search dictionary for country code of India
print(country_code.get('India', 'Not Found'))

# search dictionary for country code of Japan
print(country_code.get('Japan', 'Not Found'))



#Output: 

#0091
#Not Found
#Method 2 : Using setdefault()
#setdefault(key, def_value) works in a similar way as to get(), but the difference is that each time a key is absent, a new key is created with the def_value associated with the key passed in arguments.


country_code = {'India' : '0091',
				'Australia' : '0025',
				'Nepal' : '00977'}

# Set a default value for Japan
country_code.setdefault('Japan', 'Not Present')

# search dictionary for country code of India
print(country_code['India'])

# search dictionary for country code of Japan
print(country_code['Japan'])


#Method 3: Using defaultdict
#“defaultdict” is a container that is defined in a module named “collections“. It takes a function(default factory) as its argument. By default, the default factory is set to “int” i.e 0. If a key is not present in the defaultdict, the default factory value is returned and displayed. It has advantages over get() or setdefault(). 
 

#A default value is set at the declaration. There is no need to invoke the function again and again and pass the similar values as arguments. Hence saving time.
#The implementation of defaultdict is faster than get() or setdefault(). 
 
# Example:

# Python code to demonstrate defaultdict

# importing "collections" for defaultdict
import collections

# declaring defaultdict
# sets default value 'Key Not found' to absent keys
defd = collections.defaultdict(lambda : 'Key Not found')

# initializing values
defd['a'] = 1

# initializing values
defd['b'] = 2

# printing value
print ("The value associated with 'a' is : ",end="")
print (defd['a'])

# printing value associated with 'c'
print ("The value associated with 'c' is : ",end="")
print (defd['c'])

#Output : 
 

#The value associated with 'a' is : 1
#The value associated with 'c' is : Key Not found










