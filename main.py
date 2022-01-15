from random import randint

while True:
    player_2 = "computer"
    won_games = 0
    how_many_wanted = 0
    counter = 0
    mode = input('Do you want to play with the computer or someone else? Please type (single) to play against the computer or (multi) to play against a friend.\n')
    won_games = 0


    if mode != "single" and mode != "multi":
        print("That is an invalid mode.")
        continue
    #Single Player Mode

        
    print('Please choose how many rounds you would like to play! EG: [1, 5]\n')
    

    try:
        how_many_wanted = int(input())
    except:
        print("You have entered an invalid amount of rounds. Please enter a whole number. EG: [1, 23]")

    
    while counter < how_many_wanted :
        
        
        player_choice = input('Type rock (r), paper (p) or scissors (s):')
        print("You chose:",player_choice)
        


        if mode == "single":

            random_choice = randint(1,3)
            if random_choice == 1:
                computer_choice = 'r'
            elif random_choice == 2:
                computer_choice = 'p'
            else:
                computer_choice = 's'
            print("The computer chose:",computer_choice)
        elif mode == "multi":

            player_2 = "Player two"
            computer_choice = input("Player two. Type rock (r), paper (p) or scissors (s):\n")

        if player_choice == computer_choice:
            print("The game has concluded. The results are a draw!")
        elif player_choice == "s" and computer_choice == "r":
            print(f'The game has concluded. {player_2} wins!')
        elif player_choice == "r" and computer_choice == "s":
                print("The game has concluded. You won!")
                won_games = won_games + 1
        elif player_choice == "p" and computer_choice == "r":
                print("The game has concluded. You won!")
                won_games = won_games + 1
        elif player_choice == "s" and computer_choice == "p":
                print("The game has concluded. You won!")
                won_games = won_games + 1
        elif player_choice == "r" and computer_choice == "p":
                print(f'The game has concluded. {player_2} wins!')
        elif player_choice == "p" and computer_choice == "s":
                print(f'The game has concluded. {player_2} wins!')
        else:
            print ("Something has gone wrong... Please try again. Make sure you are typing a valid option!")
            counter = counter - 1

        counter = counter + 1
        print(f'You have played {counter} games! You choose to play {how_many_wanted} game(s). You have {how_many_wanted-counter} game(s) remaining. Out of {counter} game(s) you have played you have won {won_games}!')

