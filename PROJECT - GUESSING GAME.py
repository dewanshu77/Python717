#PROJECT GUESSING GAME
print('perfect')
guess_limit=3
guess_count=0
while guess_count<guess_limit:
     guess=int(input("sir, please can you enter your guessings on the screen : "))
     guess_count+=1
     if guess==9:
         print("you won")
         break
else :
 print("sorry looks like you guessed wrong no. and failed to answer dont worry try again")

