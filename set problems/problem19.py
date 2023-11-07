# python program convert set to dictionary


#Sometimes we need to convert one data structure into another for various operations and problems in our day to day coding and web development. Like we may want to get a dictionary from the given set elements.
#Let’s discuss a few methods to convert given set into a dictionary.

#Method #1: Using fromkeys() 

# Python code to demonstrate


# Python code to demonstrate
# converting set into dictionary
# using fromkeys()
 
# initializing set
ini_set = {1, 2, 3, 4, 5}
 
# printing initialized set
print ("initial string", ini_set)
print (type(ini_set))
 
# Converting set to dictionary
res = dict.fromkeys(ini_set, 0)
 
# printing final result and its type
print ("final list", res)
print (type(res))



#Method #2: Using dict comprehension 



# Python code to demonstrate
# converting set into dictionary
# using dict comprehension
 
 
# initializing set
ini_set = {1, 2, 3, 4, 5}
 
# printing initialized set
print ("initial string", ini_set)
print (type(ini_set))
 
str = 'fg'
# Converting set to dict
res = {element:'Geek'+str for element in ini_set}
 
# printing final result and its type
print ("final list", res)
print (type(res))




