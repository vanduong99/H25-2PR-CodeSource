# Personne [nom, prenom] classe abstraite
# class abstraite permet de crée un nouveau type
# on peu pas créer un objet personne
# une classe abstraite doit contenir au moin une methode abstraite
# une classe abstraite ne doit pas etre instancié (on ne crée d'objet )
# Sert comme moule pour les sous-classes
from abc import ABC, abstractmethod
"""pour qu'une class soit abstraite : herite de ABC et doit avoir une 
methode abstraite qui sera definie dans le sous-classe"""
class Personne(ABC):
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def __str__(self):
        return f'{self.nom} {self.prenom}'
    @abstractmethod
    def envoyerMail(self): # Methode polymorphe
        """méthode abstraite doit etre implementée dans les classe enfants"""
        pass

# classe en enfant Employee qui hérite de la classe parent Personne
class Employee(Personne):
    def __init__(self, nom, prenom, numEmployee): # constructeur
        super().__init__(nom, prenom) # appeler le constructeur du parent
        self.numEmployee = numEmployee
    def __str__(self):
        return super().__str__() + str(self.numEmployee)
    def envoyerMail(self):
        print("== Mail Employee : Bonjour " + str(self.nom) + " " + str(self.prenom))

# class Etudiant hérite de Personne
class Etudiant(Personne):
    def __init__(self, nom, prenom, numEtudiant):
        super().__init__(nom, prenom)
        self.numEtudiant = numEtudiant
    def __str__(self):
        return super().__str__() + str(self.numEtudiant)

class Enseignant(Employee):
    def __init__(self, nom, prenom, numEmployee, departement):
        super().__init__(nom, prenom,numEmployee)
        self.departement = departement
    def __str__(self):
        return super().__str__() + str(self.departement)

class Visiteur(Personne):
    def __init__(self, nom, prenom, identification):
        super().__init__(nom, prenom)
        self.identification = identification
    def __str__(self):
        return super().__str__() + str(self.identification)

# Polymorphisme :: grace à l'heritage on est capable de ne pas se soucier du type de l'objet
em1 = Employee("rouss", "jean", "EM123456")
em1.envoyerMail()

e1 = Enseignant("alain","Lefebre","EN2345","info")
e1.envoyerMail()

# avoir des objets de type different dans
maListe = [em1, e1]
for e in maListe:
    e.envoyerMail()