#write a program to print multiplication table of a given  number for loop
num = int(input("enter the number:"))
for i in range(1,11) :
    print(str(num)+"X"+str(i)+"="+str(i*num))
    #above line is valid but there is also a short way to do this 
    # like this,print(f"{num}X{i}={num*i}")