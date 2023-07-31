Juego ta-te-ti

1) Muestra el tablero numerado del 1 al 9 
2) Pedir jugada al usuario
3) Mostrar el tablero con la jugada del usuario y los libres quedan numerados
4) Muestro el tablero con la jugada de la compu y los libres quedan numerados
5) Chequeo si se terminó el juego
6) Si no se terminó vuelvo al ciclo de jugar usuario y compu
7) Si se terminó muestro resultados y pregunto si quiere volver a jugar
8) Si quiere volver a jugar reinicia el juego, si no, salir


Tablero
-------------
| 0 | 1 | 2 |
-------------
| 3 | 4 | 5 |
-------------
| 6 | 7 | 8 |
-------------

Condiciones para que gane el usuario

Filas 
jugadas[0] == "X" and jugadas[1] == "X" and jugadas[2] == "X"
jugadas[3] == "X" and jugadas[4] == "X" and jugadas[5] == "X"
jugadas[6] == "X" and jugadas[7] == "X" and jugadas[8] == "X"

Columnas 
jugadas[0] == "X" and jugadas[3] == "X" and jugadas[6] == "X"
jugadas[1] == "X" and jugadas[4] == "X" and jugadas[7] == "X"
jugadas[2] == "X" and jugadas[5] == "X" and jugadas[8] == "X"

Diagonales
jugadas[0] == "X" and jugadas[4] == "X" and jugadas[8] == "X"
jugadas[2] == "X" and jugadas[4] == "X" and jugadas[6] == "X"


Condiciones para que gane la compu

Filas 
jugadas[0] == "O" and jugadas[1] == "O" and jugadas[2] == "O"
jugadas[3] == "O" and jugadas[4] == "O" and jugadas[5] == "O"
jugadas[6] == "O" and jugadas[7] == "O" and jugadas[8] == "O"

Columnas 
jugadas[0] == "O" and jugadas[3] == "O" and jugadas[6] == "O"
jugadas[1] == "O" and jugadas[4] == "O" and jugadas[7] == "O"
jugadas[2] == "O" and jugadas[5] == "O" and jugadas[8] == "O"

Diagonales
jugadas[0] == "O" and jugadas[4] == "O" and jugadas[8] == "O"
jugadas[2] == "O" and jugadas[4] == "O" and jugadas[6] == "O"


Niveles de dificultad:
Nivel 1 (Facil): La compu no revisa las jugadas del usuario, solamente elige un valor al azar para completar
una celda vacía.

Nivel 2 (Intermedio): La compu revisa si el usuario está por completar una línea cuando ya tiene 2 "X" y solo le falta una 
celda para ganar. Si detecta esta situación juega en la celda que le falta al usuario antes de completar la línea.

Combinaciones a revisar para mitigar la situación:

---------------------------------------------------   Filas   -------------------------------------------
 

jugadas[1] == "X" and jugadas[2] == "X" -> La compu juega 0                    
jugadas[0] == "X" and jugadas[2] == "X" -> La compu juega 1                   
jugadas[0] == "X" and jugadas[1] == "X" -> La compu juega 2                   
                                                                                                            
-------------   -------------   -------------                           
|   | 1 | 2 |   | 0 |   | 2 |   | 0 | 1 |   |                          
-------------   -------------   -------------                          
|   |   |   |   |   |   |   |   |   |   |   |                          
-------------   -------------   -------------                          
|   |   |   |   |   |   |   |   |   |   |   |                          
-------------   -------------   -------------                          
 


                                    
jugadas[4] == "X" and jugadas[5] == "X" -> La compu juega 3
jugadas[3] == "X" and jugadas[5] == "X" -> La compu juega 4
jugadas[3] == "X" and jugadas[4] == "X" -> La compu juega 5

-------------   -------------   -------------   
|   |   |   |   |   |   |   |   |   |   |   |   
-------------   -------------   -------------   
|   | 4 | 5 |   | 3 |   | 5 |   | 3 | 4 |   |   
-------------   -------------   -------------   
|   |   |   |   |   |   |   |   |   |   |   |   
-------------   -------------   -------------  





jugadas[7] == "X" and jugadas[8] == "X" -> La compu juega 6                                                                   
jugadas[6] == "X" and jugadas[8] == "X" -> La compu juega 7                               
jugadas[6] == "X" and jugadas[7] == "X" -> La compu juega 8

-------------   -------------   -------------   
|   |   |   |   |   |   |   |   |   |   |   |   
-------------   -------------   -------------   
|   |   |   |   |   |   |   |   |   |   |   |   
-------------   -------------   -------------   
|   | 7 | 8 |   | 6 |   | 8 |   | 6 | 7 |   |   
-------------   -------------   -------------  

-----------------------------------------------    Fin filas    ------------------------------------------------


---------------------------------------------------   Columnas   -------------------------------------------
jugadas[3] == "X" and jugadas[6] == "X" -> La compu juega 0                                                                   
jugadas[0] == "X" and jugadas[6] == "X" -> La compu juega 3                               
jugadas[0] == "X" and jugadas[3] == "X" -> La compu juega 6

-------------   -------------   -------------   
|   |   |   |   | 0 |   |   |   | 0 |   |   |   
-------------   -------------   -------------   
| 3 |   |   |   |   |   |   |   | 3 |   |   |   
-------------   -------------   -------------   
| 6 |   |   |   | 6 |   |   |   |   |   |   |   
-------------   -------------   -------------  

                                    


jugadas[4] == "X" and jugadas[7] == "X" -> La compu juega 1                                                                   
jugadas[1] == "X" and jugadas[7] == "X" -> La compu juega 4                               
jugadas[1] == "X" and jugadas[4] == "X" -> La compu juega 7

-------------   -------------   -------------   
|   |   |   |   |   | 1 |   |   |   | 1 |   |   
-------------   -------------   -------------   
|   | 4 |   |   |   |   |   |   |   | 4 |   |   
-------------   -------------   -------------   
|   | 7 |   |   |   | 7 |   |   |   |   |   |   
-------------   -------------   -------------  

                                    


jugadas[5] == "X" and jugadas[8] == "X" -> La compu juega 2                                                                   
jugadas[2] == "X" and jugadas[8] == "X" -> La compu juega 5                               
jugadas[2] == "X" and jugadas[5] == "X" -> La compu juega 8


-------------   -------------   -------------   
|   |   |   |   |   |   | 2 |   |   |   | 2 |   
-------------   -------------   -------------   
|   |   | 5 |   |   |   |   |   |   |   | 5 |   
-------------   -------------   -------------   
|   |   | 8 |   |   |   | 8 |   |   |   |   |   
-------------   -------------   -------------  
                                    
--------------------------------------------------  Fin columnas   ---------------------------------------------------


---------------------------------------------------   Diagonales   -------------------------------------------
  
jugadas[4] == "X" and jugadas[8] == "X" -> La compu juega 0                                                                   
jugadas[0] == "X" and jugadas[8] == "X" -> La compu juega 4                               
jugadas[0] == "X" and jugadas[4] == "X" -> La compu juega 8

-------------   -------------   -------------   
|   |   |   |   | 0 |   |   |   | 0 |   |   |   
-------------   -------------   -------------   
|   | 4 |   |   |   |   |   |   |   | 4 |   |   
-------------   -------------   -------------   
|   |   | 8 |   |   |   | 8 |   |   |   |   |   
-------------   -------------   -------------  

                                    


jugadas[6] == "X" and jugadas[4] == "X" -> La compu juega 2                                                                   
jugadas[6] == "X" and jugadas[2] == "X" -> La compu juega 4                               
jugadas[2] == "X" and jugadas[4] == "X" -> La compu juega 6
-------------   -------------   -------------   
|   |   |   |   |   |   | 2 |   |   |   | 2 |   
-------------   -------------   -------------   
|   | 4 |   |   |   |   |   |   |   | 4 |   |   
-------------   -------------   -------------   
| 6 |   |   |   | 6 |   |   |   |   |   |   |   
-------------   -------------   -------------  
                                    
----------------------------------------------   Fin diagonales   -------------------------------------------------


*******************************************************************************************************************
                                                  PSEUDOCÓDIGO
*******************************************************************************************************************


* Genero la lista de jugadas [0,1,2,3,4,5,6,7,8]


* Muestro el tablero
imprimo linea superior primer fila
imprimo  | jugadas[0] | jugadas[1] | jugadas[2] |
imprimo linea superior segunda fila
imprimo  | jugadas[3] | jugadas[4] | jugadas[5] |
imprimo linea superior tercera fila
imprimo  | jugadas[6] | jugadas[7] | jugadas[8] |
imprimo linea inferior del tablero


* Juega el usuario
abro bucle infinito (usuario)
    pido jugada al usuario(el usuario juega con X)
    ¿El nro de celda es mayor a 9, menor a 0 o no es un número?
        imprimo "Jugada inválida, vuelve a intentar"
        reinicio el bucle usuario
    no:
        ¿hay una X o un O en la celda que el usuario jugó?
            imprimo "no se puede repetir la jugada, vuelve a intentar"
            reinicio el bucle usuario
    asigno X al número de celda jugado por el usuario
    salgo del bucle usuario
valido si hay algún ganador


* Juega la compu
abro bucle infinito (compu)
    ¿nivel 1 (facil)?
        genero un random del 1 al 9
        ¿hay una X o un O en la celda que jugó la compu?
            no se puede jugar una celda ya jugada, reinicio el bucle compu
        asigno O al número de celda jugado por el usuario
    ¿nivel 2(intermedio)?
        if (alguna condición de control)
            asigno O a la celda que le falta al usuario para ganar
        no: 
            genero un random del 1 al 9
            ¿hay una X o un O en la celda que jugó la compu?
                no se puede jugar una celda ya jugada, reinicio el bucle compu
            asigno O al número de celda jugado por el usuario

    salgo del bucle compu
valido si hay algún ganador


* Validación de ganador
recorro la lista de jugadas
    ¿Existe alguna combinación que haga ganador al usuario?
        muestro mensaje "Ganador usuario"
    ¿Existe alguna combinación que haga ganador a la compu?
        muestro mensaje "Ganador la compu"


* Final del juego
imprimo "Ganador usuario/compu"
¿Volver a jugar?
    reinicio el juego
no:
    salir del juego    





