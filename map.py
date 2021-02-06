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
    def affichage_pos(self, pos): #pos est un tuple (x,y)
        print(carte[pos[0]][pos[1]])




class ressource:

    def __init__(self):

        self.ressource = {"bois": 45, "eau":60}
    

    def addv(self, ressource, value):
        self.ressource[ressource] += value

    def getr(self,ressource):
        return self.ressource[ressource]


if __name__ == "__main__":
    res = ressource()
    print("bois",res.getr("bois"))
    print("eau", res.getr("eau"))
    res.addv("eau", -50)
    print("bois",res.getr("bois"))
    print("eau", res.getr("eau"))
