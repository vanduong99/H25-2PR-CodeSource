from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox
import sys

def load_file():
    filename = filename_input.text()
    try:
        with open(filename, 'r') as file:
            content = file.read()
            text_area.setPlainText(content)
            QMessageBox.information(window, "Succès", "Le fichier a été chargé avec succès.")
    except Exception as e:
        print(f"Erreur lors du chargement du fichier : {e}")
        QMessageBox.critical(window, "Erreur", f"Impossible de charger le fichier : {e}")

def save_file():
    filename = filename_input.text()
    try:
        with open(filename, 'w', encoding="utf-8") as file:
            content = text_area.toPlainText()
            file.write(content)
            QMessageBox.information(window, "Succès", "Le fichier a été sauvegardé avec succès.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde du fichier : {e}")
        QMessageBox.critical(window, "Erreur", f"Impossible de sauvegarder le fichier : {e}")

# Application principale
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Petit éditeur de texte")

# Layout principal
central_widget = QWidget()
layout = QVBoxLayout()
central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

# Champ pour saisir le nom de fichier
filename_input = QLineEdit()
filename_input.setPlaceholderText("Nom du fichier")
layout.addWidget(filename_input)

# Zone de texte pour le contenu
text_area = QTextEdit()
layout.addWidget(text_area)

# Boutons Charger et Sauvegarder
button_layout = QHBoxLayout()
layout.addLayout(button_layout)

load_button = QPushButton("Charger")
load_button.clicked.connect(load_file)
button_layout.addWidget(load_button)

save_button = QPushButton("Sauvegarder")
save_button.clicked.connect(save_file)
button_layout.addWidget(save_button)

# Affichage de la fenêtre
window.show()
sys.exit(app.exec())
