import random

def get_comp_choice():
    return random.randint(1,3)

def who_is_winner(player,pc):
    if (player == "r") | (player == "rock") | (player == "1"):
        a = 1
    elif (player == "p") | (player == "paper") | (player == "2"):
        a = 2
    elif (player == "s") | (player == "scissor") | (player == "3"):
        a = 3
    else:
        return "redo"

    if (a == 1):
        if (pc == 1):
            return "tie"
        elif (pc == 2):
            return "pc"
        else:
            return "player"
        
    elif (a == 2):
        if (pc == 1):
            return "player"
        elif (pc == 2):
            return "tie"
        else:
            return "pc"

    else:
        if (pc ==1):
            return "pc"
        elif (pc == 2):
            return "player"
        else:
            return "tie"
