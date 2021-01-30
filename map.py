class Cellule:

    def __init__(self,posX,posY):
        self.posX = posX
        self.posY = posY
    def __str__(self):
        return "vous êtes en: ("+self.posX +","+ self.posY +")"
        
class Map:
    carte = [[Cellule(0,0), Cellule(0,1)],
            [ Cellule(1,0), Cellule(1,1)]
        ]

    







    
