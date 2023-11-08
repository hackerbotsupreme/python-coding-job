#like other built in  functions recursion is formula that is called to use the formula in our function  
#the formula is factorial of n = n*factorial(n-1) so basically its a function of finding  factorial of a num 
#the formula of factorial is  ---n!=1*2*3*4*.....n --->[1*2*3*4*5....(n-1)]*n---->(n-1)!*n
n=4
product=1                             #so as we can see we need to towrite these many lines to find the factorial
for i  in range(n):                   # also we need to write it every time we need to find a factorial
    product=product*(i+1)             #whare if we call the recursion then it would be done instantaneously
print(product)#24


def factorial(n):
    product =1
    for i in range (n):                #weare defining a fuction to call that would give us the factorial every 
     product=product *  (i+1)          #every time we need without writing the same code overand over
    return product
f=factorial(6)
print(f)


def factorial_recursive(n):
    if i==1 or n==0 :                  #basa condition ehich doesnot calls the function any further
        return 1                               #factorial recursive / recursion 
    return n*factorial_recursive(n-1)  #factorial_recursive(n-1) this is the function that calls itsself 
#                                                    check notes for any revision 


q=factorial_recursive(5)
print(q) 
t=factorial_recursive(0)  
print(0) 

#  note:the programmer need to be extremely careful while working with recursion to ensure that the function
# didnot infinitely calling itself .recursion is sometimes the most direct to code an lagorithm