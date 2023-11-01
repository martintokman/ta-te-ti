def player_move(moves_list):
    """
    Requests the user to enter their move and checks if the input is valid.
    If the input is valid, it saves the move in the list of moves; if it's invalid, it requests a new input.

    Args:
    moves_list (list): A list of moves and available cells for playing.

    Returns:
    moves_list (list): An updated list of moves with the user's move.
    """
    while True:
        try:
            print("")
            player_move = int(input("Enter your option (1-9):"))
            player_move -= 1
            if (player_move + 1) < 1 or (player_move + 1) > 9:
                print("Only numbers from 1-9, try again.")
                continue
            elif not isinstance(moves_list[player_move], int):
                print("Cell already played, try again.")
                continue
            else:
                break
        except ValueError:
            print("Only numbers allowed, try again.")

    moves_list[player_move] = "X"
    return moves_list