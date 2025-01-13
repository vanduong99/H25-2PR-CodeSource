# Vous utilisez deja des classes
massage1 = "une phrase"
liste = [3,4,5,6,-99] # creation de l'objet list / tuple / dict


print(massage1)
print("type de message1 : ",  type(massage1))
print("type de liste : ", type(liste))
print(liste)
liste.sort()
liste.append(100)
liste.append(-200)
liste.append(300)
print(liste)
liste.sort()
print(liste)


monTuple = (1,2,3,-3,5)
listeDepuisTuple = list(monTuple)
print(monTuple)
listeDepuisTuple.append(100)
listeDepuisTuple.sort()
monTuple = tuple(listeDepuisTuple)
print(listeDepuisTuple)

