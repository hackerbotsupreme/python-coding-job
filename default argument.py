#default argument is a value which will be printen when the function will be called he ther will be no value 
# which is given by the user 
def greet(name="aloke"):
    return ("good morning master"+ name)
print (greet())# in this case the default value is passed down to the name
print (greet("subham"))#in this case as user provided the agument so the default value is ignored 

