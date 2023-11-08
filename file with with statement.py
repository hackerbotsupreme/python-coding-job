#the best way  to open and close the file automatically is with statement

with open("sample.txt") as f:
    content = f.read()

content = content.replace("donkey", "$%^@$^#")

with open("sample.txt", "w") as f:
    f.write(content)