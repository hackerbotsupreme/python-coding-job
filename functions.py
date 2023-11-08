#the syntax  of a func
#the syntax of  a function looks as follows
#(defining / staring /telling computer i am starting a function)def  func1(function name)(variable):
#                                                               print("hello") 
#this function can be called any number of times ,anywhere inthe  program .
#to  call the function --- name( variable )
#
def greet(name):
    print("good day,master"+ name)
greet("aloke")
# the return is---good day,masteraloke


#there are two types of functions that are 
#1.built-in function :already present in python examples are--len(), print(),range()
#2.user-defined function   :defined by user


#in  the above example we seen functions takes /acceptss values with which it can perform tasks 
#and the values are entered by us and after his task it returns a value too.
#so here the values we give to a function is called arguments 
#i am repeating that a function  can have  one/multiple    line/set of command/instruction 
#and ends at return statements
#as an exampole
def greet(name):
    gret="greet"+name    #the argument here which is name is passed tofunctions secnnd line
    return gret
a=greet("aloke")




