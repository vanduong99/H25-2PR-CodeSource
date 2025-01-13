from abc import ABC, abstractmethod


class Forme(ABC):
    @abstractmethod
    def aire(self):
        """Calcule l'aire de la forme"""
        pass

    @abstractmethod
    def perimetre(self):
        """Calcule le périmètre de la forme"""
        pass


# herite de forme pour un rectangle
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)


# herite de forme pour un cercle
class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return 3.14159 * self.rayon ** 2

    def perimetre(self):
        return 2 * 3.14159 * self.rayon


# Exemple d'utilisation
rectangle = Rectangle(5, 3)


cercle = Cercle(4)
