from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel,
    QHBoxLayout, QVBoxLayout,
    QPushButton
)
from PyQt5.QtCore import Qt

app = QApplication([])

window = QWidget()
window.setWindowTitle("My Application")
window.resize(600, 400)

txt_Hello = QLabel("Ласкаво просимо до програми визначення стану здоров'я!")
txt.instruction = QLabel("1")
btn_nxt = QPushButton("Почати")

layout = QVBoxLayout()
layout.addWidget(txt_Hello, alignment=Qt.AlignmentFlag.AlignLeft)
layout.addWidget(txt.instruction, alignment=Qt.AlignmentFlag.AlignLeft)
layout.addWidget(btn_nxt, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)

window.show()
app.exec()



