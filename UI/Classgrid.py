from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox
)
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import Qt
import sys

class PlayerResultsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Liste des joueurs")
        self.setFixedSize(600, 300)
        self.setStyleSheet("background-color: #D3D3D3;")  # Light gray background

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
       # main_layout.setSpacing(2)
        central_widget.setLayout(main_layout)

        # Title
        title = QLabel("Liste des joueurs")
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #000000;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        # Grid layout for player information (directly after the title)
        self.grid_layout = QGridLayout()
        main_layout.addLayout(self.grid_layout)

        # Column headers
        header_name = QLabel("Nom du joueur")
        header_name.setStyleSheet("font-weight: bold;")
        self.grid_layout.addWidget(header_name, 0, 1, Qt.AlignmentFlag.AlignCenter)

        header_points = QLabel("Points accumulés")
        header_points.setStyleSheet("font-weight: bold;")
        self.grid_layout.addWidget(header_points, 0, 2, Qt.AlignmentFlag.AlignCenter)

        # Player labels and input fields
        self.player_names = []
        self.player_scores = []
        for i in range(4):
            player_label = QLabel(f"Joueur #{i + 1}")
            self.grid_layout.addWidget(player_label, i + 1, 0, Qt.AlignmentFlag.AlignRight)

            name_input = QLineEdit()
            name_input.setStyleSheet("background-color: #FFFFFF;")
            self.player_names.append(name_input)
            self.grid_layout.addWidget(name_input, i + 1, 1)

            score_input = QLineEdit()
            score_input.setValidator(QIntValidator(0, 9999))
            score_input.setStyleSheet("background-color: #FFFFFF;")
            self.player_scores.append(score_input)
            self.grid_layout.addWidget(score_input, i + 1, 2)

        # Result fields
        self.total_label = QLabel("Total des points :")
        self.grid_layout.addWidget(self.total_label, 5, 0, Qt.AlignmentFlag.AlignRight)

        self.total_value = QLabel("0")
        self.grid_layout.addWidget(self.total_value, 5, 1)

        self.average_label = QLabel("Moyenne :")
        self.grid_layout.addWidget(self.average_label, 5, 2, Qt.AlignmentFlag.AlignRight)

        self.average_value = QLabel("0")
        self.grid_layout.addWidget(self.average_value, 5, 3)

        self.winner_label = QLabel("Gagnant :")
        self.grid_layout.addWidget(self.winner_label, 6, 0, Qt.AlignmentFlag.AlignRight)

        self.winner_value = QLabel("")
        self.grid_layout.addWidget(self.winner_value, 6, 1)

        # Buttons layout
        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)

        self.load_button = QPushButton("Charger résultats")
        self.load_button.setStyleSheet("background-color: #E0E0E0;")
        self.load_button.clicked.connect(self.load_results)
        button_layout.addWidget(self.load_button)

        self.save_button = QPushButton("Sauvegarder résultats")
        self.save_button.setStyleSheet("background-color: #E0E0E0;")
        self.save_button.clicked.connect(self.save_results)
        button_layout.addWidget(self.save_button)

        self.analyze_button = QPushButton("Analyser résultats")
        self.analyze_button.setStyleSheet("background-color: #E0E0E0;")
        self.analyze_button.clicked.connect(self.analyze_results)
        button_layout.addWidget(self.analyze_button)

    def save_results(self):
        try:
            with open("resultats.txt", "w") as file:
                for i in range(4):
                    name = self.player_names[i].text()
                    score = self.player_scores[i].text()
                    file.write(f"{name},{score}\n")
        except Exception as e:
            self.show_error(f"Erreur lors de la sauvegarde : {e}")

    def load_results(self):
        try:
            with open("resultats.txt", "r") as file:
                for i, line in enumerate(file.readlines()):
                    if i < 4:
                        name, score = line.strip().split(",")
                        self.player_names[i].setText(name)
                        self.player_scores[i].setText(score)
        except Exception as e:
            self.show_error(f"Erreur lors du chargement : {e}")

    def analyze_results(self):
        try:
            total = 0
            highest_score = 0
            winner = ""
            for i in range(4):
                score_text = self.player_scores[i].text()
                score = int(score_text) if score_text.isdigit() else 0
                total += score
                if score > highest_score:
                    highest_score = score
                    winner = self.player_names[i].text()

            average = total / 4 if total > 0 else 0
            self.total_value.setText(str(total))
            self.average_value.setText(f"{average:.1f}")
            self.winner_value.setText(winner if winner else "Aucun")
        except Exception as e:
            self.show_error(f"Erreur lors de l'analyse : {e}")

    def show_error(self, message):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Icon.Critical)
        error_box.setWindowTitle("Erreur")
        error_box.setText(message)
        error_box.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlayerResultsApp()
    window.show()
    sys.exit(app.exec())
