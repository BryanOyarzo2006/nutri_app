from PyQt6.QtWidgets import QPushButton, QComboBox

class CustomButton(QPushButton):
    def __init__(self, text, height, width, color = None):
        super().__init__(text)

        self.setMinimumHeight(height)
        self.setMaximumWidth(width)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border-radius: 8px;
            }}

            QPushButton:hover{{
            background-color: #1d4ed8;
            }}
        """)

class CustomSelect(QComboBox):
    
    def __init__(self, options=None, placeholder="Selecciona una opción"):
        super().__init__()

        # Opción por defecto (placeholder)
        self.setPlaceholderText(placeholder)
        self.setCurrentIndex(-1)

        # Añadir opciones que si se reciben en el constructor
        if options:
            self.addItems(options)



        