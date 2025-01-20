from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

def action_validate():
    result = int(input1.text()) * 2
    input2.setText(str(result))

app = QApplication([])
fen = QWidget()

# parametre de fenetre
fen.setWindowTitle("Calcul Double")
fen.setGeometry(300, 300, 400, 150)

# QLabel
lbl1 = QLabel(fen)
lbl1.setText("Entrer la valeur de N:")
lbl1.setGeometry(10, 10, 110, 30)

lbl2 = QLabel(fen)
lbl2.setText("Voici le double:")
lbl2.setGeometry(10, 50, 110, 30)

# QLineEdit
input1 = QLineEdit(fen)
input1.setGeometry(130, 10, 200, 30)
input2 = QLineEdit(fen)
input2.setGeometry(130, 50, 200, 30)

# QPushButton
btn_val = QPushButton(fen)
btn_val.setText("Valider l'operation")
btn_val.setGeometry(130, 100, 200, 30)
btn_val.clicked.connect(action_validate)

fen.show()
app.exec()