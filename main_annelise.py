#from Board import *
#from player import *



if __name__=="__main__":
    colonne=7
    cell=6
    l=[[" " for _ in range(colonne)] for _ in range(cell) ]
    char=" "
    
    
    """ print("+---+---+---+---+---+---+---+")
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

    print() """

    agagne=0
    count=0
    while agagne != 1 and count <= 41 :

        choix=int(input("Entrer un numero de colonne pour inserer le pion :"))
        
        if count % 2 == 0:
            no=1
            symbole="X"
        else:
            no=2
            symbole="O"

        bas = cell-1
        while l[bas][choix-1] != " ":
            bas -= 1

        l[bas][choix-1]=symbole

        msg=""
        for j in range(colonne):
            msg += f'  '+str(j+1)+' '
        msg += f'\n'
        for j in range(colonne):
            msg += f'+---'
        msg += f'+\n'
        for i in range(cell):
            for j in range(colonne):
                msg += f'| {l[i][j]} '
            msg += f'|\n'
            for j in range(colonne):
                msg += f'+---'
            msg += f'+\n'
        print(msg)

        #verifie si 4 symboles alignes
        for j in range(cell):
            for i in range(colonne-4):
                if l[j][i:i+4] == [symbole for _ in range(4)]:
                    print("Joueur ",no,"a gagne")
                    agagne=1
        
        for j in range(colonne):
            for i in range(cell-3):
                dummy=[l[i][j],l[i+1][j],l[i+2][j],l[i+3][j]]
                if dummy == [symbole for _ in range(4)]:
                    print("Joueur ",no,"a gagne")
                    agagne=1
        
        for j in range(colonne-3):
            for i in range(cell-3):
                dummy=[l[i][j],l[i+1][j+1],l[i+2][j+2],l[i+3][j+3]]
                if dummy == [symbole for _ in range(4)]:
                    print("Joueur ",no,"a gagne")
                    agagne=1
        
        for j in range(colonne-1,colonne-5,-1):
            for i in range(cell-3):
                dummy=[l[i][j],l[i+1][j-1],l[i+2][j-2],l[i+3][j-3]]
                if dummy == [symbole for _ in range(4)]:
                    print("Joueur ",no,"a gagne")
                    agagne=1

        count+=1
        if count == 42:
            print("Match nul !")
            agagne=1