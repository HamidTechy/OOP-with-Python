import random

randNumber = random.randint(1, 20)
user = None
guesscount = 0

while randNumber != user:

    user = int(input("guess number from 1 to 20"))
    guesscount += 1

    if randNumber == user:
        print("you choose the correct number")
    elif randNumber > user:
        print("choose larger number")
    elif randNumber < user:
        print("choose smaller number")


print(f"{guesscount} times you choose number")

with open("highscore.txt", "r") as f:
    hiscore = int(f.read())

if guesscount < hiscore:
    with open("highscore.txt", "w") as f:
        f.write(str(guesscount))
