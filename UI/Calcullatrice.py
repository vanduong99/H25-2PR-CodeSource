# application graphique avec pyQt6
# 0- install la librairie : pip install PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

# 1- créer un objet QApllication   app
# 2- créer un objet Qwidget       fen
# 3- appeler la méthode de l'objet QWidget fen.show()
# 4- appeler la méthode executer de l'objet app.exec()
# 5- autres objets : QPushButton, QLabel, QLineEdit

def action_add():
	# Increment the current number
	result = int(input1.text()) + int(input2.text())
	lbl3.setText(f"{result}")

def action_sub():
	result = int(input1.text()) - int(input2.text())
	lbl3.setText(f"{result}")

app = QApplication([])
fen = QWidget()

# parametre de fenetre
fen.setWindowTitle("Simple Calculatrice")
fen.setGeometry(300, 300, 400, 350)

# QLabel
lbl1 = QLabel(fen)
lbl1.setText("nb1 : ")
lbl1.setGeometry(10, 10, 50, 30)

lbl2 = QLabel(fen)
lbl2.setText("nb2 : ")
lbl2.setGeometry(10, 50, 50, 30)

lbl3 = QLabel(fen)
lbl3.setText(":::::::::: ")
lbl3.setGeometry(10, 100, 100, 30)

# QLineEdit
input1 = QLineEdit(fen)
input1.setGeometry(80, 10, 50, 30)
input2 = QLineEdit(fen)
input2.setGeometry(80, 50, 50, 30)

# QPushButton
btn_add = QPushButton(fen)
btn_add.setText("+")
btn_add.setGeometry(50, 150, 40, 30)
btn_add.clicked.connect(action_add)

btn_sub = QPushButton(fen)
btn_sub.setText("_")
btn_sub.setGeometry(10, 150, 40, 30)
btn_sub.clicked.connect(action_sub)

fen.show()
app.exec()