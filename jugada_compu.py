import random

def jugada_compu(lista_jugadas):
    while True:
        jugada_compu = random.randrange(0,9)
        if not isinstance(lista_jugadas[jugada_compu], int):
            continue
        else:
            lista_jugadas[jugada_compu] = "O"
            print(f"La compu jugó: {jugada_compu}")
            break
    
    return lista_jugadas
