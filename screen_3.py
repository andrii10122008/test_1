from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication


class TestScreen(QWidget):
    def __init__(self, name, age, p1, p2, p3):
        super().__init__()

        self.name = name
        self.age = age
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        
        self.set_win()
        self.initUI()
        self.show()

    def set_win(self):
        self.resize(1280, 720)
        self.setWindowTitle("Результат!")


    def initUI(self):
        self.index = (4 * (self.p1 + self.p2 + self.p3) - 200) / 10

        result_text = self.get_result_text()

        self.lbl_name = QLabel(f"Ім'я: {self.name}")
        self.lbl_age = QLabel(f"Вік: {self.age}")
        self.lbl_result = QLabel(f"Ім'я: {self.name}\nВік: {self.age}\nПульс 1: {self.p1}\nПрисідання: {self.p2}\nПульс 2: {self.p3}")
        self.lbl_work = QLabel(f"Індекс Руф'є: {self.index:.1f}")
        self.lbl_index = QLabel("Тестування")

        self.lbl_result.setStyleSheet("font-size: 16px;")
        self.lbl_name.setStyleSheet("font-size: 16px;")
        self.lbl_age.setStyleSheet("font-size: 16px;")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lbl_name, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.lbl_age, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.lbl_index, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.lbl_result, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.lbl_work, alignment=Qt.AlignmentFlag.AlignLeft)

        self.setLayout(self.layout)

    def get_result_text(self):
        if self.index < 0:
            return "Відмінна робота серця!"
        elif self.index >= 0 and self.index < 5:
            return "Добра робота серця!"
        elif self.index >= 5 and self.index < 10:
            return "Середня робота серця!"
        elif self.index >= 10 and self.index < 15:
            return "Нижче середньої роботи серця!"
        else:
            return "Погана робота серця!"













