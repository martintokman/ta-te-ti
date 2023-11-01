
Tic-Tac-Toe Game

1) Display the numbered game board from 1 to 9.
2) Ask the user for their move.
3) Display the game board with the user's move, and the available spots are renumbered.
4) Show the game board with the computer's move, and the available spots are renumbered.
5) Check if the game is over.
6) If the game is not over, return to the cycle of user and computer moves.
7) If the game is over, display the results and ask if you want to play again.
8) If you want to play again, restart the game; if not, exit.


Board
-------------
| 0 | 1 | 2 |
-------------
| 3 | 4 | 5 |
-------------
| 6 | 7 | 8 |
-------------


Conditions for the user to win:

Rows
moves[0] == "X" and moves[1] == "X" and moves[2] == "X"
moves[3] == "X" and moves[4] == "X" and moves[5] == "X"
moves[6] == "X" and moves[7] == "X" and moves[8] == "X"

Columns
moves[0] == "X" and moves[3] == "X" and moves[6] == "X"
moves[1] == "X" and moves[4] == "X" and moves[7] == "X"
moves[2] == "X" and moves[5] == "X" and moves[8] == "X"

Diagonals
moves[0] == "X" and moves[4] == "X" and moves[8] == "X"
moves[2] == "X" and moves[4] == "X" and moves[6] == "X"

Conditions for the computer to win:

Rows
moves[0] == "O" and moves[1] == "O" and moves[2] == "O"
moves[3] == "O" and moves[4] == "O" and moves[5] == "O"
moves[6] == "O" and moves[7] == "O" and moves[8] == "O"

Columns
moves[0] == "O" and moves[3] == "O" and moves[6] == "O"
moves[1] == "O" and moves[4] == "O" and moves[7] == "O"
moves[2] == "O" and moves[5] == "O" and moves[8] == "O"

Diagonals
moves[0] == "O" and moves[4] == "O" and moves[8] == "O"
moves[2] == "O" and moves[4] == "O" and moves[6] == "O"

Difficulty levels:
Level 1 (Easy): The computer randomly selects an empty cell without checking the user's moves.

Level 2 (Intermediate): The computer checks if the user is about to complete a line when they already have 2 "X" and only need one more cell to win. If it detects this situation, it plays in the cell the user needs to complete the line before the user does.

Combinations to watch to mitigate the situation:

---------------------------------------------------------------------------------------------------------
--------------------------------------------------- Rows ------------------------------------------------

moves[1] == "X" and moves[2] == "X" -> The computer plays 0
moves[0] == "X" and moves[2] == "X" -> The computer plays 1
moves[0] == "X" and moves[1] == "X" -> The computer plays 2

-------------   -------------   -------------                           
|   | 1 | 2 |   | 0 |   | 2 |   | 0 | 1 |   |                          
-------------   -------------   -------------                          
|   |   |   |   |   |   |   |   |   |   |   |                          
-------------   -------------   -------------                          
|   |   |   |   |   |   |   |   |   |   |   |                          
-------------   -------------   -------------                          
 

moves[4] == "X" and moves[5] == "X" -> The computer plays 3
moves[3] == "X" and moves[5] == "X" -> The computer plays 4
moves[3] == "X" and moves[4] == "X" -> The computer plays 5

-------------   -------------   -------------   
|   |   |   |   |   |   |   |   |   |   |   |   
-------------   -------------   -------------   
|   | 4 | 5 |   | 3 |   | 5 |   | 3 | 4 |   |   
-------------   -------------   -------------   
|   |   |   |   |   |   |   |   |   |   |   |   
-------------   -------------   -------------  

moves[7] == "X" and moves[8] == "X" -> The computer plays 6
moves[6] == "X" and moves[8] == "X" -> The computer plays 7
moves[6] == "X" and moves[7] == "X" -> The computer plays 8

-------------   -------------   -------------   
|   |   |   |   |   |   |   |   |   |   |   |   
-------------   -------------   -------------   
|   |   |   |   |   |   |   |   |   |   |   |   
-------------   -------------   -------------   
|   | 7 | 8 |   | 6 |   | 8 |   | 6 | 7 |   |   
-------------   -------------   -------------  

----------------------------------------------- End Rows ------------------------------------------------
---------------------------------------------------------------------------------------------------------


---------------------------------------------------------------------------------------------------------
--------------------------------------------------- Columns ---------------------------------------------

moves[3] == "X" and moves[6] == "X" -> The computer plays 0
moves[0] == "X" and moves[6] == "X" -> The computer plays 3
moves[0] == "X" and moves[3] == "X" -> The computer plays 6

-------------   -------------   -------------   
|   |   |   |   | 0 |   |   |   | 0 |   |   |   
-------------   -------------   -------------   
| 3 |   |   |   |   |   |   |   | 3 |   |   |   
-------------   -------------   -------------   
| 6 |   |   |   | 6 |   |   |   |   |   |   |   
-------------   -------------   -------------  

moves[4] == "X" and moves[7] == "X" -> The computer plays 1
moves[1] == "X" and moves[7] == "X" -> The computer plays 4
moves[1] == "X" and moves[4] == "X" -> The computer plays 7

-------------   -------------   -------------   
|   |   |   |   |   | 1 |   |   |   | 1 |   |   
-------------   -------------   -------------   
|   | 4 |   |   |   |   |   |   |   | 4 |   |   
-------------   -------------   -------------   
|   | 7 |   |   |   | 7 |   |   |   |   |   |   
-------------   -------------   -------------  

moves[5] == "X" and moves[8] == "X" -> The computer plays 1
moves[2] == "X" and moves[8] == "X" -> The computer plays 5
moves[2] == "X" and moves[5] == "X" -> The computer plays 8

-------------   -------------   -------------   
|   |   |   |   |   |   | 2 |   |   |   | 2 |   
-------------   -------------   -------------   
|   |   | 5 |   |   |   |   |   |   |   | 5 |   
-------------   -------------   -------------   
|   |   | 8 |   |   |   | 8 |   |   |   |   |   
-------------   -------------   -------------  


                                    
--------------------------------------------------  End columns  ---------------------------------------------------
--------------------------------------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------------------------------------
---------------------------------------------------   Diagonals   --------------------------------------------------
  
moves[4] == "X" and moves[8] == "X" -> The computer plays 0                                                                   
moves[0] == "X" and moves[8] == "X" -> The computer plays 4                               
moves[0] == "X" and moves[4] == "X" -> The computer plays 8

-------------   -------------   -------------   
|   |   |   |   | 0 |   |   |   | 0 |   |   |   
-------------   -------------   -------------   
|   | 4 |   |   |   |   |   |   |   | 4 |   |   
-------------   -------------   -------------   
|   |   | 8 |   |   |   | 8 |   |   |   |   |   
-------------   -------------   -------------  

                                    


moves[6] == "X" and moves[4] == "X" -> The computer plays 2                                                                   
moves[6] == "X" and moves[2] == "X" -> The computer plays 4                               
moves[2] == "X" and moves[4] == "X" -> The computer plays 6
-------------   -------------   -------------   
|   |   |   |   |   |   | 2 |   |   |   | 2 |   
-------------   -------------   -------------   
|   | 4 |   |   |   |   |   |   |   | 4 |   |   
-------------   -------------   -------------   
| 6 |   |   |   | 6 |   |   |   |   |   |   |   
-------------   -------------   -------------  
                                    
----------------------------------------------   End Diagonals   ---------------------------------------------------
--------------------------------------------------------------------------------------------------------------------