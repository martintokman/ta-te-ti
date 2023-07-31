from mostrar_tablero import mostrar_tablero
from jugada_usuario import jugada_usuario
from valida_ganador import valida_ganador

lista_jugadas = [1,2,3,4,5,6,7,8,9]
mostrar_tablero(lista_jugadas)

jugada_usuario(lista_jugadas)

mostrar_tablero(lista_jugadas)

ganador = valida_ganador(lista_jugadas)
print(ganador)


