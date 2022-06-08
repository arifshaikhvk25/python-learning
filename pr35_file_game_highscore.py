# ## def game()function in a program user play game return score in integer read file pr36_high_score either blank or contains previous highscore 

def game():
    return 5

score = game()
with open("pr36_high_score") as f:
    highscore = int(f.read())

if highscore < score:
    with open("pr36_high_score", "w") as f:
        f.write(str(score))
        # f.write(f"{score}")
        