from PyQt6.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit,
    QStackedWidget
)   
from PyQt6.QtCore import Qt, pyqtSignal
from src.gui.widgets.custom_widgets import CustomButton, CustomSelect


class InitialPage(QWidget):

    # Definimos la señal personalizada en la clase
    goto_next_section = pyqtSignal()

    def __init__(self):
        super().__init__()

        # CREACIÓN DE WIDGETS
        title_label = QLabel("NutriAPP")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                margin-top: 1px;
                margin-bottom: 1px;
            }
        """)
        title_label.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop
        )

        birthday = QLineEdit()
        select_sex = CustomSelect(options=["Hombre", "Mujer"], placeholder="Sexo")
        accept_button = CustomButton("Siguiente", 40, 120, "#2563eb")

        # CREACIÓN DE LAYOUTS Y BOXES
        vbox = QVBoxLayout()
        vbox.addWidget(title_label)
        vbox.addWidget(birthday)
        vbox.addWidget(select_sex)
        vbox.addWidget(accept_button)

        self.setLayout(vbox)