from mostrar_tablero import mostrar_tablero
from jugada_usuario import jugada_usuario
from valida_ganador import valida_ganador
from jugada_compu import jugada_compu
import sys, os
from colorama import Fore


nivel = 2

while True: #abro bucle infinito (reinicio)

    lista_jugadas = [1,2,3,4,5,6,7,8,9]

    os.system("clear")

    mostrar_tablero(lista_jugadas)

    while True: #abro bucle infinito (juego)
        
        #juega el usuario
        jugada_usuario(lista_jugadas)

        #muestro tablero
        mostrar_tablero(lista_jugadas)


        #valida ganador
        ganador = valida_ganador(lista_jugadas)
        if ganador == "usuario" or ganador == "compu" or ganador == "empate":
            break
 

        #jugada compu
        jugada_compu(lista_jugadas, nivel)

        os.system("clear")

        #muestro tablero
        mostrar_tablero(lista_jugadas)

        #valida ganador
        ganador = valida_ganador(lista_jugadas)
        if ganador == "usuario" or ganador == "compu" or ganador == "empate":
            break



    #juego terminado, muestro resultado
    os.system("clear")

    #muestro tablero
    mostrar_tablero(lista_jugadas)  

    print(f"\nGanador: {ganador}")

    while True:
        volver_a_jugar = input("Volver a jugar?: ")
        volver_a_jugar = volver_a_jugar.upper()
        if volver_a_jugar == "S" or volver_a_jugar == "N":
            break
        else:
            print("Opción no válida, vuelve a intentar.")
            continue
    
    if volver_a_jugar == "S":
        continue
    elif volver_a_jugar == "N":
        print("\nGracias por jugar!. Nos vemos pronto :)")
        exit()
