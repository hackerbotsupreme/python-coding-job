__name__="__main__"
#lets assume we are  delveloping script which is designed to be  used as a module :
#difference between script and module : a script is generally a directly executable piece of  code, run by itself. a module  is generally a library ,imported by othert pieces of code.
#note that there's no internal ditinction -- both are executable and importable . although library code often wont do anything when executed directly.  
def my_function():
    print("i am inside function")

my_function()
#now if we want to use that module by importing we have to comment out our call.
#rather than that best approach is to use following code:
#python program to use main for function call
if __name__=="__main__":
    my_function()
import myscript 
myscript.my_function()
#advantages:
#every python module has its __name__ defined and if thi sis " __main__" , it implies that the module is being run standalone by the user and we can do corresponding appropiate actions.
#if yopu import this script as a module in another script , the __name__ is set to the name of the script or module 
#python files can act as aeither reusable modules ,or s standalone programs .
#4. if __name __ =="main " : is used to execute some code only if the file was run directly , and not imported .

