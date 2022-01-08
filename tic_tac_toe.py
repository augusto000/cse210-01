import os;
def main():
    s=True
    counter_time = 0
   
    os.system('cls')
      
    
       #interface() devuelve el tablero para empeza a jugar
    interfa= interface()
    #Luego de imprimir el tablero de juego, pido que ingrese la posicion
    #a escribir el simbolo x
    posicion_escogida_x = int(input("Jugador 1 Ingrese Posicion escogida "))
    inte = marco_x(interfa, posicion_escogida_x)    
    posicion_escogida_o = int(input("Jugador 2 Ingrese Posicion escogida :"))
    marco_o(inte, posicion_escogida_o)
    
def marco_o(inte, posicion_escogida_o):
    for i in range(3):
        for j in range(3):
            if inte[i][j] == posicion_escogida_o:
                inte[i][j] = "o"
                print(inte[i][j], end = " ")
            else:
                print(inte[i][j], end = " ")
        print(sep = "\n")
    return inte    
                
def marco_x(interfa, posicion_escogida_x):
    #inter is the positions picked at the interface
    for i in range(3):
        for j in range(3):
            if interfa[i][j] == posicion_escogida_x:
                interfa[i][j] = "x"
                print(interfa[i][j], end = " ")
            else:
                print(interfa[i][j], end = " ")
                        
        print(sep = "\n")
    return interfa        
        
def interface():
     #matriz with nine elements/creo una matriz de nueve elementos
    positions = [
                [1,2,3],
                [4,5,6],
                [7,8,9]        
                ]        
    for i in positions:
        for elemento in i:
            print(elemento, end=" ")
        print(sep="\n") 
    return positions       


if __name__== "__main__":
    main()