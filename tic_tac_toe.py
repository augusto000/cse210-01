import os;
def main():
   
    os.system('cls')
      
    #interface()draw The Board / devuelve el tablero para empeza a jugar
    interfa= interface()
    
    #Player 1 for the choosen position 
    posicion_escogida_x = int(input("Player 1 Input the choosen position :"))
    os.system('cls')
    #call to spot the position choosen of Player 1
    inte = marco_x(interfa, posicion_escogida_x)    
    
    #Player 2 input your choosen position
    posicion_escogida_o = int(input("Player 2 Input the choosen position :"))
    
    #call to spot the position choosen of Player 2
    marco_o(inte, posicion_escogida_o)
    
def marco_o(inte, posicion_escogida_o):
    #this function draw the board with the o position choosen from Player 2
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
    #this function draw the board with the x position choosen from Player 1
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
     #Draw the matriz with nine elements/dibujo una matriz de nueve elementos
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