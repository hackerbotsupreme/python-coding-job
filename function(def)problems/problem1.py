#python program  to  print multiple arguments in python



#An argument is a value that is passed within a function when it is called.They are independent items, or variables, that contain data or codes. During the time of call each argument is always assigned to the parameter in the function definition.
def GFG(name, num):
	print("Hello from ", name + ', ' + num)


GFG("geeks for geeks", "25")

#Calling the above code with no arguments or just one argument generates an error.





#Variable Function Arguments
#As shown above, functions had a fixed number of arguments. In Python, there are other ways to define a function that can take the variable number of arguments.
#Different forms are discussed below:

#Python Default Arguments: Function arguments can have default values in Python. We provide a default value to an argument by using the assignment operator (=).

def GFG(name, num="25"):
	print("Hello from", name + ', ' + num)


GFG("gfg")
GFG("gfg", "26")
#Output:

#Hello from gfg, 25

#Hello from gfg, 26

#Pass it as a tuple
def GFG(name, num):
	print("hello from %s , %s" % (name, num))


GFG("gfg", "25")

#Output:

#hello from gfg , 25

#Pass it as a dictionary

def GFG(name, num):
	print("hello from %(n)s , %(s)s" % {'n': name, 's': num})


GFG("gfg", "25")


#back to it later
