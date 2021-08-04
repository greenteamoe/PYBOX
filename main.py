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

        # CALLING MINIMUM AND INITIAL RESOLUTION METHOD
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # SHOWING THE SCREEN
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
