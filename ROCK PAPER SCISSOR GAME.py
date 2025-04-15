import random

def game(user,computer):
    print(f" USER CHOICE : {user_choice}")
    print(f" COMPUTER CHOICE : {computer_choice}")

    if user_choice == computer_choice:
        return "**** TIE **** "
    elif user_choice == "ROCK" and computer_choice == "PAPER":
        return "**** COMPUTER WON THE MATCH **** "
    elif user_choice == "ROCK" and computer_choice == "SCISSER":
        return "**** USER WON THE MATCH **** "
    

    elif user_choice == "PAPER" and computer_choice == "ROCK":
        return "**** USER WON THE MATCH **** "
    elif user_choice == "PAPER" and computer_choice == "SCISSER":
        return "**** COMPUTERUSER WON THE MATCH **** "
    

    elif user_choice == "SCISSER" and computer_choice == "ROCK":
        return "**** COMPUTER WON THE MATCH **** "
    elif user_choice == "SCISSER" and computer_choice == "PAPER":
        return "**** USER WON THE MATCH **** "

game_list = ["ROCK","PAPER","SCISSOR"]

menu = """

                    MENU
            
                ROCK
                PAPER
                SCISSOR

"""
status = True
while status:
    print(menu)

    user_choice = input("Enter your choice : ").upper()
    computer_choice = random.choice(game_list)

    result = game(user_choice,computer_choice)
    print(f"RESULT : {result} \n")

    game_choice = input("DO you want to ply again press 'y' for yes and 'n' for no : ").lower()
    if game_choice == 'y' or game_choice == 'yes':
        status = True
    else:
        status = False
    