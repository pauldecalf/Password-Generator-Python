# python3 -m venv venv
# .\venv\Scripts\activate.ps1
# .\venv\bin\pip install pyside6
# Freeze les dépendences
# .\venv\bin\pip freeze > requirement.txt

import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file_name = ""
        self.file_content = ""
        self.setFixedSize(QSize(300, 150))

        # Créer un widget central pour la QMainWindow
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Créer un layout horizontal pour les deux colonnes
        min_layout = QVBoxLayout()
        central_widget.setLayout(min_layout)  # Aligner le contenu en haut

        option_layout = QGridLayout()
        self.password_generated = QLineEdit()
        button_layout = QHBoxLayout()

        min_layout.addLayout(option_layout)
        min_layout.addWidget(self.password_generated)
        min_layout.addLayout(button_layout)


        btn_quit = QPushButton("Quitter", self)
        btn_copy = QPushButton("Copier", self)
        btn_generate = QPushButton("Générer", self)
        button_layout.addWidget(btn_quit)
        button_layout.addWidget(btn_copy)
        button_layout.addWidget(btn_generate)

        self.txt_size = QLabel(f"Taille : 10")
        option_layout.addWidget(self.txt_size, 0, 0)

        self.option_size = QSlider(Qt.Horizontal)
        self.option_size.setMinimum(0)
        self.option_size.setMaximum(30)
        self.option_size.setValue(10)
        option_layout.addWidget(self.option_size, 1, 0)


        self.option_lowercase = QCheckBox("Minuscules")
        option_layout.addWidget(self.option_lowercase, 0, 1)
        self.option_uppercase = QCheckBox("Majuscules")
        option_layout.addWidget(self.option_uppercase, 1, 1)
        self.option_number = QCheckBox("Chiffres")
        option_layout.addWidget(self.option_number, 0, 2)
        self.option_special = QCheckBox("Symboles")
        option_layout.addWidget(self.option_special, 1, 2)

        # Connecter le signal valueChanged du QSlider à une méthode
        self.option_size.valueChanged.connect(self.update_label)

    def update_label(self):
        # Mettre à jour le texte du QLabel avec la valeur du QSlider
        self.txt_size.setText(f"Taille : {self.option_size.value()}")


app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle("Richnou Text Editor Moisi")
window.show()
app.exec()
