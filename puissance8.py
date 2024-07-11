class Board: 

    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        self.statut = self.__str__()
    
    def display(self):
        print(self.statut)
        
    def __str__(self):
        number = 1
        msg = ""

        while number <= self.colonnes:
            msg += f"  "+str(number)+" "
            number+=1

        msg += "\n"

        count_tableau = 0
        
        while count_tableau < self.lignes:
            
            count = 0
           
            while  count <= self.colonnes -1:
                msg += "+---"
                count += 1
            msg += "+\n"

            count_tilt = 0
            while count_tilt <= self.colonnes-1:
                msg += "|   "
                count_tilt += 1
            msg += "|\n"

            count_tableau += 1

        count_fin =0

        while  count_fin <= self.colonnes -1:
                msg += "+---"
                count_fin += 1 
        msg +="+\n"

        return msg
    
class Pion(Board):

    def __init__(self, forme):
        self.forme = forme
        choise_player1 != choise_player2
    
    
    def __str__(self):
        msg = f"Choix de la ligne {len(self.lignes)} numero"
        for i in range(len(self.lignes)):
            msg += f"{self.lignes}"


        msg = f"Ce zoo contient {len(self.animals)} animaux :\n"
        for i in range(len(self.animals)):
            msg += f"{self.animals[i].nom}\n"
        return msg


if __name__ == "__main__":
    board = Board(7,6)
    board.display()
   

