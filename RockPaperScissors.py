# RockPaperScissors.py
# @ Timothy Tomas 2019
# Date: 21/05/19
# Description: A game of rock, paper, scissors - user inputs their symbol of choice
# and program randomly chooses its symbol. Values are compared and the player with the
# winning symbol is declared the winner.

import random   # importing random function for computer selection


# welcome message and instructions
print("\n-ROCK- -PAPER- -SCISSORS-\n\n")
player_name = input("Enter your name: ").title()
print("\nWelcome {}, I challenge you to a game of Rock, Paper, Scissors!\n\n"
      "To choose 'Rock', type 'R'...\n"
      "To choose 'Paper', type 'P'...\n"
      "To choose 'Scissors', type 'S', then press ENTER.\n\n"
      "Exit any time by typing 'E', then pressing ENTER.\n".format(player_name))
print("Let's play!\n\n")

is_running = True   # instantiating loop, can only terminate loop if exiting
while is_running is True:
    rps_dict = {"R": "Rock",
                "P": "Paper",
                "S": "Scissors",
                "E": "Exit"}
    # input section
    input_valid = False
    while input_valid is False:    # loops input section until  a valid response given
        player_selection_input = input("Type the shape you wish to throw.\n" 
                                       "(R = Rock, P = Paper, S = Scissors or E to Exit)\n\n").title()
        # exit conditions
        if player_selection_input == "E":
            stop = input("Are you sure you wish to quit? (Y/N)").title()
            if stop == "Y" or stop == "Yes":
                print("Goodbye {}!".format(player_name))
                exit()
        elif player_selection_input not in rps_dict:    # loops to start of section
            print("Invalid input, please enter a valid shape!")
            input_valid = False
        else:
            input_valid = True    # if input is valid, moves on to the output section

    # output section
    rps_dict.pop("E")
    computer_selection = (random.choice(list(rps_dict.keys())))

    print("You threw {}...".format(rps_dict.get(player_selection_input)), end=" ")
    print("Computer throws {}!".format(rps_dict.get(computer_selection)))

    if player_selection_input == "R" and computer_selection == "Scissors":
        print("You win!!\n")
    elif player_selection_input == "P" and computer_selection == "Rock":
        print("You win!!\n")
    elif player_selection_input == "S" and computer_selection == "Paper":
        print("You win!!\n")
    elif player_selection_input == computer_selection:
        print("It's a tie!\n")
    else:
        print("Computer wins!\n")






