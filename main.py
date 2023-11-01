from show_board import show_board
from player_move import player_move
from check_winner import check_winner
from computer_move import computer_move
import sys, os



level = 2

while True: # Create infinite loop (restart)

    moves_list = [1,2,3,4,5,6,7,8,9]

    os.system("clear")

    show_board(moves_list)

    while True: # Create ininite loop (game)
        
        # Player move
        player_move(moves_list)

        # Show board
        show_board(moves_list)


        # Check for winner
        winner = check_winner(moves_list)
        if winner == "user" or winner == "computer" or winner == "draw":
            break
 

        # computer move
        computer_move(moves_list, level)

        os.system("clear")

        # Show board
        show_board(moves_list)

        # Check winner
        winner = check_winner(moves_list)
        if winner == "user" or winner == "computer" or winner == "draw":
            break



    # Game finished, show result
    os.system("clear")

    # Show board
    show_board(moves_list)  

    print(f"\nwinner: {winner}")

    while True:
        play_again = input("Play again? (y/n): ")
        play_again = play_again.upper()
        if play_again == "Y" or play_again == "N":
            break
        else:
            print("Invalid option, try again.")
            continue
    
    if play_again == "Y":
        continue
    elif play_again == "N":
        print("\nThanks for playing. See you next time :)\n")
        exit()
