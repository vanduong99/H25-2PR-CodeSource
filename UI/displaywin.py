# application graphique avec pyQt6
# 0- install la librairie : pip install PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

# 1- créer un objet QApllication   app
# 2- créer un objet Qwidget       fen
# 3- appeler la méthode de l'objet QWidget fen.show()
# 4- appeler la méthode executer de l'objet app.exec()
# 5- autres objets : QPushButton, QLabel, QLineEdit

def action_ok():
    # print("ok")
    # print("Bonjour ", input1.text()," ", input2.text())
    lbl3.setText("Bonjour "+ input1.text()+" "+ input2.text())

def action_cancel():
    input1.setText("")
    input2.setText("")
    lbl3.setText("Message : ")

app = QApplication([])
fen = QWidget()

# parametre de fenetre
fen.setWindowTitle("Titre de la fenetre")
fen.setGeometry(300, 300, 400, 350)

# QLabel
lbl1 = QLabel(fen)
lbl1.setText("nom : ")
lbl1.setGeometry(10, 10, 50, 30)

lbl2 = QLabel(fen)
lbl2.setText("prenom : ")
lbl2.setGeometry(10, 50, 50, 30)

lbl3 = QLabel(fen)
lbl3.setText("message : ")
lbl3.setGeometry(10, 80, 150, 50)

# QLineEdit
input1 = QLineEdit(fen)
input1.setGeometry(80, 10, 200, 30)
input2 = QLineEdit(fen)
input2.setGeometry(80, 50, 200, 30)

# QPushButton
btn_ok = QPushButton(fen)
btn_ok.setText("Ok")
btn_ok.setGeometry(10, 140, 100, 50)
btn_ok.clicked.connect(action_ok)

btn_cancel = QPushButton(fen)
btn_cancel.setText("Cancel")
btn_cancel.setGeometry(130, 140, 100, 50)
btn_cancel.clicked.connect(action_cancel)

fen.show()
app.exec()