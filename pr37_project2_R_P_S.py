# ## project
# ## Rock Paper Scissor

import random

print("WELCOME TO ROCK PAPER SCISSOR")

def game(computer,user):
    if computer == user:
        return None
    elif computer == "r":
        if user == "s":
            return False
        elif user == "p":
            return True

    elif computer == "p":
        if user == "s":
            return True
        elif user == "r":
            return False

    elif computer == "s":
        if user == "p":
            return False
        elif user == "r":
            return True

print("Computer Turn:  Rock(r) Paper(p) Scissor(s) ?")
random_number = random.randint(1,3)

if random_number == 1:
    computer = "r"
elif random_number == 2:
    computer = "p"
elif random_number == 3:
    computer = "s"

user = input("Player Turn : Rock(r) Paper(p) Scissor(s) ?")

print(f"computer choose {computer}")
print(f"user choose {user}")

rps_game = game(computer,user)
if rps_game == None:
    print("Tie")
elif rps_game :
    print("YOU WIN !!!")
else:
    print("YOU LOSSE Try Again ")
