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
        minimum_width = 65,
        text_padding = 72,
        text_color = "#9da5b3",
        icon_path = "",
        icon_color = "#D1D5DA",
        btn_color = "#14151E",
        btn_hover = "#1b1d29",
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
        btn_color = "#14151E",
        btn_hover = "#1b1d29",
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
            border-right: 5px solid #597996;
        }}
        """
        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)

    def paintEvent(self,event):
        # Returning default style
        QPushButton.paintEvent(self, event)

        # Set QPainter
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        rect = QRect(0,0, self.minimum_width, self.height())

        # CALLING PAINT EVENT
        self.draw_icon(qp, self.icon_path, rect, self.icon_color)

        qp.end()

    def draw_icon(self, qp, image, rect, color):

        # Format path
        app_path = os.path.abspath(os.getcwd())
        folder = "interface/images/icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))

        # Draw icons
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon

        )
        painter.end()