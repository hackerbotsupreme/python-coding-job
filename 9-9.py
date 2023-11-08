#write a program to find out whether a file is identical & matches the content of anothe file
file1="this.txt"
file2="copy.txt"


with open(file1)as f:
    content=f.read()
with open (file2) as f:
    f.write(content)

    

    
    