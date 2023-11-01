from termcolor import colored


def show_board(moves_list):
    """
    Imprime en consola el tablero con las jugadas realizadas y las celdas disponibles para jugar.
    Las jugadas del usuario se muestran en color rojo.
    Las jugadas de la compu se muestran en color amarillo.

    Args:
        moves_list (list): Lista de jugadas y celdas disponibles para jugar.
    """
    
    for i in range(2): print("")
    print ("-------------")
    
    #agrego colores a las jugadas, rojo al usuario y amarillo a la compu
    #fila1
    print("| ", end="")
    if moves_list[0] == "X": 
        print(colored(moves_list[0], "red"), end=" ")
    elif moves_list[0] == "O":
        print(colored(moves_list[0], "yellow"), end=" ")
    else:
        print(colored(moves_list[0], "dark_grey"), end=" ")

    
    
    print("| ", end="")
    if moves_list[1] == "X": 
        print(colored(moves_list[1], "red"), end=" ")
    elif moves_list[1] == "O":
        print(colored(moves_list[1], "yellow"), end=" ")
    else:
        print(colored(moves_list[1], "dark_grey"), end=" ")

    print("| ", end="")
    if moves_list[2] == "X": 
        print(colored(moves_list[2], "red"), end=" |\n")
    elif moves_list[2] == "O":
        print(colored(moves_list[2], "yellow"), end=" |\n")
    else:
        print(colored(moves_list[2], "dark_grey"), end=" |\n")
        

    
    print ("-------------")


    #fila 2
    print("| ", end="")
    if moves_list[3] == "X": 
        print(colored(moves_list[3], "red"), end=" ")
    elif moves_list[3] == "O":
        print(colored(moves_list[3], "yellow"), end=" ")
    else:
        print(colored(moves_list[3], "dark_grey"), end=" ")
    
    
    print("| ", end="")
    if moves_list[4] == "X": 
        print(colored(moves_list[4], "red"), end=" ")
    elif moves_list[4] == "O":
        print(colored(moves_list[4], "yellow"), end=" ")
    else:
        print(colored(moves_list[4], "dark_grey"), end=" ")

    print("| ", end="")
    if moves_list[5] == "X": 
        print(colored(moves_list[5], "red"), end=" |\n")
    elif moves_list[5] == "O":
        print(colored(moves_list[5], "yellow"), end=" |\n")
    else:
        print(colored(moves_list[5], "dark_grey"), end=" |\n")

    
    print ("-------------")


    #fila 3
    print("| ", end="")
    if moves_list[6] == "X": 
        print(colored(moves_list[6], "red"), end=" ")
    elif moves_list[6] == "O":
        print(colored(moves_list[6], "yellow"), end=" ")
    else:
        print(colored(moves_list[6], "dark_grey"), end=" ")
    
    
    print("| ", end="")
    if moves_list[7] == "X": 
        print(colored(moves_list[7], "red"), end=" ")
    elif moves_list[7] == "O":
        print(colored(moves_list[7], "yellow"), end=" ")
    else:
        print(colored(moves_list[7], "dark_grey"), end=" ")

    print("| ", end="")
    if moves_list[8] == "X": 
        print(colored(moves_list[8], "red"), end=" |\n")
    elif moves_list[8] == "O":
        print(colored(moves_list[8], "yellow"), end=" |\n")
    else:
        print(colored(moves_list[8], "dark_grey"), end=" |\n")

    
    print ("-------------")










    