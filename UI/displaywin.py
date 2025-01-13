# Étape 1

# from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
# # Première étape : création d'une application Qt avec QApplication
# # afin d'avoir un fonctionnement correct avec IDLE ou Spyder
# # on vérifie s'il existe déjà une instance de QApplication
# app = QApplication([])
# # création d'une fenêtre avec QWidget dont on place la référence dans fen
# fen = QWidget()
# # la fenêtre est rendue visible
# fen.show()
# # exécution de l'application, l'exécution permet de gérer les événements
# app.exec()

# Étape 2

# from PyQt6.QtWidgets import QApplication, QWidget
#
# class MyWindow(QWidget):
#     def __init__(self, fen):
#         super().__init__()
#         self.fen = fen
#
#     def build(self):
#         self.fen.setWindowTitle('Hi')
#
#     app = QApplication([])
#      fen = QWidget()
#     mywin = MyWindow(fen)
#     mywin.build()
#
#     fen.show()
#     app.exec()

# Étape 3

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel
# class MyWindow(QWidget):
#     def __init__(self, win):
#         super().__init__()
#         self.win = win
#
#     def build(self):
#         self.win.setWindowTitle("PyQt6 from object approach")
#         self.win.setGeometry(100, 100, 400, 150)
#
#         # create a QLabel
#         qlabel = QLabel(self.win)
#         qlabel.setText("Hello World !")
#         # Use QSS designe
#         qlabel.setStyleSheet(
#             "background: darkblue; border: 2px solid red; color:yellow; font:broadway; font-size:36px;")
#
#         # define the qlabel dimensions & position
#         qlabel.setGeometry(50, 50, 200, 50)
#
# if __name__ == '__main__':
#     app = QApplication([])
#     fen = QWidget()
#     mywin = MyWindow(fen)
#     mywin.build()
#     fen.show()
#     app.exec()
#

# Étape 4
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

app = QApplication([])
widget = QWidget()
widget.setGeometry(50, 50, 350, 200)
widget.setWindowTitle("Label Example")

# create a QLabel
qlabel = QLabel(widget)
qlabel.setText("Hello World !")

# define the qlabel dimensions & position
qlabel.setGeometry(50, 50, 250, 50)

# Use QSS designe
qlabel.setStyleSheet("background: darkblue; border: 2px solid red; color:yellow; font:broadway; font-size:36px;")

widget.show()
app.exec()


