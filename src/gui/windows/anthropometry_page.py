## Aquí va el código de la página de antropometría
from PyQt6.QtWidgets import (
    QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtCore import Qt, pyqtSignal
from src.gui.widgets.custom_widgets import CustomButton

class AnthropometryPage(QWidget):
    def __init__(self):
        super().__init__()

        # CREACIÓN DE WIDGETS
        self.title_label = QLabel("NutriAPP")
        self.title_label.setStyleSheet("""
            QLabel {
            font-size: 24px;
            font-weight: bold;
            margin-top: 5px;
            margin-bottom: 5px;
            }
        """)
        self.title_label.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop
        )

    
        self.muac = QLineEdit() # para escribir el valor MUAC
        self.back_button = CustomButton("Volver", 40, 120, "#2563eb")
        self.accept_button = CustomButton("Aceptar", 40, 120, "#2563eb")

        # CREACIÓN DE LAYOUTS Y BOXES
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        # AÑADIENDO WIDGETS A LAS BOXES
        vbox.addWidget(self.title_label)
        vbox.addWidget(self.muac)

        vbox.addLayout(hbox)
        hbox.addWidget(self.back_button)
        hbox.addWidget(self.accept_button)

        self.setLayout(vbox)