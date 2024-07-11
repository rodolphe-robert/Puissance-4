class player:

    def __init__(self,nom:str) -> None:
        self.nom=nom
    
    def display(self):
        print(self.nom)