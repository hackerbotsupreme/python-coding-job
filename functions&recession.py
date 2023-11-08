# what is the function 
#function is a  group of statements programming performing a specific task.
# when  we specifically we use fuctions , when the program gets bigger and its complexity grows then we
# cant use normal things bcz we will eventually start to forget what which is doing so that when function comes into play
#for exampletake a look at the following examples
#but when you know about function this is how you do it
def percent(marks):
    return((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
marks1=[45,78,86,77]
marks2=[75,78,96,37]
print("the percentage of marks1 is",percent(marks1))
print("the percentage of marks1 is",percent(marks2))

#if you dont know about functions then if you need to find percentage then this is how you do it
marks1=[45,78,86,77]
percentage1=(sum(marks1)/400)*100

marks2=[75,78,96,37]
percentage2=(sum(marks2)/400)*100
print(percentage1,percentage2)


#thats what the difference is it  is one liner it is best 