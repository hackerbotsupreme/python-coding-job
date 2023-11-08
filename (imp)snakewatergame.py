#we all have played snake wate and gun game in our childhood, so write a program to play the game with user.
import random
def gamewin(comp,you):
    if comp=='s':
        if you=='w':
          return False
        elif you=='g':
          return True
    elif comp=='w':
        if you=='w':
            return False
        elif you=='g':
          return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
          return True
            

randno= random.radiant(1,2)#this function chooses the random value between the vakues given between the brackets 
print(randno)
a=input("comp turn : snake(s)  water(w) or Gun(n)?")
randno=random.radiant(1,3)
print(randno)
if randno== 1:
    comp='s'
elif randno==2:
    comp='w'
elif randno == 3:
    compp='g'
you= input("player's turn: snake(1)  water(2) or Gun(3)?")
gamewin(comp,you)





