def check_winner(moves_list):
    """
    Receives the list of moves to validate if there is a winner, a tie, or if no one has won, and the game continues.

    Args:
    moves_list (list): A list of moves and available cells for playing.

    Returns:
    list: A list of moves and available cells for playing.
    """

    # Contidions for the user to win
    # Rows

    if moves_list[0] == "X" and moves_list[1] == "X" and moves_list[2] == "X":
        winner = "user"
    elif moves_list[3] == "X" and moves_list[4] == "X" and moves_list[5] == "X":
        winner = "user"
    elif moves_list[6] == "X" and moves_list[7] == "X" and moves_list[8] == "X":
        winner = "user"

    # Columns 
    elif moves_list[0] == "X" and moves_list[3] == "X" and moves_list[6] == "X":
        winner = "user"
    elif moves_list[1] == "X" and moves_list[4] == "X" and moves_list[7] == "X":
        winner = "user"
    elif moves_list[2] == "X" and moves_list[5] == "X" and moves_list[8] == "X":
        winner = "user"

    # Diagonals
    elif moves_list[0] == "X" and moves_list[4] == "X" and moves_list[8] == "X":
        winner = "user"
    elif moves_list[2] == "X" and moves_list[4] == "X" and moves_list[6] == "X":
        winner = "user"


    # Conditions for the computerter to win
    # Rows
    elif moves_list[0] == "O" and moves_list[1] == "O" and moves_list[2] == "O":
        winner = "computer"
    elif moves_list[3] == "O" and moves_list[4] == "O" and moves_list[5] == "O":
        winner = "computer"
    elif moves_list[6] == "O" and moves_list[7] == "O" and moves_list[8] == "O":
        winner = "computer"

    # Columns
    elif moves_list[0] == "O" and moves_list[3] == "O" and moves_list[6] == "O":
        winner = "computer"
    elif moves_list[1] == "O" and moves_list[4] == "O" and moves_list[7] == "O":
        winner = "computer"
    elif moves_list[2] == "O" and moves_list[5] == "O" and moves_list[8] == "O":
        winner = "computer"

    # Diagonals
    elif moves_list[0] == "O" and moves_list[4] == "O" and moves_list[8] == "O":
        winner = "computer"
    elif moves_list[2] == "O" and moves_list[4] == "O" and moves_list[6] == "O":
        winner = "computer"
    
    
    else:
        # Draw
        counter = 0
        for element in moves_list:
            if not isinstance(element, int):
                counter += 1
        if counter == 9:
            winner = "draw"
        else:
            winner = "none"

    return winner