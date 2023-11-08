#python program to capitalize firat and last charecter of the string
#lets breakdown the question -- what is a string -- string is a cetain sequence of charecters 
#in other words  it is a collection of words
#and in this ques tion 'captilize first and last charecters of the string ' means capitalizing every first and last charecter of every word/sentence


#its like first we have to break the whole string in its component strings/sentences/words
#then somehow uppercase the edge charecters and then join the pieces together again
#attempt1
#slicing, upper(), split()
s="welcome to the geeks for geeks"
print("string before :",s)
a=s.split()
res=[]
for i in a :
    x=i[0].upper()+ i[-1]+i[-1].upper()
    res=' '.join(res)
print("string after :", res)



#