# faire une application PyQt6
# contient deux champs X et Y
# un bouton + qui affiche la somme X+Y

from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel

def add():
    somme = int(input_x.text()) + int(input_y.text())
    lbl_result.setText(str(somme))
    print(somme)

app = QApplication([])
fenetre = QWidget()

# QLineEdit
input_x = QLineEdit(fenetre)
input_x.setText("x?")
input_x.setGeometry(20, 20, 60, 30)
input_y = QLineEdit(fenetre)
input_y.setText("y?")
input_y.setGeometry(120, 20, 60, 30)

# QLabel
lbl_result = QLabel(fenetre)
lbl_result.setGeometry(20, 60, 60, 30)
lbl_result.setText("::::")

# QPushButton
btn = QPushButton(fenetre)
btn.setText("+")
btn.setGeometry(20, 100, 30, 30)
btn.clicked.connect(add)

fenetre.setWindowTitle("Calculateur")
fenetre.show()
app.exec()