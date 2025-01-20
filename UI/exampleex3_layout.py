import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

def calculate_double():
    # Get the value from the input field
    value = input_field.text()
    # Ensure the input is a valid integer
    if value.isdigit():
        double_value = int(value) * 2
        output_field.setText(str(double_value))
    else:
        output_field.setText("Invalid Input")

# Create the application
app = QApplication(sys.argv)

# Create the main window
window = QWidget()
window.setWindowTitle("Double Calculator")

# Create widgets
label_input = QLabel("Entrer la valeur de N:")
label_output = QLabel("Voici le double:")

input_field = QLineEdit()
output_field = QLineEdit()
output_field.setReadOnly(True)

button = QPushButton("Valider l'operation")
button.clicked.connect(calculate_double)

# Set layout
layout = QVBoxLayout()
layout.addWidget(label_input)
layout.addWidget(input_field)
layout.addWidget(label_output)
layout.addWidget(output_field)
layout.addWidget(button)

window.setLayout(layout)

# Show the window
window.show()

# Run the application
sys.exit(app.exec())
