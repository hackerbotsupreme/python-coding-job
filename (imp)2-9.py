
#the game() function in a program lets a user play a game amd returns the score  as an integer . you need to read a file 'hiscore.txt' which is either  
# blank or contains the previous hi score .you need to write a program to update the hi-score whenevr game(breaks the hi-score.)
def game():
    return 664

score=game()
with open("hiscore.txt")as f:
    hiscorestr=f.read()
if hiscorestr=='':
    with open ("hiscore.txt","w")as f:
        f.write(str(score))
elif int(hiscorestr)<score :
    with open("hiscore.txt","w") as f :
        f.write(str(score))


