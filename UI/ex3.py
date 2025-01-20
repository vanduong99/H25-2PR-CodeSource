import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class DoubleCalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Labels
        self.label_input = QLabel("Entrer la valeur de N:")
        self.label_output = QLabel("Voici le double:")

        # Input and Output Fields
        self.input_field = QLineEdit()
        self.output_field = QLineEdit()
        self.output_field.setReadOnly(True)

        # Button
        self.button = QPushButton("Valider l'operation")
        self.button.clicked.connect(self.calculate_double)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_input)
        layout.addWidget(self.input_field)
        layout.addWidget(self.label_output)
        layout.addWidget(self.output_field)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.setWindowTitle("Double Calculator")

    def calculate_double(self):
        try:
            # Get the value from input, calculate the double, and display it
            value = int(self.input_field.text())
            self.output_field.setText(str(value * 2))
        except ValueError:
            self.output_field.setText("Invalid Input")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DoubleCalculatorApp()
    window.show()
    sys.exit(app.exec())
