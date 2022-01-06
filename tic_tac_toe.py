import os;
import keyboard;
import pyautogui as pa;
import random;
def main():
    s=True
    counter_time = 0
    #array with nine elements/creo una lista de nueve elementos
    os.system('cls')
    positions=[1,2,3,4,5,6,7,8,9]
    player1 = "X"
    player2 = "O"
    
    print("Tic-Tac-Toe Game")
    interface(positions)
    print()
    print()
    while counter_time < 10:
        position_picked_player1 = int(input("Player 1 Choice the position to draw your Simbol :"))
        print("Positions should be betwen 1 and 9")
        os.system('crtl+ñ')
        #This function call to Player_one to pick position
        player_one(positions, position_picked_player1)
        player_two()
        
        
            
    print()
    print()
def player_one(positions, position_picked_ply1):
    if (position_picked_ply1 > 0 and position_picked_ply1 < 10):
                positions[position_picked_ply1-1]="X"
                interface(positions)
                
                    
def player_two():
    pass

def interface(position):
    print()
    print()
    for i in position:
        #set separator "|"
        print(i, end =" | ")
        if i == 3:
            #print next line down with that simbols
            print("\n - + - + -")
        elif i == 6:
            #next line down
            print("\n- + - + -")
        

if __name__== "__main__":
    main()