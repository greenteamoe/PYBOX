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

        # Home btn function event
        self.ui.home_btn.clicked.connect(self.show_page_1)

        # Widget btn function event
        self.ui.widget_btn.clicked.connect(self.show_page_2)

        # Settings btn function event
        self.ui.settings_btn.clicked.connect(self.show_page_3)

        # SHOWING THE WINDOW
        self.show()

    # Function to reset the selection style of the button by finding related parents/children
    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    # Show page function
    def show_page_1(self):
        print("Home page selected")
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.home_btn.set_active(True)

    def show_page_2(self):
        print("Widget page selected")
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.widget_btn.set_active(True)

    def show_page_3(self):
        print("Settings page selected")
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.settings_btn.set_active(True)

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
