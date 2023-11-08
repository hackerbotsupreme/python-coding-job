with open ("this.txt") as f:
    content=f.read()
with open ("copy1.txt", "w") as f:
    f.write(content)