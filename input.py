#input function in python -- used to take inputs from the user 
a=input("Enter your name :")#you will enter your name and it will be passed or printed in next step
print (a)     # imp : if we give a number as a input then tell me will that be passed as a string or int in next step 
print(type(a))# and in the terminal you will see the class type is str so we can say whatever we are giving as an input 
              #it is going into double quote so that is why is is coverting into string data typee even if we give int/num as a input
              #so again if we need to pass as int in the next step then we can typecast it like
b=input("Enter your num aloke :")
b=int(b)      # convert b to integer  and again not everything can be converted into int as string to integer is not possible 
print(type(b))


