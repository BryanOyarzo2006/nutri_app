from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
)   
from PyQt6.QtCore import Qt
from src.gui.widgets.custom_widgets import CustomButton, CustomSelect


class InitialPage(QWidget):

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

        self.birthday = QLineEdit()
        self.select_sex = CustomSelect(options=["Hombre", "Mujer"], placeholder="Sexo")
        self.accept_button = CustomButton("Siguiente", 40, 120, "#2563eb")

        # CREACIÓN DE LAYOUTS Y BOXES
        vbox = QVBoxLayout()
        vbox.addWidget(self.title_label)
        vbox.addWidget(self.birthday)
        vbox.addWidget(self.select_sex)
        vbox.addWidget(self.accept_button)

        self.setLayout(vbox)