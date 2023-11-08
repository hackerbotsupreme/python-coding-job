#write a program to find whether a given number is prime or not 
#what is a prime num 
#a whole number greater than 1 that cannot be exactly divided by any whole number other than itselfand 1 (e.g. 2,3,5,7,11)
#prime numbers are very useful in cryptography
num=int(input("enter you number:" ))
prime= False
for i in range (2,num):
    if(num%i==0):
        prime=True
        break
if prime:   
    print("this number is prime ")
else:
    print("this number is  not prime ")
    
