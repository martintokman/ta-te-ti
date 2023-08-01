import random

def jugada_compu(lista_jugadas, nivel):
    
    if nivel == 1: 
        while True:
            jugada_compu = random.randrange(0,9)
            if not isinstance(lista_jugadas[jugada_compu], int):
                continue
            else:
                lista_jugadas[jugada_compu] = "O"
                print(f"La compu jugó: {jugada_compu}")
                break
        
        return lista_jugadas
    
    else: #nivel = 2
        if lista_jugadas[1] == "X" and lista_jugadas[2] == "X" and lista_jugadas[0] == 1: 
            lista_jugadas[0] = "O" #La compu juega 0                    
            print("La compu jugó: 1")
        elif lista_jugadas[0] == "X" and lista_jugadas[2] == "X" and lista_jugadas[1] == 2: 
            lista_jugadas[1] = "O" #La compu juega 1 
            print("La compu jugó: 2")                  
        elif lista_jugadas[0] == "X" and lista_jugadas[1] == "X" and lista_jugadas[2] == 3:
            lista_jugadas[2] = "O" #La compu juega 2 
            print("La compu jugó: 3")
        elif lista_jugadas[4] == "X" and lista_jugadas[5] == "X" and lista_jugadas[3] == 4: 
            lista_jugadas[3] = "O" # compu juega 3
            print("La compu jugó: 4")
        elif lista_jugadas[3] == "X" and lista_jugadas[5] == "X" and lista_jugadas[4] == 5: 
            lista_jugadas[4] = "O" # compu juega 4
            print("La compu jugó: 5")
        elif lista_jugadas[3] == "X" and lista_jugadas[4] == "X" and lista_jugadas[5] == 6: 
            lista_jugadas[5] = "O" # compu juega 5
            print("La compu jugó: 6")
        elif lista_jugadas[7] == "X" and lista_jugadas[8] == "X" and lista_jugadas[6] == 7: 
            lista_jugadas[6] = "O" # compu juega 6 
            print("La compu jugó: 7")                                                                  
        elif lista_jugadas[6] == "X" and lista_jugadas[8] == "X" and lista_jugadas[7] == 8: 
            lista_jugadas[7] = "O" # compu juega 7                               
            print("La compu jugó: 8")
        elif lista_jugadas[6] == "X" and lista_jugadas[7] == "X" and lista_jugadas[8] == 9: 
            lista_jugadas[8] = "O" # compu juega 8
            print("La compu jugó: 9")
        elif lista_jugadas[3] == "X" and lista_jugadas[6] == "X" and lista_jugadas[0] == 1:
            lista_jugadas[0] = "O" # compu juega 0   
            print("La compu jugó: 1")                                                                
        elif lista_jugadas[0] == "X" and lista_jugadas[6] == "X" and lista_jugadas[3] == 4: 
            lista_jugadas[3] = "O" # compu juega 3
            print("La compu jugó: 4")                               
        elif lista_jugadas[0] == "X" and lista_jugadas[3] == "X" and lista_jugadas[6] == 7:
            lista_jugadas[6] = "O" # compu juega 6
            print("La compu jugó: 7")
        elif lista_jugadas[4] == "X" and lista_jugadas[7] == "X" and lista_jugadas[1] == 2: 
            lista_jugadas[1] = "O" # compu juega 1  
            print("La compu jugó: 2")                                                                 
        elif lista_jugadas[1] == "X" and lista_jugadas[7] == "X" and lista_jugadas[4] == 5: 
            lista_jugadas[4] = "O" # compu juega 4
            print("La compu jugó: 5")                               
        elif lista_jugadas[1] == "X" and lista_jugadas[4] == "X" and lista_jugadas[7] == 8: 
            lista_jugadas[7] = "O" # compu juega 7
            print("La compu jugó: 8")
        elif lista_jugadas[5] == "X" and lista_jugadas[8] == "X" and lista_jugadas[2] == 3: 
            lista_jugadas[2] = "O" # compu juega 2       
            print("La compu jugó: 3")                                                            
        elif lista_jugadas[2] == "X" and lista_jugadas[8] == "X" and lista_jugadas[5] == 6: 
            lista_jugadas[5] = "O" # compu juega 5
            print("La compu jugó: 6")                               
        elif lista_jugadas[2] == "X" and lista_jugadas[5] == "X" and lista_jugadas[8] == 9:
            lista_jugadas[8] = "O" # compu juega 8
            print("La compu jugó: 9")
        elif lista_jugadas[4] == "X" and lista_jugadas[8] == "X" and lista_jugadas[0] == 1: 
            lista_jugadas[0] = "O" # compu juega 0
            print("La compu jugó: 1")                                                                   
        elif lista_jugadas[0] == "X" and lista_jugadas[8] == "X" and lista_jugadas[4] == 5: 
            lista_jugadas[4] = "O" # compu juega 4   
            print("La compu jugó: 5")                            
        elif lista_jugadas[0] == "X" and lista_jugadas[4] == "X" and lista_jugadas[8] == 9: 
            lista_jugadas[8] = "O" # compu juega 8
            print("La compu jugó: 9")
        elif lista_jugadas[6] == "X" and lista_jugadas[4] == "X" and lista_jugadas[2] == 3:
            lista_jugadas[2] = "O" # compu juega 2   
            print("La compu jugó: 3")                                                                
        elif lista_jugadas[6] == "X" and lista_jugadas[2] == "X" and lista_jugadas[4] == 5: 
            lista_jugadas[4] = "O" # compu juega 4 
            print("La compu jugó: 5")                              
        elif lista_jugadas[2] == "X" and lista_jugadas[4] == "X" and lista_jugadas[6] == 7: 
            lista_jugadas[6] = "O" # compu juega 6
            print("La compu jugó: 7")
        else:
            while True:
                jugada_compu = random.randrange(0,9)
                if not isinstance(lista_jugadas[jugada_compu], int):
                    continue
                else:
                    lista_jugadas[jugada_compu] = "O"
                    print(f"La compu jugó: {jugada_compu}")
                    break
            
            return lista_jugadas
