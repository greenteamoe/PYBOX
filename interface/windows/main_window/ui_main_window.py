__author__ = "greenteamoe"
__status__ = "planning"
__description__ = "Project made with Qt Designer and PySide6"

# IMPORT QTCORE
from qt_core import *

# MAIN WINDOW
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # INITIAL AND MINIMUM SIZE OF THE APPLICATION
        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)

        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()

        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # LEFT MENU
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #3e4552")
        self.left_menu.setMaximumWidth(70)

        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282c34")

        # ADD WIDGETS
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)