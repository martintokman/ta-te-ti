from termcolor import colored


def mostrar_tablero(lista_jugadas):
    """
    Imprime en consola el tablero con las jugadas realizadas y las celdas disponibles para jugar.
    Las jugadas del usuario se muestran en color rojo.
    Las jugadas de la compu se muestran en color amarillo.

    Args:
        lista_jugadas (list): Lista de jugadas y celdas disponibles para jugar.
    """
    
    for i in range(2): print("")
    print ("-------------")
    
    #agrego colores a las jugadas, rojo al usuario y amarillo a la compu
    #fila1
    print("| ", end="")
    if lista_jugadas[0] == "X": 
        print(colored(lista_jugadas[0], "red"), end=" ")
    elif lista_jugadas[0] == "O":
        print(colored(lista_jugadas[0], "yellow"), end=" ")
    else:
        print(colored(lista_jugadas[0], "dark_grey"), end=" ")

    
    
    print("| ", end="")
    if lista_jugadas[1] == "X": 
        print(colored(lista_jugadas[1], "red"), end=" ")
    elif lista_jugadas[1] == "O":
        print(colored(lista_jugadas[1], "yellow"), end=" ")
    else:
        print(colored(lista_jugadas[1], "dark_grey"), end=" ")

    print("| ", end="")
    if lista_jugadas[2] == "X": 
        print(colored(lista_jugadas[2], "red"), end=" |\n")
    elif lista_jugadas[2] == "O":
        print(colored(lista_jugadas[2], "yellow"), end=" |\n")
    else:
        print(colored(lista_jugadas[2], "dark_grey"), end=" |\n")
        

    
    print ("-------------")


    #fila 2
    print("| ", end="")
    if lista_jugadas[3] == "X": 
        print(colored(lista_jugadas[3], "red"), end=" ")
    elif lista_jugadas[3] == "O":
        print(colored(lista_jugadas[3], "yellow"), end=" ")
    else:
        print(colored(lista_jugadas[3], "dark_grey"), end=" ")
    
    
    print("| ", end="")
    if lista_jugadas[4] == "X": 
        print(colored(lista_jugadas[4], "red"), end=" ")
    elif lista_jugadas[4] == "O":
        print(colored(lista_jugadas[4], "yellow"), end=" ")
    else:
        print(colored(lista_jugadas[4], "dark_grey"), end=" ")

    print("| ", end="")
    if lista_jugadas[5] == "X": 
        print(colored(lista_jugadas[5], "red"), end=" |\n")
    elif lista_jugadas[5] == "O":
        print(colored(lista_jugadas[5], "yellow"), end=" |\n")
    else:
        print(colored(lista_jugadas[5], "dark_grey"), end=" |\n")

    
    print ("-------------")


    #fila 3
    print("| ", end="")
    if lista_jugadas[6] == "X": 
        print(colored(lista_jugadas[6], "red"), end=" ")
    elif lista_jugadas[6] == "O":
        print(colored(lista_jugadas[6], "yellow"), end=" ")
    else:
        print(colored(lista_jugadas[6], "dark_grey"), end=" ")
    
    
    print("| ", end="")
    if lista_jugadas[7] == "X": 
        print(colored(lista_jugadas[7], "red"), end=" ")
    elif lista_jugadas[7] == "O":
        print(colored(lista_jugadas[7], "yellow"), end=" ")
    else:
        print(colored(lista_jugadas[7], "dark_grey"), end=" ")

    print("| ", end="")
    if lista_jugadas[8] == "X": 
        print(colored(lista_jugadas[8], "red"), end=" |\n")
    elif lista_jugadas[8] == "O":
        print(colored(lista_jugadas[8], "yellow"), end=" |\n")
    else:
        print(colored(lista_jugadas[8], "dark_grey"), end=" |\n")

    
    print ("-------------")










    