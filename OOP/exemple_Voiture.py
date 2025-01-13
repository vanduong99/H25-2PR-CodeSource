from Voiture import Voiture

marque1 = "Mercedes"
modele1 = "C300"
annee1 = "2020"

marque2 = "toyota"
modele2 = "Yaris"
annee2 = "2000"


v1 = Voiture()
v1.marque = marque1
v1.modele = modele1
v1.annee = annee1
print(v1)
v2 = Voiture()
v2.marque = marque2
v2.modele = modele2
v2.annee = annee2
v2.rouler_une_anne()
v2.set_millage(-8000) # moi fou ... malhonnete ...
print(v2)

liste = [v1, v2]
for i in liste:
    print(i)