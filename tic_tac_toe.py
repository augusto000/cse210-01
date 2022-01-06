import os;
def main():
    #creo una lista de nueve elementos
    elementos=[1,2,3,4,5,6,7,8,9]
    os.system('cls')
    interfaz(elementos)
    print()
    print()
    
def interfaz(elements):
    for i in elements:
        #crear separador "|"
        print(i, end =" | ")
        if i == 3:
            print("\n - + - + -")
        elif i == 6:
            print("\n")
        elif i==9:
            print("\n - + - + -")

if __name__== "__main__":
    main()