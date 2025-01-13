class Voiture():
    def __init__(self): # construit des objets
        self.marque = ""
        self.modele = ""
        self.annee = ""
        self.__millage = 0 # attribut privé on (ne peut pas le modifier)
    def rouler_une_anne(self):
        self.__millage += 15000
    def set_millage(self, millage):
        self.__millage = millage
    def get_millage(self):
        return self.__millage
    def __str__(self):
        return "Voiture:[ " + str(self.marque) + "  " +  str(self.modele) + "  " +  str(self.annee) + "  "+ str(self.__millage) + " ] "
