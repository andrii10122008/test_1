from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLabel,
    QHBoxLayout, QVBoxLayout,
    QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt, QTimer, QTime
from screen_3 import TestScreen

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_win()
        self.initUI()
        self.show()
        self.connect_signals()
        

    def set_win(self):
        self.resize(700, 600)
        self.setWindowTitle("Здоров'я")

    def initUI(self):
        self.lbl_timer = QLabel("Таймер: 15")
        self.lbl_timer.setStyleSheet("font-size: 20px;")

        self.lbl_name = QLabel("Введіть ПІБ:")
        self.in_name = QLineEdit()
        self.in_name.setPlaceholderText("ПІБ")

        self.lbl_age = QLabel("Введіть вік:")
        self.in_age = QLineEdit("0")

        self.lbl_test1 = QLabel("Ляжте на спину і заміряйте пульс протягом 15 секунд. натисніть кнопку 'Почати перший тест', щоб запустити таймер")
        self.btn_test1 = QPushButton("Почати перший тест")
        self.in_test1 = QLineEdit("0")

        self.lbl_test2 = QLabel("Виконайте 30 присілань за 45 секунд. Для натисніть кнопку 'Почати робити присідання', щоб запустити лічильник присіданнь")
        self.btn_test2 = QPushButton("Почати робити присідання")
        self.in_test2 = QLineEdit("0")


        self.lbl_test3 = QLabel("Лягте на спину і замірайте пульс спочатку за перші 15 секунд, потім за останні 15 секунд, хвилини без виміру пульсацій. Результати запишіть у видповідні поля.")
        self.btn_test3 = QPushButton("Почати фінальний тест")
        self.in_test3 = QLineEdit("0")

        self.btn_next = QPushButton("Надіслати результати")

        h_top = QHBoxLayout()
        h_top.addWidget(self.lbl_timer)

        layout = QVBoxLayout()
        layout.addLayout(h_top)


        layout.addWidget(self.lbl_name, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.in_name, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.lbl_age, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.in_age, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.lbl_test1, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.btn_test1, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.in_test1, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.lbl_test2, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.btn_test2, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.in_test2, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.lbl_test3, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.btn_test3, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.in_test3, alignment=Qt.AlignmentFlag.AlignLeft)

        layout.addWidget(self.btn_next, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def connect_signals(self):
        self.btn_test1.clicked.connect(self.start_test1)
        self.btn_test2.clicked.connect(self.start_test2)
        self.btn_test3.clicked.connect(self.start_test3)
        self.btn_next.clicked.connect(self.next_click)
    def next_click(self):
        self.sw = TestScreen
        self.name=self.in_name.text(),
        self.age=int(self.in_age.text()),
        self.p1=int(self.in_test1.text()),
        self.p2=int(self.in_test2.text()),
        self.p3=int(self.in_test3.text())
        
        self.sw = TestScreen(self.name, self.age, self.p1, self.p2, self.p3)
        self.sw.show()
        self.close()
        

    def timerEvent(self):
        if self.counter > 0:
            self.counter -= 1
            self.lbl_timer.setText(f"Таймер: {self.counter}")
        else:
            self.timer.stop()
    def start_test1(self):
        self.counter = 15
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(1000)
    def start_test2(self):
        self.counter = 45
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(1000)
    def start_test3(self):
        self.counter = 15
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(1000)
    
            


        







