print("+---+---+---+---+---+---+---+---+")
print("\n")

i=0
while i<7:
     print(i)
     i+=1
count_tableau = 0
ligne = 8
while count_tableau < ligne:
    
    count = 0
    colonne=6
    while  count <= colonne -1:
        print("+---",end="")
        count += 1
    print("+")

    count_tilt = 0
    while count_tilt <= colonne-1:
        print("|   ", end="")
        count_tilt += 1
    print("|")

    count_tableau += 1

count_fin =0
while  count_fin <= colonne -1:
        print("+---",end="")
        count_fin += 1 
print("+")


print("\n")
