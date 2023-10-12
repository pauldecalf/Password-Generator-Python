# python3 -m venv venv
# .\venv\Scripts\activate.ps1
# .\venv\bin\pip install pyside6
# Freeze les dépendences
# .\venv\bin\pip freeze > requirement.txt
import random
import string
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

        self.option_lowercase.setChecked(True)
        self.option_number.setChecked(True)

        btn_quit.clicked.connect(self.quit)
        btn_copy.clicked.connect(self.copy)
        btn_generate.clicked.connect(self.generate)


        # Générer un mdp au lancement
        self.generate()

        # Connecter le signal valueChanged du QSlider à une méthode
        self.option_size.valueChanged.connect(self.change_size)
    def quit(self):
        QApplication.quit()
    def copy(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.password_generated.text())
    def change_size(self):
        # Mettre à jour le texte du QLabel avec la valeur du QSlider
        self.txt_size.setText(f"Taille : {self.option_size.value()}")
    def generate(self):
        size = self.option_size.value()
        has_lower = self.option_lowercase.isChecked()
        has_upper = self.option_uppercase.isChecked()
        has_number = self.option_number.isChecked()
        has_special = self.option_special.isChecked()

        all_chars = ''
        if has_lower:
            all_chars += string.ascii_lowercase
        if has_upper:
            all_chars += string.ascii_uppercase
        if has_number:
            all_chars += string.digits
        if has_special:
            all_chars += string.punctuation

        if len(all_chars) == 0:
            self.password_generated.setText("Veuillez sélectionner au moins une option.")
            return

        password = ''.join(random.choice(all_chars) for _ in range(size))
        self.password_generated.setText(f"{password}")

app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle("Richnou Text Editor Moisi")
window.show()
app.exec()
