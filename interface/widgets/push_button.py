__author__ = "greenteamoe"
__status__ = "planning"
__description__ = "Project made with Qt Designer and PySide6"

# IMPORTS
import os

# IMPORT QT CORE
from qt_core import *

class PyPushButton(QPushButton):
    def __init__(
        self,
        text = "",
        height = 40,
        minimum_width = 70,
        text_padding = 75,
        text_color = "#9da5b3",
        icon_path = "",
        icon_color = "#3e4552",
        btn_color = "#3e4552",
        btn_hover = "#434c5e",
        #btn_pressed = "#1b1e24",
        is_active = False
    ):
        super().__init__()

        # Set default parameters
        self.setText(text)
        self.setMinimumHeight(height)
        self.setMaximumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # Custom parameters
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        #self.btn_pressed = btn_pressed
        self.is_active = is_active

        # Set style
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            #btn_pressed = self.btn_pressed,
            is_active = self.is_active,
        )

    def set_style(
        self,
        text_padding = 75,
        text_color = "#9da5b3",
        btn_color = "#3e4552",
        btn_hover = "#6c738c",
        #btn_pressed = "#1b1e24",
        is_active = False
    ):
        style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
        }}
        QPushButton:hover {{
            background-color: {btn_hover};
        }}
        """
        #QPushButton:pressed {{
        #    background-color: {btn_pressed};
        #}}
        

        active_style = f"""
        QPushButton {{
            background-color: {btn_hover};
            border-right: 5px solid #1b1e24;
        }}
        """
        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)