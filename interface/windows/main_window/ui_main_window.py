__author__ = "greenteamoe"
__status__ = "planning"
__description__ = "Project made with Qt Designer and PySide6"

# IMPORT QTCORE
from PyQt5 import QtCore
from qt_core import *

# IMPORT PAGES
from interface.pages.ui_pages import Ui_application_pages

# IMPORT CUSTOM WIDGETS
from interface.widgets.push_button import PyPushButton

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
        self.left_menu.setStyleSheet("background-color: #14151E")
        self.left_menu.setMaximumWidth(65)
        self.left_menu.setMinimumWidth(65)

        # LEFT MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        # TOP FRAME MENU
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(40)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        self.left_menu_top_frame.setStyleSheet("#left_menu_top_frame { background-color: red; }")

        # TOP FRAME LAYOUT
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(0)

        # TOP BUTTONS
        self.toggle_button = PyPushButton(
            text = "Hide menu", 
            icon_path = "icon_hamburger.svg"
        )

        self.btn_1 = PyPushButton(
            text = "Home page", 
            is_active = True, 
            icon_path = "icon_home.svg"
        )

        self.btn_2 = PyPushButton(
            text = "Widgets", 
            icon_path = "icon_widgets.svg"
        )

        # ADD TOP BUTTONS TO LAYOUT
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.btn_1)
        self.left_menu_top_layout.addWidget(self.btn_2)

        # MENU SPACER
        self.left_menu_spacer = QSpacerItem(20,20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # BOTTOM FRAME MENU
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(40)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")

        # BOTTOM FRAME LAYOUT
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bottom_layout.setSpacing(0)

        # ADD BOTTOM BUTTONS
        self.settings_btn = PyPushButton(
            text = "Settings", 
            icon_path = "icon_settings.svg"

        )

        # ADD BOTTOM BUTTONS TO LAYOUT
        self.left_menu_bottom_layout.addWidget(self.settings_btn)

        # LABEL VERSION SAMPLE
        self.left_menu_label_version = QLabel("v1.0.0")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMaximumWidth(60)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setStyleSheet("color: #a1a1a1")

        # ADD TO LAYOUT
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)

        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #28293A")

        # Content Layout
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)
        
        # TOP BAR
        self.top_bar = QFrame()
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setStyleSheet("background-color: #1b1e24; color: #a1a1a1")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)

        # Left Label
        self.top_label_left = QLabel("ToolBox made in PySide6")

        # Top Spacer
        self.top_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Right Label
        self.top_label_right = QLabel("| Home page")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI")

        # Add to layout
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)

        # Application pages
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: white")
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)

        # BOTTOM BAR
        self.bottom_bar = QFrame()
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #1b1e24; color: #a1a1a1")

        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10,0,10,0)

        # Bottom Label
        self.bottom_label_left = QLabel("Made with ♥ by @greenteamoe")

        # Bottom Spacer
        self.bottom_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Add to layout
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)

        # Add to content layout
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # ADD WIDGETS
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)