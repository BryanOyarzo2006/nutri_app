from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QStackedWidget
)
from src.gui.widgets.custon_widgets import CustomButton, CustomSelect

# Clase para la ventana principal de la aplicación

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("NutriApp")
        self.setGeometry(100, 100, 400, 600)

        # CONFIGURACIÓN DE LAYOUTS Y BOXES PRINCIPALES========================================
        self.stacked_widget = QStackedWidget() # Aquí creamos el Widget para tener secciones
        self.setCentralWidget(self.stacked_widget) # Lo dejamos como Widget Central.

        main_pag = QWidget() # Creamos un Widget para la página principal
        main_vbox = QVBoxLayout(main_pag) # Añadimos un QVBoxLayout a la página principal


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
        main_vbox.addWidget(title_label)
        main_vbox.addWidget(birthday)
        main_vbox.addWidget(select_sex)
        main_vbox.addWidget(accept_button)
        self.stacked_widget.addWidget(main_pag) # Añadimos toda la página al QStackedWidget
