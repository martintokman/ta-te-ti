def jugada_usuario(lista_jugadas):
    while True:
        try:
            print("")
            jugada_usuario = int(input("Ingresa tu jugada (1-9):"))
            jugada_usuario -= 1
            if (jugada_usuario + 1) < 1 or (jugada_usuario + 1) > 9:
                print("Sólo números del 1 al 9, vuelve a intentar.")
                continue
            elif not isinstance(lista_jugadas[jugada_usuario], int):
                print("La celda ya fue jugada, vuelve a intentar.")
                continue
            else:
                break
        except ValueError:
            print("Sólo se permiten números, vuelve a intentar")

    lista_jugadas[jugada_usuario] = "X"
    return lista_jugadas