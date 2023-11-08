#a file contains a word"donkey"   multiple times  you nees to write a progran which replaces this word with ##### by updating the same file 

with open("sample.txt") as f:
    content = f.read()

content = content.replace("donkey", "$%^@$^#")

with open("sample.txt", "w") as f:
    f.write(content)
#why the content is not writing i need to find out?   