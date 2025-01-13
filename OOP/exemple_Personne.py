# Personne [nom, prenom],
# Héritage -- Un employee `est une` personne
# L'héritage n'est pas fait pour éviter la redondance dans le code
# Employee(Personne) [nom, prenom, numEmploye]
# Sans héritage -- Composision
# Employee [objet de type Personne, numEmployee]

# Définir un language, Objets de librairies

class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def __str__(self):
        return f'{self.nom} {self.prenom}'
    def envoyerMail(self): # Methode polymorphe
        print("== Mail : Bonjour " + str(self.nom) + " " +str(self.prenom))

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

p1 = Personne("alain","Lefebre")
p1.envoyerMail()

# avoir des objets de type different dans
maListe = [em1, p1]
for e in maListe:
    e.envoyerMail()