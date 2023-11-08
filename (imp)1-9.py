#write a program to read the text from the given  'file'poems.txt' and find out whether  it contains the word twinkle 
f=open('poems.txt')
t=f.read()
if 'twinkle ' in t:
    print("twinkle is present ")
else:
    print("twinkle is not present ")
f.close()
with open ('poems.txt','w')as f:
    a=f.write(" this is my time")
print(a)# i need to find out why this piece of code from with to print(a) is not working
    
