import random
num=random.randint(1,10)
attempts=0
score=0
for attempts in range(5):
    guess=int(input("Enter your guess:"))
    if guess==num:
        print("Correct guess")
        score+=1
        break
    else:
        if score>0:
            score=score-1
        else:
            score=0
    attempts+=1
    if attempts==5:
        print("You lost all your guesses,the number was:",num)
print("Score is:",score)