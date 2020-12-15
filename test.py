from random import randint

#create a list of play options
t = ["Rock","Paper","Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player= input("Rock, Paper, Scissors? :")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose! {} covers {}".format(player,computer))
        else:
            print("You win! {} shashes {}".format(player,computer))
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose! {} cuts {}".format(player,computer))
        else:
            print("You win! {} covers {}".format(player,computer))
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose! {} smashes {}".format(player,computer))
        else:
            print("You win! {} cuts {}".format(player,computer))
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues 
    player = False
    computer = t[randint(0,2)]
