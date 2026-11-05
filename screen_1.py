from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel,
    QHBoxLayout, QVBoxLayout,
    QPushButton
)
from PyQt5.QtCore import Qt

from settings_1 import TEST_INFO_TEXT
from screen_2 import TestWin
from settings_1 import BUTTON_STYLE


class Screen(QWidget):
    def __init__(self):
        super().__init__()

        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.resize(1280, 720)
        self.setWindowTitle("Здоров'я")

    def initUI(self):
        self.txt_Hello = QLabel("Ласкаво просимо до програми визначення стану здоров'я!")
        self.txt_instruction = QLabel(TEST_INFO_TEXT)
        self.btn_nxt = QPushButton("Почати")

        self.btn_nxt.setStyleSheet(BUTTON_STYLE)


        self.layout = QVBoxLayout()
        self.layout.addWidget(self.txt_Hello, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.txt_instruction, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.btn_nxt, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.layout)

        self.btn_nxt.clicked.connect(self.next_click)

    def next_click(self):
        self.tw = TestWin()
        self.tw.show()
        self.close()


