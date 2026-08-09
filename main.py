import sys
from PyQt6.QtWidgets import QApplication
from src.gui.windows.main_window import MainWindow

if __name__ == "__main__":

    # Con esto creamos la aplicación para ejecutarla
    app = QApplication(sys.argv)

    # La ventana va a ser una instancia de MainWindow
    window = MainWindow()
    window.show() # Llamamos al método show para que aparezca en pantalla

    sys.exit(app.exec())