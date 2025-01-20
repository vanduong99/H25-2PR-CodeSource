# coding: utf-8
class Rectangle:
	def __init__(self, longueur, largeur):
		self.longueur = longueur
		self.largeur = largeur
	
	# Méthode qui calcul le périmètre
	def Perimetre(self):
		return 2 * (self.longueur + self.largeur)
	
	# Méthode qui calcul la surface
	def Surface(self):
		return self.longueur * self.largeur

#Rectangle is super class de Paralllepidede
class Parallelepipede(Rectangle):
	def __init__(self, longueur, largeur, hauteur):
		Rectangle.__init__(self, longueur, largeur)
		self.hauteur = hauteur
	
	# méthode qui calcul le volume
	def Volume(self):
		return self.longueur * self.largeur * self.hauteur


monRectangle = Rectangle(7, 5)
monParallelepipede = Parallelepipede(7, 5, 2)
print("Le périmètre de mon rectangle est : ", monRectangle.Perimetre())
print("La surface de mon rectangle est : ", monRectangle.Surface())
print("Le volume de mon parallelepipede est : ", monParallelepipede.Volume())

