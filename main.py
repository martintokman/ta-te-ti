from mostrar_tablero import mostrar_tablero
from jugada_usuario import jugada_usuario
from valida_ganador import valida_ganador
from jugada_compu import jugada_compu
import sys

nivel = 2

while True: #abro bucle infinito (reinicio)

    lista_jugadas = [1,2,3,4,5,6,7,8,9]
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

        

        #muestro tablero
        mostrar_tablero(lista_jugadas)



        #valida ganador
        ganador = valida_ganador(lista_jugadas)
        if ganador == "usuario" or ganador == "compu" or ganador == "empate":
            break

        print("")
        print("**************************")
        print("**************************")
        print("")


        

    print(f"Ganador: {ganador}")

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
        print("Gracias por jugar!. Nos vemos pronto :)")
        exit()
