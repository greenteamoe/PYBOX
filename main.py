__author__ = "greenteamoe"
__status__ = "planning"
__description__ = "Project made with Qt Designer and PySide6"

# IMPORT MODULES
import sys
import os

# IMPORT QTCORE
from qt_core import *

# IMPORT MAIN WINDOW
from interface.windows.main_window.ui_main_window import *

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # APPLICATION TITLE
        self.setWindowTitle("PYBOX")

        # SETUP MAIN WINDOWN AND CALLING MINIMUM AND INITIAL RESOLUTION METHOD
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # Toggle button
        self.ui.toggle_button.clicked.connect(self.toggle_button)

        # SHOWING THE WINDOW
        self.show()

    def toggle_button(self):
        # Get menu width
        menu_width = self.ui.left_menu.width()

        # Check menu width
        width = 65

        # If current menu width is less than 50px, set menu width to 240px
        if menu_width == 65:
            width = 220

        # Start left menu animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)

        # Setting animation speed in ms
        self.animation.setDuration(400)
        
        # Setting animation type
        self.animation.setEasingCurve(QEasingCurve.OutCirc)

        # Starting animation
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
