def valida_ganador(lista_jugadas):
    #Condiciones para que gane el usuario
    #filas

    if lista_jugadas[0] == "X" and lista_jugadas[1] == "X" and lista_jugadas[2] == "X":
        ganador = "usuario"
    elif lista_jugadas[3] == "X" and lista_jugadas[4] == "X" and lista_jugadas[5] == "X":
        ganador = "usuario"
    elif lista_jugadas[6] == "X" and lista_jugadas[7] == "X" and lista_jugadas[8] == "X":
        ganador = "usuario"

    #Columnas 
    elif lista_jugadas[0] == "X" and lista_jugadas[3] == "X" and lista_jugadas[6] == "X":
        ganador = "usuario"
    elif lista_jugadas[1] == "X" and lista_jugadas[4] == "X" and lista_jugadas[7] == "X":
        ganador = "usuario"
    elif lista_jugadas[2] == "X" and lista_jugadas[5] == "X" and lista_jugadas[8] == "X":
        ganador = "usuario"

    #Diagonales
    elif lista_jugadas[0] == "X" and lista_jugadas[4] == "X" and lista_jugadas[8] == "X":
        ganador = "usuario"
    elif lista_jugadas[2] == "X" and lista_jugadas[4] == "X" and lista_jugadas[6] == "X":
        ganador = "usuario"


    #Condiciones para que gane la compu
    #Filas 
    elif lista_jugadas[0] == "O" and lista_jugadas[1] == "O" and lista_jugadas[2] == "O":
        ganador = "compu"
    elif lista_jugadas[3] == "O" and lista_jugadas[4] == "O" and lista_jugadas[5] == "O":
        ganador = "compu"
    elif lista_jugadas[6] == "O" and lista_jugadas[7] == "O" and lista_jugadas[8] == "O":
        ganador = "compu"

    #Columnas 
    elif lista_jugadas[0] == "O" and lista_jugadas[3] == "O" and lista_jugadas[6] == "O":
        ganador = "compu"
    elif lista_jugadas[1] == "O" and lista_jugadas[4] == "O" and lista_jugadas[7] == "O":
        ganador = "compu"
    elif lista_jugadas[2] == "O" and lista_jugadas[5] == "O" and lista_jugadas[8] == "O":
        ganador = "compu"

    #Diagonales
    elif lista_jugadas[0] == "O" and lista_jugadas[4] == "O" and lista_jugadas[8] == "O":
        ganador = "compu"
    elif lista_jugadas[2] == "O" and lista_jugadas[4] == "O" and lista_jugadas[6] == "O":
        ganador = "compu"
    
    else:
        ganador = "empate"

    return ganador