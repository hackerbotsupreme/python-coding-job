#write a program to find the sum of first n natural number using while loop
#n!=1 X 2 X 3 X .....n 
#5!= 1X 2 X 3 X 4 X 5

num =int(input("enter the number:"))
factorial =1
for i in range(1, num+1):
    factorial=factorial * i                                       #when we try this as we thinks
                                                        #print ("the factorial of the number is", (factorial)) 
print(f"the factorial of this number is {factorial}") 
#when we do this                                            #enter the number:7
#enter the number:7
#the factorial of this number is 5040                      #the factorial of the number is 1
                                                            #the factorial of the number is 2
                                                            #the factorial of the number is 6
                                                            #the factorial of the number is 24
                                                            #the factorial of the number is 120
                                                            #the factorial of the number is 720
                                                            #the factorial of the number is 5040
#then what is the difference between them   