from PyQt6.QtWidgets import (
    QMainWindow, QStackedWidget
)
from src.gui.windows.initial_page import InitialPage
from src.gui.windows.anthropometry_page import AnthropometryPage

# Clase para la ventana principal de la aplicación
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # INSTANCIACIÓN DE CADA PÁGINA ===================
        self.initial_page = InitialPage()
        self.anthropometry_page = AnthropometryPage()

        # WIDGETS DE CLASES INSTANCIADAS ### lambda es para que no se ejecute la función altiro, solamente cuando se presione el botón
        self.initial_page.accept_button.clicked.connect(lambda: self.change_page("anthropometry"))
        self.anthropometry_page.back_button.clicked.connect(lambda: self.change_page("initial"))
        # VENTANA =====================================
        self.setWindowTitle("NutriApp")
        self.setGeometry(100, 100, 400, 600)

        # LAYOUTS Y BOXES PRINCIPALES========================================
        self.stacked_widget = QStackedWidget() # Aquí creamos el Widget para tener secciones
        self.setCentralWidget(self.stacked_widget) # Lo dejamos como Widget Central.

        # ADICIÓN DE WIDGETS AL STACKEDWIDGET
        self.stacked_widget.addWidget(self.initial_page)
        self.stacked_widget.addWidget(self.anthropometry_page)

        # DICCIONARIO PARA MAPEAR LOS NOMBRES DE LAS RUTAS
        self.sections = {
            "initial": self.initial_page,
            "anthropometry": self.anthropometry_page
        }

    # MÉTODO PARA PODER CAMBIAR LAS SECCIONES DE LA APLICACIÓN
    def change_page(self, destiny_name: str):
        if destiny_name in self.sections:
            widget_destiny = self.sections[destiny_name]
            self.stacked_widget.setCurrentWidget(widget_destiny)