
#from Board import *
#from player import *

class Board:

    def __init__(self) :
         #self.row=row
         #self.cell=cell
         pass

    #row=6
    #cell=7
    def board(self,row,cell,choix,symbole):
        #saisie de Board

        l=[[" " for _ in range(row+1)] for _ in range(cell+1) ]
        char=" "
        i=0
        j=0
        count=0
        count_nbr=0
        count_choix=0

        #Loop to display number of cells

        while(count_nbr<cell):
            print(f"  {count_nbr} ",end='')
            count_nbr+=1
        print("")

        #Loop to display board
        while i<row:

            while(count<cell):
                print("+---",end='')
                count+=1
            print("+")
            count=0
            while(j<cell):
                if(count_choix==choix):
                    l[i][j]=symbole
                print(f'| {l[i][j]}',end=' ')
                count_choix+=1
                j+=1
            print("|")
            j=0
            i+=1

        while(count<cell):
            print("+---",end='')
            count+=1
        print("+")

        ###### remplissage ###





    '''''
    print("+---+---+---+---+---+---+---+")
    print(f'| {l[0][0]} | {l[0][1]} | {l[0][2]}  | {l[0][3]}  | {l[0][4]}  | {l[0][5]}  | {l[0][6]}  |')
    print("+---+---+---+---+---+---+---+")
    print(f'| {l[1][0]}  | {l[1][1]}  | {l[1][2]}  | {l[1][3]}  | {l[1][4]}  | {l[1][5]}  | {l[1][6]}  |')
    print("+---+---+---+---+---+---+---+")
    print(f'| {l[2][0]}  | {l[2][1]}  | {l[2][2]}  | {l[2][3]}  | {l[2][4]}  | {l[2][5]}  | {l[2][6]}  |')
    print("+---+---+---+---+---+---+---+")
    print(f'| {l[3][0]}  | {l[3][1]}  | {l[3][2]}  | {l[3][3]}  | {l[3][4]}  | {l[3][5]}  | {l[3][6]}  |')
    print("+---+---+---+---+---+---+---+")
    print(f'| {l[4][0]}  | {l[4][1]}  | {l[4][2]}  | {l[4][3]}  | {l[4][4]}  | {l[4][5]}  | {l[4][6]}  |')
    print("+---+---+---+---+---+---+---+")
    print(f'| {l[5][0]}  | {l[5][1]}  | {l[5][2]}  | {l[5][3]}  | {l[5][4]}  | {l[5][5]}  | {l[5][6]}  |')
    print("+---+---+---+---+---+---+---+")
    print(f'| {l[6][0]}  | {l[6][1]}  | {l[6][2]}  | {l[6][3]}  | {l[6][4]}  | {l[6][5]}  | {l[6][6]}  |')
    '''
    
    
