import random

def computer_move(moves_list, level):
    """
    Generates the computer's move based on the configured game level in main.py.
    Level 1 does not perform any validations.
    Level 2 checks the user's move and acts accordingly to prevent a line from being completed.

    Args:
    moves_list (list): A list of moves and available cells for playing.
    level (int): The game level.

    Returns:
    moves_list (list): An updated list of moves with the user's move.
    """
    
    if level == 1: 
        while True:
            computer_move = random.randrange(0,9)
            if not isinstance(moves_list[computer_move], int):
                continue
            else:
                moves_list[computer_move] = "O"
                print(f"Computer played: {computer_move}")
                break
        
        return moves_list
    
    else: # level = 2
        if moves_list[1] == "X" and moves_list[2] == "X" and moves_list[0] == 1: 
            moves_list[0] = "O" #Computer played 0                    
            
        elif moves_list[0] == "X" and moves_list[2] == "X" and moves_list[1] == 2: 
            moves_list[1] = "O" #Computer played 1 
            
        elif moves_list[0] == "X" and moves_list[1] == "X" and moves_list[2] == 3:
            moves_list[2] = "O" #Computer played 2 
            
        elif moves_list[4] == "X" and moves_list[5] == "X" and moves_list[3] == 4: 
            moves_list[3] = "O" # Computer played 3
            
        elif moves_list[3] == "X" and moves_list[5] == "X" and moves_list[4] == 5: 
            moves_list[4] = "O" # Computer played 4
            
        elif moves_list[3] == "X" and moves_list[4] == "X" and moves_list[5] == 6: 
            moves_list[5] = "O" # Computer played 5
           
        elif moves_list[7] == "X" and moves_list[8] == "X" and moves_list[6] == 7: 
            moves_list[6] = "O" # Computer played 6 
            
        elif moves_list[6] == "X" and moves_list[8] == "X" and moves_list[7] == 8: 
            moves_list[7] = "O" # Computer played 7                               
            
        elif moves_list[6] == "X" and moves_list[7] == "X" and moves_list[8] == 9: 
            moves_list[8] = "O" # Computer played 8
            
        elif moves_list[3] == "X" and moves_list[6] == "X" and moves_list[0] == 1:
            moves_list[0] = "O" # Computer played 0   
            
        elif moves_list[0] == "X" and moves_list[6] == "X" and moves_list[3] == 4: 
            moves_list[3] = "O" # Computer played 3
            
        elif moves_list[0] == "X" and moves_list[3] == "X" and moves_list[6] == 7:
            moves_list[6] = "O" # Computer played 6
            
        elif moves_list[4] == "X" and moves_list[7] == "X" and moves_list[1] == 2: 
            moves_list[1] = "O" # Computer played 1  
            
        elif moves_list[1] == "X" and moves_list[7] == "X" and moves_list[4] == 5: 
            moves_list[4] = "O" # Computer played 4
            
        elif moves_list[1] == "X" and moves_list[4] == "X" and moves_list[7] == 8: 
            moves_list[7] = "O" # Computer played 7
            
        elif moves_list[5] == "X" and moves_list[8] == "X" and moves_list[2] == 3: 
            moves_list[2] = "O" # Computer played 2       
            
        elif moves_list[2] == "X" and moves_list[8] == "X" and moves_list[5] == 6: 
            moves_list[5] = "O" # Computer played 5
            
        elif moves_list[2] == "X" and moves_list[5] == "X" and moves_list[8] == 9:
            moves_list[8] = "O" # Computer played 8
            
        elif moves_list[4] == "X" and moves_list[8] == "X" and moves_list[0] == 1: 
            moves_list[0] = "O" # Computer played 0
            
        elif moves_list[0] == "X" and moves_list[8] == "X" and moves_list[4] == 5: 
            moves_list[4] = "O" # Computer played 4   
            
        elif moves_list[0] == "X" and moves_list[4] == "X" and moves_list[8] == 9: 
            moves_list[8] = "O" # Computer played 8
            
        elif moves_list[6] == "X" and moves_list[4] == "X" and moves_list[2] == 3:
            moves_list[2] = "O" # Computer played 2   
           
        elif moves_list[6] == "X" and moves_list[2] == "X" and moves_list[4] == 5: 
            moves_list[4] = "O" # Computer played 4 
            
        elif moves_list[2] == "X" and moves_list[4] == "X" and moves_list[6] == 7: 
            moves_list[6] = "O" # Computer played 6
            
        else:
            while True:
                computer_move = random.randrange(0,9)
                if not isinstance(moves_list[computer_move], int):
                    continue
                else:
                    moves_list[computer_move] = "O"
                    break
            
            return moves_list
