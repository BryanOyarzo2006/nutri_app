from PyQt6.QtWidgets import (
    QMainWindow, QStackedWidget
)
from src.gui.windows.initial_page import InitialPage

# Clase para la ventana principal de la aplicación
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # INSTANCIACIÓN DE CADA PÁGINA ===================
        self.initial_page = InitialPage()

        # VENTANA =====================================
        self.setWindowTitle("NutriApp")
        self.setGeometry(100, 100, 400, 600)

        # LAYOUTS Y BOXES PRINCIPALES========================================
        self.stacked_widget = QStackedWidget() # Aquí creamos el Widget para tener secciones
        self.setCentralWidget(self.stacked_widget) # Lo dejamos como Widget Central.

        # ADICIÓN DE WIDGETS AL STACKEDWIDGET
        self.stacked_widget.addWidget(self.initial_page)
