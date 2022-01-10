import os;
def main():
    os.system('cls')
    s_x = True
    s_o = True
           
    #os.system('cls')
    #interface()draw The Board / devuelve el tablero para empeza a jugar  
    interfa=interface()
    
    x = callInput_Player1_x()
    
    if (x >= 1 and x <= 9): 
        #call to spot the position choosen of Player 1
        inte_x = marco_x(interfa, x)
        o = callInput_Player2_o()
        inte_o = marco_o (inte_x, o) 
        print()
            
def callInput_Player2_o():
    o = int(input("Player 2 Input the choosen position :"))
    return o    

def callInput_Player1_x():
    #Player 1 for the choosen position 
    x = int(input("Player 1 Input the choosen position :"))
    return x

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

def marco_x(interf, posicion_escogida_x):
    #this function draw the board with the x position choosen from Player 1
    for i in range(3):
        for j in range(3):
            if interf[i][j] == posicion_escogida_x:
                interf[i][j] = "x"
                print(interf[i][j], end = " ")
            else:
                print(interf[i][j], end = " ")
                        
        print(sep = "\n")
    return interf        

        
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