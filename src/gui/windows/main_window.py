from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
from src.gui.widgets.custon_widgets import CustomButton, CustomSelect

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("NutriApp")
        self.setGeometry(100, 100, 400, 600)

        # Esto crea el Widget Principal y el Layout de la ventana principal
        central = QWidget()

        # Esto anida un layout vertical dentro de uno horizontals
        vbox = QVBoxLayout(central)

        # CREACIÓN DE WIDGETS ================================================================
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

        # AÑADIR WIDGETS =====================================================================
        vbox.addWidget(title_label)
        vbox.addWidget(birthday)
        vbox.addWidget(select_sex)
        vbox.addWidget(accept_button)
        self.setCentralWidget(central)
