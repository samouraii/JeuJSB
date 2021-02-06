import carte
class Personne:
    def __init__(self, pos, nom):
        self.pos = pos
        self.nom = nom
        
    def deplacer(self, limite_carte_x, limite_carte_y):
        print("dans quel direction voulez vous allez?")
        print("la limite en x:", limite_carte_x, "la limite en y",limite_carte_y) 
        clavier = input("Quel direction (haut,Bas,droite,gauche)?")
        if clavier == "haut":
            self.pos = (self.pos[0] + 1,self.pos[1])
        elif clavier == "bas":
            self.pos = (self.pos[0] -1,self.pos[1])
        elif clavier == "droite":
            self.pos = (self.pos[0], self.pos[1]+1)
        else:
            self.pos = (self.pos[0] ,self.pos[1] -1)
        print("tu es sur la carte:", self.pos)
    
class Main:

    def __init__(self, perso):
        self.perso = perso
        self.carte = carte.Map()

    def afficher_les_options(self):
        print("Bienvenue dans mon jeu " +self.perso.nom)
        print("Voici toutes les options du jeu DODA:")
        print("1) Récolter des ressources")
        print("2) Attaquer un monstre")
        print("3) Parler à une personne")
        print("4) Se déplacer ")

    def input_option(self):
        clavier = input("Quel option souhaites tu ?")
        return clavier
    
    def action(self, option):
        if(option == 1):
            print("Tu as récolté du bois")
        elif(option == 2):
            print("Tu as tué un monstre")
        elif(option == 3):
            print("Tu as parlé à ...")
        elif(option == 4):
            self.perso.deplacer(len(self.carte.carte),len(self.carte.carte[0]))
            self.carte.affichage_pos(self.perso.pos)

    def main(self):
        option = -1
        while(option != 0):
            self.afficher_les_options()
            option = int(self.input_option())
            while( option < 0 or option > 4):
                self.afficher_les_options()
                option = int(self.input_option())
            self.action(option)
        
        
if __name__ == "__main__" :
    personnage = Personne((0,0),"Adrien")
    initmain = Main(personnage)
    initmain.main()
        
