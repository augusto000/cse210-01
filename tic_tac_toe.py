#***************************************************************
#Assignament: Programming with Class -cse210-w02
#Author: Augusto Achá
#***************************************************************
'''
Requirements
Your program must also meet the following requirements.

The program must have a comment with assignment and author names. DONE
The program must have at least one if/then block.DONE
The program must have at least one while loop.DONE
The program must have more than one function.DONE
The program must have a function called main.DONE
'''
import os, random,time;

def main():
    os.system('cls')
              
    #interface()draw The Board / devuelve el tablero para empeza a jugar  
    interfa = interface()
    
    #Counters for each player's round 
    zx = 0
    zo = 0
    z=0
    winner = None
    s=True
    
    #while loop checks tree times gamming each one of the players
    while s and z<=9:           
        #ask for Input position Player 1
        x, zx, z = callInput_Player1_x(zx, z)
        
        if (x >= 1 and x <= 9): 
            #call to spot the position choosen of Player 1
            board = marco_x(interfa, x)
            #look for a winner    
            w=isWinner(board)
            if w==True:
                break
            else:
                if w ==None:
                    o, zo, z = callInput_Player2_o(zo, z)#####
                    #marco_o updates the position choosen at the board
                    inte_o = marco_o (board, o) 
                    print()
                    w=isWinner(board)
                    if w==True:
                        s=False
                        break
                    print()
                    print()
                else:
                    o, zo, z = callInput_Player2_o(zo, z)
                    #marco_o updates the position choosen at the board
                    inte_o = marco_o (board, o) 
                    print()
                    w=isWinner(board)
                    break
    s = input("Do you play once again ? Y/N :") 
    if s.lower() =="y":
        s = True
        main()
    else:
        print("**The game is over **")
        
            
def callInput_Player2_o(zo, z):
    #callInput_Players_o ask for the Player2 option
    o = int(input("Player 2 Input position to start playing a 'O'  :"))
    #o= random.randint(1, 9)
    zo = zo + 1
    z = z + 1
    return o, zo, z    

def callInput_Player1_x(zx, z):
    #Player 1 for the choosen position 
    x = int(input("Player 1 Input position to start playing a 'X' :"))
    #x= random.randint(1, 9)
    zx = zx +1
    z = z + 1
    return x, zx, z

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
    print("----------------------------------------------------------------------------------------------------------")
    tit="-----------------------------------------TIC - TAC - TOE ------------------------------------------"
    print("----------------------------------------------------------------------------------------------------------")
    print()
    print(tit)
    print()
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
    
    if board[0][0]==board[0][1]==board[0][2] \
       or board[1][0]==board[1][1]==board[1][2]\
       or board[2][0]== board[2][1]== board[2][2]:
           a=board[1][0]
           b=board[1][1]
           c=board[1][2]
           print("---------")
           print(a, b, c)
           time.sleep(6)
           
           if board[0][0]=="x" and board[0][1]=="x" and board[0][2]=="x"\
               or board[1][0]=="x" and board[1][1]=="x" and board[1][2]=="x"\
               or board[2][0] =="x" and board[2][1]=="x" and board[2][2]=="x":
               print(f"Congratulations X won !")
               return True
           else:
               print(f"Congratulations O won !")
               return True
               
    #looks for a Vertical Winner
    elif   board[0][0]==board[1][0]==board[2][0]\
        or board[0][1]==board[1][1]==board[2][1]\
        or board[0][2]==board[1][2]==board[2][2] :
            
                    
            if board[0][0]=="x" and board[1][0]=="x" and board[2][0]=="x"\
                or board[0][1]=="x" and board[1][1]=="x" and board[2][1]=="x"\
                or board[0][2]=="x" and board[1][2]=="x" and board[2][2]=="x" :
                print(f"Congratulations X won !")
                return True   
            else:
                print("Congratulations O won !")
                return True       
    
    #looks for Diagonal Winner
    elif board[0][0]==board[1][1]==board[2][2]\
       or board[0][2]==board[1][1]==board[2][0]:
           if board[0][0]=="o" and board[1][1]=="o" and board[2][2]=="o"\
               or board[0][2]=="o" and board[1][1]=="o" and board[2][0]=="o":
              print(f"Congratulations O won !")
              return True   
           else:
               print("Congratulations X won ! ")
               return True 
    #look if it is tie       
    elif isinstance(board[0][0] and board[0][1] and board[0][2]\
        and board[1][0] and board[1][1] and board[1][2]\
        and board[2][0] and board[2][1] and board[2][2], str):
                
        return None                 

if __name__== "__main__":
    main()