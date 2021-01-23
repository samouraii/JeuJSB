
class Main:

    def afficher_les_options(self):
        print("Bienvenue dans mon jeu")
        print("Voici toutes les options du jeu:")
        print("1) Récolter des ressources")
        print("2) Attaquer un monstre")
        print("3) Parler à une personne")

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

    def main(self):
        
        self.afficher_les_options()
        option = int(self.input_option())
        while( option < 1 or option > 3):
            self.afficher_les_options()
            option = int(self.input_option())
        self.action(option)
        
        
if __name__ == "__main__" :
    initmain = Main()
    initmain.main()
        
