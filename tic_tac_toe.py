import os, random,time;
def main():
    os.system('cls')
              
    #interface()draw The Board / devuelve el tablero para empeza a jugar  
    interfa = interface()
    
    #Counters for each player's round 
    zx = 0
    zo = 0
    winner = None
    
    #while loop checks tree times gamming each one of the players
    while zo <= 2 :
           
        #ask for Input position Player 1
        x, zx = callInput_Player1_x(zx)
        if (x >= 1 and x <= 9): 
            #call to spot the position choosen of Player 1
            board = marco_x(interfa, x)
            #look for a winner    
            w=isWinner(board)
            if w==True:
                break
            else:
                o, zo = callInput_Player2_o(zo)
                #marco_o updates the position choosen at the board
                inte_o = marco_o (board, o) 
                print()
                w=isWinner(board)
    
    #winner_o(inte_o)         
    s = input("Do you play once again ? Y/N :") 
    if s.lower() =="y":
        op = True
        print()
        main()
        
    else:
        print("Thank you!")         
            
def callInput_Player2_o(zo):
    #callInput_Players_o ask for the Player2 option
    o = int(input("Player 2 Input position to draw a 'O'  :"))
    #o= random.randint(1, 9)
    zo = zo + 1
    return o, zo    

def callInput_Player1_x(zx):
    #Player 1 for the choosen position 
    x = int(input("Player 1 Input position to draw a 'X' :"))
    #x= random.randint(1, 9)
    zx = zx +1
    return x, zx

def marco_o(inte, posicion_escogida_o):
    print()
    #marco_o updates the position 'o' choosen at the board
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
    #marco_x updates the position 'x' choosen at the board
    print()
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
    positions=[
              [1,2,3],
              [4,5,6],
              [7,8,9]        
    ]
    
    for i in positions:
        for elemento in i:
            print(elemento, end=" ")
        print(sep="\n")
        print("-+-+-") 
    return positions  

def isWinner(board):
    #looks for Horizotal Winner
    
    if board[0][0] == board[0][1] == board[0][2] \
       or board[1][0]== board[1][1] == board[1][2]\
       or board[2][0]== board[2][1]== board[2][2]:
           if board[0][0]=="x" or board[1][0]=="x" or board[2][0]=="x":
               winner = board[0][0]
               print(f"The Winner is X {board[0][0]} Horizontal")
               return True
           else:
               print(f"The Winner is {board[0][0]} Horizontal")
               return True
               
    #looks for a Vertical Winner
    elif board[0][0]==board[1][0]==board[2][0]\
        or board[0][1]==board[1][1]==board[2][1]\
        or board[0][2]==board[1][2]==board[2][2] :
        if board[0][0]=="x" or board[0][1]=="x"or board[0][2]=="x":
            print(f"The Winner is X {board[0][2]}Vertical")
            return True   
        else:
            print("The Winner is O Vertical")
            return True       
    
    #looks for Diagonal Winner
    elif board[0][0]==board[1][1]==board[2][2]\
       or board[0][2]==board[1][1]==board[2][0]:
           if board[0][0]=="x"  or board[2][0]=="x":
              print(f"The Winner is X Diagonal")
              return True   
           else:
               print("The Winner is O Diagonal ")
               return True          

if __name__== "__main__":
    main()