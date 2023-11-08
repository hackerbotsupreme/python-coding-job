#you are given a list of cencosored word and and a file now what 
# you have todo is to if you find any word of the list in the file you have to replace it so write a program to do that  
words=["donkeys","kaddu", "mote",] #and the file you have is----sample3.txt

with open("sample3.txt") as f:
    content = f.read()

for word in words:

 content=content.replace(word,"###")
 with open ("sample3.txt","w") as f:
    f.write(content)
#i really need to find out that why the write mode is not working ?or i am doing something wrong?