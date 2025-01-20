# coding: utf-8
class Calcul:
	def __init__(self):
		pass
	
	# ---Factorielle ------------
	def factorielle(self, n):
		j = 1
		for i in range(1, n + 1):
			j = j * i
		return j
	
	# ---Somme des n premiers nombres----
	def somme(self, n):
		j = 1
		for i in range(1, n + 1):
			j = j + i
		return j
	
	# ---Test primalité d'un nombre------------
	def testPrim(self, n):
		j = 0
		for i in range(1, n + 1):
			if (n % i == 0):
				j = j + 1
		if (j == 2):
			return True
		else:
			return False
	
	# ---Test primalité de deux nombres entiers------------
	def testprims(self, n, m):
		divCommun = 0
		for i in range(1, n + 1):
			if (n % i == 0 and m % i == 0):
				divCommun = divCommun + 1
		if divCommun == 1:
			print("Les nombres ", n, " et ", m, " sont premiers entre eux")
		else:
			print("Les nombres ", n, " et ", m, " ne sont pas premiers entre eux")
	
	# ---Table de multiplication-------------
	def tableMult(self, k):
		for i in range(1, 10):
			print(i, " x ", k, " = ", i * k)
	
	# ---Toutes les tables de multiplication des nombres 1, 2, .., 9
	def toutesLesTables(self):
		for k in range(1, 10):
			print("\nla table de multiplication de : ", k, " est : ")
			for i in range(1, 10):
				print(i, " x ", k, " = ", i * k)
	
	# ----- liste des diviseurs d'un entier
	def listDiv(self, n):
		# initialisation de la liste des diviseurs
		lDiv = []
		for i in range(1, n + 1):
			if (n % i == 0):
				lDiv.append(i)
			return lDiv
			
		# ------liste des diviseurs premiers d'un entier----------------
		# ------liste des diviseurs premiers d'un entier----------------
		
	def listDivPrim(self, n):
		# initialisation de la liste des diviseurs
		lDiv = []
		for i in range(1, n + 1):
			if (n % i == 0 and self.testPrim(i)):
				lDiv.append(i)
		return lDiv
		
# Exemple Instanciation
Cal = Calcul()
Cal.testprims(13, 7)
print("Liste des diviseurs de 18 : ", Cal.listDiv(18))
print("Liste des diviseurs premiers de 18 : ", Cal.listDivPrim(18))
Cal.toutesLesTables()


