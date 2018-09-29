import veritas_lib

my_choice = input("What is your choice? [r, p, s]")

comp_choice = veritas_lib.get_comp_choice()

x = 1

while (x == 1):
    winner = veritas_lib.who_is_winner(my_choice, comp_choice)
    if (winner == "redo"):
        print ("Please type in [r, p, s].")
        x = 2
    x = x - 1

if (winner == "player"):
    print ("You won!")
elif (winner == "pc"):
    print ("You lost!")
else:
    print ("You tied!")

print (comp_choice)
