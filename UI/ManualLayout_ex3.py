from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

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
app = QApplication([])

# Create the main window
window = QWidget()
window.setWindowTitle("Double Calculator")
window.setGeometry(100, 100, 300, 200)

# Create widgets
label_input = QLabel("Entrer la valeur de N:", window)
label_input.setGeometry(20, 20, 150, 30)

input_field = QLineEdit(window)
input_field.setGeometry(150, 20, 120, 30)

label_output = QLabel("Voici le double:", window)
label_output.setGeometry(20, 70, 150, 30)

output_field = QLineEdit(window)
output_field.setGeometry(150, 70, 120, 30)
output_field.setReadOnly(True)

button = QPushButton("Valider l'operation", window)
button.setGeometry(150, 120, 120, 30)
button.clicked.connect(calculate_double)

# Show the window
window.show()

# Run the application
app.exec()
