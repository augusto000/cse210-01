import os;
def main():
    s=True
    #array with nine elements/creo una lista de nueve elementos
    os.system('cls')
    positions=[1,2,3,4,5,6,7,8,9]
    player1 = "X"
    player2 = "O"
    interface(positions)
    position_picked_player1 = int(input("Player 1 Choice the position to draw your Simbol :"))
    print("Positions should be betwen 1 and 9")
    if (position_picked_player1 > 0 and position_picked_player1 < 10):
            positions[position_picked_player1-1]="X"
            interface(positions)
            
    print()
    print()
    
def interface(position):
    for i in position:
        #set separator "|"
        print(i, end =" | ")
        if i == 3:
            #print next line down with that simbols
            print("\n - + - + -")
        elif i == 6:
            #next line down
            print("\n- + - + -")
        elif i==9:
            #print next line down with that simbols
            print("\n - + - + -")

if __name__== "__main__":
    main()