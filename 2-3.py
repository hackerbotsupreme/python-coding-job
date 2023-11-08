#a program to fill in a letter template given below with name and date 
letter=''' dear<|name|>,
you are selected 

date:<|date|>
'''
name=input("enter your name : \n ")
date=input("enter date :\n")
letter=letter.replace("<|name|>", name)#letter.replce("name",name) is need tobe sved after replacing
letter=letter.replace("<|date|>",date)# same for this
print(letter)