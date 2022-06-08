## project 
## snake water gun

import random

def gameWin(computer,player):
    if computer == player:
        return None
    elif computer == "s":
        if player == "w":
            return False
        elif player == "g":
            return True
    elif computer == "w":
        if player == "g":
            return False
        elif player == "s":
            return True
    elif computer == "g":
        if player == "s":
            return False
        elif player == "w":
            return True
        
print("Computer Turn:  Snake (s) Water (w) Gun (g) ? ")
random_no = random.randint(1,3)
## print(random_no)
if random_no == 1:
    computer = "s"
elif random_no == 2:
    computer = "w"
elif random_no == 3:
    computer = "g"

player = input("Player Turn: Snake (s) Water (w) Gun (g) ? ")

game = gameWin(computer,player)

print(f"computer choose {computer}")
print(f"player choose {player}")

if game == None:
    print("The Game Is TIE")
elif game:
    print("CONGRATULATION YOU WON !!!!")
else:
    print("YOU LOSSE")