import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox


class InputBoxApp(QWidget):
	def __init__(self):
		super().__init__()
		
		# Set up the window
		self.setWindowTitle("Input Box Example")
		self.setGeometry(50, 50, 200, 150)
		
		# Create layout
		self.layout = QVBoxLayout()
		
		# Create input boxes
		self.label1 = QLabel("Enter first value:", self)
		self.layout.addWidget(self.label1)
		
		self.input1 = QLineEdit(self)
		self.layout.addWidget(self.input1)
		
		self.label2 = QLabel("Enter second value:", self)
		self.layout.addWidget(self.label2)
		
		self.input2 = QLineEdit(self)
		self.layout.addWidget(self.input2)
		
		# Create button
		self.button = QPushButton("Submit", self)
		self.button.clicked.connect(self.handle_submit)
		self.layout.addWidget(self.button)
		
		# Set layout
		self.setLayout(self.layout)
	
	def handle_submit(self):
		# Get input values
		value1 = self.input1.text()
		value2 = self.input2.text()
		
		# Display values in a message box
		msg = QMessageBox(self)
		msg.setWindowTitle("Input Values")
		msg.setText(f"Input 1: {value1}\nInput 2: {value2}")
		msg.exec()


# Run the application
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = InputBoxApp()
	window.show()
	sys.exit(app.exec())
